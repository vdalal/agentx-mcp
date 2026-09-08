"""agentx-mcp: the keyless MCP security shield, one line in your mcp.json.

Wrap any MCP server's launch command with `agentx-mcp` and every tools/call is
screened before it runs. Out of the box it watches: a dangerous call (a destructive
database write, an SSRF, a secret read) is recorded and let through, and
`agentx-mcp --audit` shows what would have been stopped. Set the posture to enforce
and the same call is blocked and returned to your agent as coaching it can act on, so
the agent revises and the run survives instead of executing the damage. No API key,
no gateway, nothing leaves your machine.

The proxy itself lives in `agentx-security-sdk` (imported as `agentx_sdk`); this
package is the launcher that lets `uvx agentx-mcp ...` and `pipx run agentx-mcp ...`
resolve with no `--from`. Same command and behavior as the `agentx-mcp` shipped
inside the SDK.
"""
from agentx_sdk.mcp_proxy import main  # re-export the real proxy entry point

__all__ = ["main"]
# KEEP IN SYNC with pyproject.toml::[project].version (BACKLOG C12d).
# These two version strings were unbound: a bump to one could silently leave the other
# behind, so the wheel's metadata and the package's own report of itself could disagree.
# test_version_gate.py now binds them.
__version__ = "0.2.0"
