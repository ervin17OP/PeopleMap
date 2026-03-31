# Jira Workflow

PeopleMap includes a small Jira helper for local agent workflows.

## Local config

Create a local, ignored file named `.jira.local.json` at the repository root:

```json
{
  "base_url": "https://example.atlassian.net",
  "email": "name@example.com",
  "api_token": "replace-me",
  "project_key": "KAN"
}
```

This file is ignored by Git and should never be committed.

## Commands

Run from the repository root:

```bash
./scripts/jira me
./scripts/jira search
./scripts/jira get KAN-1
./scripts/jira create --summary "Create landing page" --description "Bootstrap the first user-facing page"
./scripts/jira comment KAN-1 --text "Implementation has started."
./scripts/jira transitions KAN-1
./scripts/jira transition KAN-1 31
```

## Intended use

- Create tickets from a coding workflow
- Read ticket details before implementation
- Comment progress back to Jira
- Move issues across workflow states once work advances
