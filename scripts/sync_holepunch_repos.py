#!/usr/bin/env python3
"""Sync one or more GitHub orgs into a local cache and refresh the Holepunch org index.

Defaults to the Holepunch-adjacent knowledge set under ~/.codex/skills-cache, including holepunchto, pearopen, and tetherto.
The generated Holepunch org index is written to references/holepunch-org-index.md
unless --no-index is supplied.
Supports --dry-run, --offline, and --shallow.
"""

import argparse
import json
import os
import subprocess
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

DEFAULT_ORGS = ["holepunchto", "pearopen", "tetherto"]
DEFAULT_DEST = os.path.expanduser("~/.codex/skills-cache/holepunch-p2p-architect/repos")
DEFAULT_INDEX_ORG = "holepunch"
DEFAULT_INDEX_OUT = "references/holepunch-org-index.md"


def _run(cmd, dry_run):
    display = " ".join(cmd)
    print(f"+ {display}")
    if dry_run:
        return 0
    return subprocess.run(cmd, check=False).returncode


def _list_repos_via_gh(org):
    try:
        out = subprocess.check_output(
            [
                "gh",
                "repo",
                "list",
                org,
                "--limit",
                "1000",
                "--json",
                "name,description,url,createdAt,updatedAt,pushedAt",
            ],
            text=True,
        )
    except (FileNotFoundError, subprocess.CalledProcessError):
        return None
    try:
        return json.loads(out)
    except json.JSONDecodeError:
        return None


def _list_repos_via_api(org):
    repos = []
    page = 1
    while True:
        url = f"https://api.github.com/orgs/{org}/repos?per_page=100&page={page}&sort=full_name&direction=asc"
        with urllib.request.urlopen(url, timeout=30) as resp:
            data = json.load(resp)
        if not data:
            break
        repos.extend(data)
        page += 1
    return repos


def _load_repo_list(path):
    if not path:
        return []
    p = Path(path)
    if not p.exists():
        return []
    repos = []
    for line in p.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        repos.append(line)
    return repos


def _expand_repo_list(repo_list, orgs):
    expanded = []
    for entry in repo_list:
        if "/" in entry:
            org, repo = entry.split("/", 1)
            if org and repo:
                expanded.append((org, repo))
            continue
        if len(orgs) == 1:
            expanded.append((orgs[0], entry))
        else:
            print(f"Skipping ambiguous repo '{entry}' without org (use org/repo).", file=sys.stderr)
    return expanded


def _short_date(value):
    if not value:
        return "unknown"
    return str(value)[:10]


def _repo_url(org, repo):
    return repo.get("html_url") or repo.get("url") or f"https://github.com/{org}/{repo.get('name', '')}"


def _write_index(index_path, org, repos, dry_run):
    generated_at = datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z")
    lines = [
        "# Holepunch organization repository index",
        "",
        f"Generated at: {generated_at}",
        "",
        f"Source: GitHub org `{org}`",
        "",
        f"Total repositories found: {len(repos)}",
        "",
        "Note: this file is auto-updated by `scripts/sync_holepunch_repos.py`.",
        "",
        "## Repositories",
        "",
    ]

    for repo in sorted(repos, key=lambda item: (item.get("name") or "").lower()):
        name = repo.get("name") or "unknown"
        lines.extend(
            [
                f"- [{org}/{name}]({_repo_url(org, repo)})",
                f"  - Description: {repo.get('description') or 'No description set.'}",
                f"  - Created: {_short_date(repo.get('created_at') or repo.get('createdAt'))} | Updated: {_short_date(repo.get('updated_at') or repo.get('updatedAt'))} | Last pushed: {_short_date(repo.get('pushed_at') or repo.get('pushedAt'))}",
                "",
            ]
        )

    content = "\n".join(lines).rstrip() + "\n"
    path = Path(index_path)
    if dry_run:
        print(f"+ write {path}")
        print(content)
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)


def main():
    parser = argparse.ArgumentParser(description="Sync one or more GitHub orgs into a local cache and refresh the Holepunch org index.")
    parser.add_argument("--org", action="append", default=[], help="GitHub org (repeatable)")
    parser.add_argument("--dest", default=DEFAULT_DEST)
    parser.add_argument("--repo-list", default="", help="Path to a newline-delimited repo list")
    parser.add_argument("--offline", action="store_true", help="Do not use network; rely on repo list")
    parser.add_argument("--dry-run", action="store_true", help="Print commands without executing")
    parser.add_argument("--shallow", action="store_true", help="Clone with --depth=1")
    parser.add_argument("--index-org", default=DEFAULT_INDEX_ORG, help="GitHub org used to refresh the generated org index")
    parser.add_argument("--index-out", default=DEFAULT_INDEX_OUT, help="Path to write the generated org index")
    parser.add_argument("--no-index", action="store_true", help="Skip the org index refresh")
    args = parser.parse_args()

    orgs = args.org if args.org else list(DEFAULT_ORGS)
    dest = Path(args.dest)
    dest.mkdir(parents=True, exist_ok=True)

    repo_tuples = []
    if args.offline:
        repo_list = _load_repo_list(args.repo_list)
        if not repo_list:
            repo_list = ["hypercore", "hyperswarm", "hyperbee"]
        repo_tuples = _expand_repo_list(repo_list, orgs)
    else:
        for org in orgs:
            repos = _list_repos_via_gh(org)
            if repos is None:
                repos = _list_repos_via_api(org)
            repo_tuples.extend((org, repo.get("name") if isinstance(repo, dict) else repo) for repo in repos)

    if not repo_tuples:
        print("No repos found. Provide --repo-list or check network access.", file=sys.stderr)
        return 2

    for org, repo in repo_tuples:
        repo_dir = dest / org / repo
        repo_dir.parent.mkdir(parents=True, exist_ok=True)
        if (repo_dir / ".git").exists():
            code = _run(["git", "-C", str(repo_dir), "fetch", "--all", "--prune"], args.dry_run)
        else:
            clone_cmd = ["git", "clone"]
            if args.shallow:
                clone_cmd += ["--depth", "1"]
            clone_cmd += [f"https://github.com/{org}/{repo}.git", str(repo_dir)]
            code = _run(clone_cmd, args.dry_run)
        if code != 0 and not args.dry_run:
            print(f"Failed on {org}/{repo}", file=sys.stderr)

    if not args.no_index:
        if args.offline:
            print("Skipping Holepunch org index refresh in offline mode.")
        else:
            index_repos = _list_repos_via_gh(args.index_org)
            if index_repos is None:
                index_repos = _list_repos_via_api(args.index_org)
            _write_index(args.index_out, args.index_org, index_repos, args.dry_run)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
