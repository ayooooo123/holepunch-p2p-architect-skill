#!/usr/bin/env bash
set -euo pipefail

# Dump a Pear app for one-shot architecture analysis, module-guide extraction,
# and repo-shape references.

if [[ $# -lt 1 ]]; then
  echo "Usage: pear_dump_app.sh <appkey|pear://appkey> [--dest PATH] [--dry-run]" >&2
  exit 1
fi

APP="$1"
shift

DEST=""
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
      echo "Usage: pear_dump_app.sh <appkey|pear://appkey> [--dest PATH] [--dry-run]"
      exit 0
      ;;
    *)
      echo "Unknown arg: $1" >&2
      exit 1
      ;;
  esac
done

if [[ "$APP" != pear://* ]]; then
  APP="pear://$APP"
fi

if [[ -z "$DEST" ]]; then
  SAFE_KEY="${APP#pear://}"
  DEST="$HOME/.codex/skills-cache/holepunch-p2p-architect/pear-dumps/$SAFE_KEY"
fi

mkdir -p "$DEST"

if [[ "$DRY_RUN" -eq 1 ]]; then
  echo "+ (cd \"$DEST\" && pear dumps \"$APP\")"
  exit 0
fi

(cd "$DEST" && pear dumps "$APP")
