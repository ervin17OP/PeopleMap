# TOOLS.md - Local Notes

## Active local tools

- Jira helper:
  - `./scripts/jira search`
  - `./scripts/jira get KAN-1`
  - `./scripts/jira create --summary "..." --description "..."`
  - `./scripts/jira comment KAN-1 --text "..."`
  - `./scripts/jira transitions KAN-1`
  - `./scripts/jira transition KAN-1 <id>`
- Git remote:
  - `origin = https://github.com/ervin17OP/PeopleMap.git`
- Telegram bot:
  - configured and paired as a control channel

## Tool preference

- For task tracking: prefer Jira
- For source control: prefer GitHub Git workflow
- For remote commands: use Telegram
- For deeper supervision and sessions: use OpenClaw Control UI

## Local rules

- Never store secrets in tracked files
- Keep Jira credentials only in `.jira.local.json` or environment variables
- Never create GitHub Issues unless explicitly requested
