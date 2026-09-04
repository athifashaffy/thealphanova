#!/usr/bin/env bash
# Run on your Mac or Linux PC. Opens ChatGPT, Claude, MERX, Drive, and the local prompt page.
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
open_url() {
  if command -v open >/dev/null 2>&1; then
    open "$1"
  elif command -v xdg-open >/dev/null 2>&1; then
    xdg-open "$1"
  else
    echo "Open this: $1"
  fi
}
open_url "$HERE/open-on-pc.html"
open_url "https://chatgpt.com"
open_url "https://claude.ai"
open_url "https://www.merx.com"
open_url "https://drive.google.com/drive/folders/1OlzaMxK54cpJyfcwu8r86wBAUKfZGm5V"
echo "ChatGPT writes. Claude edits. You submit. Nothing uploads to a portal from this script."
