#!/usr/bin/env bash
set -euo pipefail

# Mirror Pear docs for offline reference and module-guide lookups.
# This is a support script for the one-shot Holepunch knowledge sync flow.

DEST="$HOME/.codex/skills-cache/holepunch-p2p-architect/docs/pears"
DRY_RUN=0

while [[ $# -gt 0 ]]; do
  case "$1" in
    --dest)
      DEST="$2"
      shift 2
      ;;
    --dry-run)
      DRY_RUN=1
      shift
      ;;
    --help)
      echo "Usage: fetch_pears_docs.sh [--dest PATH] [--dry-run]"
      exit 0
      ;;
    *)
      echo "Unknown arg: $1" >&2
      exit 1
      ;;
  esac
done

mkdir -p "$DEST"

if command -v wget >/dev/null 2>&1; then
  cmd=(wget --mirror --convert-links --adjust-extension --page-requisites --no-parent https://docs.pears.com -P "$DEST")
  if [[ "$DRY_RUN" -eq 1 ]]; then
    echo "+ ${cmd[*]}"
    exit 0
  fi
  "${cmd[@]}"
  exit 0
fi

if command -v curl >/dev/null 2>&1; then
  if [[ "$DRY_RUN" -eq 1 ]]; then
    echo "+ curl -L https://docs.pears.com -o $DEST/index.html"
    exit 0
  fi
  curl -L https://docs.pears.com -o "$DEST/index.html"
  exit 0
fi

echo "Need wget or curl to fetch docs." >&2
exit 1
