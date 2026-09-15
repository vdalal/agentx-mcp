# agentx-mcp

Wrap any MCP server so every tool call is screened and recorded before it runs, and set the posture to enforce when you want the dangerous ones stopped.

`agentx-mcp` sits in front of any MCP server's stdio and screens every `tools/call` before it runs. Out of the box it watches: a dangerous call (a destructive database write, an SSRF, a secret read) is recorded and let through, so wrapping a server that works cannot break it, and `agentx-mcp --audit` shows what would have been stopped. Set the posture to enforce and the same call is blocked and handed back to your agent as coaching it can act on, so the agent revises and the run finishes instead of executing the damage. No API key, no gateway, nothing leaves your machine.

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

Then keep using your MCP client normally. Every tool call is screened and recorded.

Watching is silent on purpose: your agent's results are untouched and nothing appears in your chat. See what it caught:

```bash
uvx agentx-mcp --audit
```

That lists what your agent did, what AgentX would have stopped, and what is new since you last looked. It also shows the whole menu: every tool the server offers, how many your agent called, and the ones it never called, since nobody chooses what a third-party server exposes. Add `--calls` for one line per call. `uvx agentx-mcp --review` then approves or rejects what it found, one key each.

To block rather than watch, add one more line to that server's entry:

```jsonc
"env": { "AGENTX_POSTURE": "enforce" }
```

A blocked call comes back as coaching your agent recovers from.

To keep the records per project rather than per user, and to have the proxy match the rules you adopted in that project's `.agentx/rules.json`, name the project in the same env block. The proxy prints where its stores are and how it decided at every start:

```jsonc
"env": { "AGENTX_PROJECT_DIR": "${CLAUDE_PROJECT_DIR}" }   // Claude Code; Cursor and VS Code: "${workspaceFolder}"
```

That is the keyless floor. For the judge that catches what keywords miss, automatic retries, and human escalation on the largest calls, see Recover at https://agentx-core.com/?utm_source=agentx-mcp&utm_medium=repo.

## What it is

A thin launcher for the proxy that ships in [`agentx-security-sdk`](https://pypi.org/project/agentx-security-sdk/). Installing `agentx-mcp` gives you the `agentx-mcp` command with no `--from` needed. MIT licensed.

Docs: https://agentx-core.com/docs?utm_source=agentx-mcp&utm_medium=repo
