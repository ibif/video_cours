#!/bin/bash
set -euo pipefail

# Only relevant for Claude Code on the web (ephemeral remote containers).
if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

# Already installed in this container (e.g. resumed session) — nothing to do.
if [ -x "$HOME/.local/bin/claude-fugu" ]; then
  exit 0
fi

# claude-fugu's installer requires a Sakana API key. It must be provided as a
# persistent environment variable configured in the platform's environment
# settings — never committed to this repo. Skip gracefully if absent.
if [ -z "${SAKANA_API_KEY:-}" ]; then
  echo "[session-start] SAKANA_API_KEY not set — skipping claude-fugu install. Configure it in the environment's settings to enable auto-install." >&2
  exit 0
fi

echo "[session-start] Installing claude-fugu..." >&2
export FUGU_INSTALL_TARGET=claude
curl -fsSL https://sakana.ai/fugu/install | bash
