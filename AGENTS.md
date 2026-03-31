# PeopleMap Agent Guide

This repository is intended to be the active OpenClaw workspace.

## Working rules

- Prefer small, reviewable changes.
- Summarize the plan before risky actions.
- Do not deploy or touch production unless explicitly requested.
- Do not run destructive database actions without a short impact summary first.
- Keep setup and run commands documented in `README.md` as the project evolves.

## Current state

- Fresh repository
- No framework chosen yet
- No database selected yet
- GitHub remote connected: `https://github.com/ervin17OP/PeopleMap.git`
- Default branch: `main`
- Jira helper available locally via `./scripts/jira`
- Current Jira project key: `KAN`

## First objective

Help define the product, choose the stack, scaffold the app, and start implementation.

## GitHub workflow

- Work in this local repository and use Git normally.
- Before committing, summarize the intended changes.
- Prefer creating a feature branch for non-trivial work.
- After changes, use:
  - `git status`
  - `git add ...`
  - `git commit -m "..."`
  - `git push -u origin <branch>`
- Never force-push unless explicitly requested.
- If asked to push directly, verify the current branch and remote first.

## Jira workflow

- Use `./scripts/jira search` to inspect recent Jira issues.
- Use `./scripts/jira get KAN-1` to read a ticket in detail.
- Use `./scripts/jira create ...` to create a task when asked.
- Use `./scripts/jira comment KAN-1 --text "..."` to post progress updates.
- Use Jira issue keys in branch names, commit messages, and PR titles when the work maps to a ticket.
