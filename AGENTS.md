# PeopleMap Agent Guide

This repository is intended to be the active OpenClaw workspace.

## Working rules

- Prefer small, reviewable changes.
- Summarize the plan before risky actions.
- Do not deploy or touch production unless explicitly requested.
- Do not run destructive database actions without a short impact summary first.
- Keep setup and run commands documented in `README.md` as the project evolves.
- Prefer Jira over GitHub Issues for work tracking in this project.
- Do not create GitHub Issues unless the user explicitly asks for GitHub Issues.
- Keep `SUIVI.md` updated after each meaningful task or session.

## Current state

- Fresh repository
- No framework chosen yet
- No database selected yet
- GitHub remote connected: `https://github.com/ervin17OP/PeopleMap.git`
- Default branch: `main`
- Jira helper available locally via `./scripts/jira`
- Current Jira project key: `KAN`
- Telegram is used as a command channel for OpenClaw
- GitHub is connected and can be used for branches, commits, and pushes

## First objective

Help define the product, choose the stack, scaffold the app, and start implementation.

## GitHub workflow

- Work in this local repository and use Git normally.
- Before committing, summarize the intended changes.
- Prefer creating a feature branch for non-trivial work.
- Never start non-trivial work directly on `main`.
- Use `main` only as the stable integration branch unless the user explicitly asks otherwise.
- After changes, use:
  - `git status`
  - `git add ...`
  - `git commit -m "..."`
  - `git push -u origin <branch>`
- Never force-push unless explicitly requested.
- If asked to push directly, verify the current branch and remote first.
- When work is tied to a Jira ticket, branch names and commits must include the Jira key.
- If GitHub push from WSL fails because of auth, use the Windows-authenticated wrapper:
  - `cmd.exe /c C:\Users\ervin\PeopleMap\scripts\git-push.cmd <branch>`

## Branch naming

- Preferred format: `feature/KAN-123-short-description`
- Alternative for fixes: `fix/KAN-123-short-description`
- Alternative for chores: `chore/KAN-123-short-description`
- Use lowercase words separated by hyphens after the Jira key.

## Jira workflow

- Jira is the source of truth for task tracking in this project.
- Use `./scripts/jira search` to inspect recent Jira issues.
- Use `./scripts/jira get KAN-1` to read a ticket in detail.
- Use `./scripts/jira create ...` to create a task when asked.
- Use `./scripts/jira comment KAN-1 --text "..."` to post progress updates.
- Use Jira issue keys in branch names, commit messages, and PR titles when the work maps to a ticket.
- Before implementation tied to a ticket:
  - read the ticket first
  - summarize the goal
  - create the matching branch
- After meaningful progress:
  - commit with the Jira key
  - push the branch
  - comment on the Jira ticket with a short status update

## Commit message policy

- Preferred format: `KAN-123 short imperative summary`
- Examples:
  - `KAN-4 initialize project scaffold`
  - `KAN-7 add Jira helper commands`
- Do not use vague commit messages like `update`, `fix stuff`, or `changes`.

## Telegram operating mode

- Telegram is a command surface, not the source of truth.
- When a Telegram request refers to a task, prefer mapping it to an existing Jira ticket.
- If no Jira ticket exists and the request is substantial, propose creating one first.
- When the user asks to "create a ticket", always use the local Jira helper:
  - `./scripts/jira create ...`
- Do not default to GitHub Issues for ticket creation.

## Execution policy

- Allowed by default:
  - reading repository files
  - creating or updating Jira tickets
  - creating branches
  - coding in the current workspace
  - committing changes
  - pushing to GitHub
- Ask for confirmation before:
  - database schema changes
  - destructive data operations
  - deployment to staging or production
  - secret rotation or credential changes

## Standard delivery flow

1. Read the Jira ticket or create it if explicitly requested.
2. Summarize the goal and planned steps.
3. Create a branch named with the Jira key.
4. Implement the change.
5. Run relevant checks if available.
6. Commit with the Jira key.
7. Push the branch to GitHub.
8. Comment on the Jira ticket with progress, status, and next step.

## Persistent task log

- `SUIVI.md` is the persistent handoff log for this repository.
- Update it after each meaningful action so another agent or human can quickly understand:
  - what was requested
  - what was done
  - what files changed
  - what commands or checks were run
  - what remains to do
  - any blockers or risks
- Prefer appending a short dated entry rather than rewriting history.
- If a Jira ticket exists, include the Jira key in the entry title.
- If work was pushed to GitHub, note the branch and latest commit hash.
- Before starting a new task, read the latest relevant entries in `SUIVI.md`.
