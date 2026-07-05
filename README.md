# agentx-mcp

Wrap any MCP server so a poisoned tool call cannot wreck your system, and your agent keeps working.

`agentx-mcp` sits in front of any MCP server's stdio and screens every `tools/call` before it runs. When a call is dangerous (a destructive database write, an SSRF, a secret read), it is blocked and handed back to your agent as coaching it can act on, so the agent revises and the run finishes instead of executing the damage. No API key, no gateway, nothing leaves your machine.

## Use it

No install needed with `uvx`:

```jsonc
// mcp.json / claude_desktop_config.json / .cursor/mcp.json
{
  "command": "uvx",
  "args": ["agentx-mcp", "npx", "-y", "your-mcp-server", "..."]
}
```

Or install it persistently:

```bash
pipx install agentx-mcp        # or: pip install agentx-mcp
agentx-mcp npx -y your-mcp-server ...
```

Then keep using your MCP client normally. Every tool call is screened; a blocked call comes back as coaching your agent recovers from.

That is the keyless Shield. For the judge that catches what keywords miss, automatic retries, and human escalation on the largest calls, see Recover at https://agentx-core.com.

## What it is

A thin launcher for the proxy that ships in [`agentx-security-sdk`](https://pypi.org/project/agentx-security-sdk/). Installing `agentx-mcp` gives you the `agentx-mcp` command with no `--from` needed. MIT licensed.

Docs: https://agentx-core.com/docs
