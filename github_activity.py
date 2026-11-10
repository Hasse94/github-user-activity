import sys
import json
import urllib.request
import urllib.error


def get_username():
    # sys.argv = what you typed in the terminal
    if len(sys.argv) < 2:
        print("Usage: python github_activity.py <username>")
        sys.exit(1)
    return sys.argv[1]


def fetch_events(username):
    url = f"https://api.github.com/users/{username}/events/public"
    try:
        with urllib.request.urlopen(url) as response:
            return json.loads(response.read())
    except urllib.error.HTTPError as e:
        # e.code is only available INSIDE this block
        if e.code == 404:
            print(f"User '{username}' was not found.")
        else:
            print(f"GitHub returned an error: {e.code}")
        sys.exit(1)
    except urllib.error.URLError:
        print("Could not connect. Check your internet.")
        sys.exit(1)


def format_event(event):
    event_type = event["type"]
    repo = event["repo"]["name"]

    if event_type == "PushEvent":
        branch = event["payload"]["ref"].split("/")[-1]
        return f"Pushed to {branch} in {repo}"
    elif event_type == "WatchEvent":
        return f"Starred {repo}"
    elif event_type == "CreateEvent":
        # ref_type is "repository", "branch" or "tag"
        what = event["payload"].get("ref_type", "something")
        return f"Created a {what} in {repo}"
    elif event_type == "ForkEvent":
        return f"Forked {repo}"
    else:
        return f"{event_type} in {repo}"


username = get_username()
events = fetch_events(username)

if not events:
    print(f"No recent public activity for {username}.")
    sys.exit(0)

for event in events:
    print("- " + format_event(event))