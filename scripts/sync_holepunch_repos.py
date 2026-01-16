#!/usr/bin/env python3
"""Sync all repos from one or more GitHub orgs into a local cache.

Defaults to the Holepunch org and a cache under ~/.codex/skills-cache.
Supports --dry-run and --offline to avoid network access.
"""

import argparse
import json
import os
import subprocess
import sys
import urllib.request
from pathlib import Path

DEFAULT_ORGS = ["holepunchto"]
DEFAULT_DEST = os.path.expanduser("~/.codex/skills-cache/holepunch-p2p-architect/repos")


def _run(cmd, dry_run):
    display = " ".join(cmd)
    print(f"+ {display}")
    if dry_run:
        return 0
    return subprocess.run(cmd, check=False).returncode


def _list_repos_via_gh(org):
    try:
        out = subprocess.check_output(
            ["gh", "repo", "list", org, "--limit", "1000", "--json", "name", "--jq", ".[].name"],
            text=True,
        )
    except (FileNotFoundError, subprocess.CalledProcessError):
        return None
    repos = [line.strip() for line in out.splitlines() if line.strip()]
    return repos


def _list_repos_via_api(org):
    repos = []
    page = 1
    while True:
        url = f"https://api.github.com/orgs/{org}/repos?per_page=100&page={page}"
        with urllib.request.urlopen(url, timeout=30) as resp:
            data = json.load(resp)
        if not data:
            break
        for item in data:
            name = item.get("name")
            if name:
                repos.append(name)
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


def main():
    parser = argparse.ArgumentParser(description="Sync one or more GitHub orgs into a local cache.")
    parser.add_argument("--org", action="append", default=[], help="GitHub org (repeatable)")
    parser.add_argument("--dest", default=DEFAULT_DEST)
    parser.add_argument("--repo-list", default="", help="Path to a newline-delimited repo list")
    parser.add_argument("--offline", action="store_true", help="Do not use network; rely on repo list")
    parser.add_argument("--dry-run", action="store_true", help="Print commands without executing")
    parser.add_argument("--shallow", action="store_true", help="Clone with --depth=1")
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
            repo_tuples.extend((org, repo) for repo in repos)

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

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
