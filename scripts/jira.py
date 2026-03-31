#!/usr/bin/env python3
import argparse
import base64
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path


CONFIG_FILE = Path(".jira.local.json")


def load_config():
    data = {}
    if CONFIG_FILE.exists():
        data.update(json.loads(CONFIG_FILE.read_text(encoding="utf-8-sig")))

    env_map = {
        "base_url": "JIRA_BASE_URL",
        "email": "JIRA_EMAIL",
        "api_token": "JIRA_API_TOKEN",
        "project_key": "JIRA_PROJECT_KEY",
    }
    for key, env_name in env_map.items():
        value = os.getenv(env_name)
        if value:
            data[key] = value

    missing = [key for key in env_map if not data.get(key)]
    if missing:
        raise SystemExit(
            "Missing Jira config values: "
            + ", ".join(missing)
            + ". Use environment variables or .jira.local.json."
        )
    return data


def jira_request(config, method, path, payload=None, query=None):
    url = config["base_url"].rstrip("/") + "/rest/api/3/" + path.lstrip("/")
    if query:
        url += "?" + urllib.parse.urlencode(query)

    auth = f'{config["email"]}:{config["api_token"]}'.encode("utf-8")
    headers = {
        "Authorization": "Basic " + base64.b64encode(auth).decode("ascii"),
        "Accept": "application/json",
    }
    body = None
    if payload is not None:
        body = json.dumps(payload).encode("utf-8")
        headers["Content-Type"] = "application/json"

    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req) as resp:
            raw = resp.read().decode("utf-8")
            return json.loads(raw) if raw else {}
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise SystemExit(f"Jira API error {exc.code}: {detail}") from exc


def cmd_me(config, _args):
    data = jira_request(config, "GET", "myself")
    print(json.dumps(data, indent=2, ensure_ascii=False))


def cmd_get(config, args):
    data = jira_request(config, "GET", f"issue/{args.key}")
    print(json.dumps(data, indent=2, ensure_ascii=False))


def cmd_search(config, args):
    jql = args.jql or f'project = "{config["project_key"]}" ORDER BY created DESC'
    payload = {
        "jql": jql,
        "maxResults": args.limit,
        "fields": ["summary", "status", "assignee", "issuetype"],
    }
    data = jira_request(config, "POST", "search/jql", payload=payload)
    for issue in data.get("issues", []):
        fields = issue["fields"]
        assignee = fields.get("assignee")
        assignee_name = assignee.get("displayName") if assignee else "unassigned"
        print(
            f'{issue["key"]}: {fields["summary"]} '
            f'[{fields["status"]["name"]}] ({fields["issuetype"]["name"]}, {assignee_name})'
        )


def cmd_create(config, args):
    payload = {
        "fields": {
            "project": {"key": config["project_key"]},
            "summary": args.summary,
            "description": {
                "type": "doc",
                "version": 1,
                "content": [
                    {
                        "type": "paragraph",
                        "content": [{"type": "text", "text": args.description}],
                    }
                ],
            },
            "issuetype": {"name": args.issue_type},
        }
    }
    data = jira_request(config, "POST", "issue", payload=payload)
    print(json.dumps(data, indent=2, ensure_ascii=False))


def cmd_comment(config, args):
    payload = {
        "body": {
            "type": "doc",
            "version": 1,
            "content": [
                {
                    "type": "paragraph",
                    "content": [{"type": "text", "text": args.text}],
                }
            ],
        }
    }
    data = jira_request(config, "POST", f"issue/{args.key}/comment", payload=payload)
    print(json.dumps(data, indent=2, ensure_ascii=False))


def cmd_transitions(config, args):
    data = jira_request(config, "GET", f"issue/{args.key}/transitions")
    for item in data.get("transitions", []):
        print(f'{item["id"]}: {item["name"]}')


def cmd_transition(config, args):
    payload = {"transition": {"id": args.transition_id}}
    jira_request(config, "POST", f"issue/{args.key}/transitions", payload=payload)
    print(f"Transition applied to {args.key}: {args.transition_id}")


def build_parser():
    parser = argparse.ArgumentParser(description="Minimal Jira helper for PeopleMap")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("me")

    get_p = sub.add_parser("get")
    get_p.add_argument("key")

    search_p = sub.add_parser("search")
    search_p.add_argument("--jql")
    search_p.add_argument("--limit", type=int, default=10)

    create_p = sub.add_parser("create")
    create_p.add_argument("--summary", required=True)
    create_p.add_argument("--description", required=True)
    create_p.add_argument("--issue-type", default="Task")

    comment_p = sub.add_parser("comment")
    comment_p.add_argument("key")
    comment_p.add_argument("--text", required=True)

    transitions_p = sub.add_parser("transitions")
    transitions_p.add_argument("key")

    transition_p = sub.add_parser("transition")
    transition_p.add_argument("key")
    transition_p.add_argument("transition_id")

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()
    config = load_config()

    commands = {
        "me": cmd_me,
        "get": cmd_get,
        "search": cmd_search,
        "create": cmd_create,
        "comment": cmd_comment,
        "transitions": cmd_transitions,
        "transition": cmd_transition,
    }
    commands[args.command](config, args)


if __name__ == "__main__":
    main()
