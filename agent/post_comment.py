import os
import requests
from dotenv import load_dotenv
from agent.ci_hygiene_agent import analyze_ci_failure

load_dotenv()

TOKEN = os.getenv("GITHUB_TOKEN")
OWNER = os.getenv("GITHUB_OWNER")
REPO = os.getenv("GITHUB_REPO")

def post_fix_comment(pr_number: int, log_path: str = "ci_logs.txt"):
    """Reads CI logs, diagnoses the failure, and posts a fix suggestion as a PR comment."""

    # Read logs
    with open(log_path, "r") as f:
        logs = f.read()

    # Diagnose
    diagnosis = analyze_ci_failure(logs)

    # Build comment body
    comment = f"""**DietCode CI Agent — Fix Suggestion**

---
**What failed:** {diagnosis.get('failure_type', 'Unknown')}

**Why it failed:** {diagnosis.get('root_cause', 'Could not determine root cause')}

**Suggested fix:** {diagnosis.get('suggested_patch', 'No fix available')}

**Confidence:** {diagnosis.get('confidence', 'N/A')}

---
⏳ *This fix has NOT been applied. Awaiting maintainer approval.*
"""

    # Post to GitHub
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/issues/{pr_number}/comments"
    headers = {
        "Authorization": f"token {TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    response = requests.post(url, json={"body": comment}, headers=headers)

    if response.status_code == 201:
        print(f"Comment posted on PR #{pr_number}")
    else:
        print(f"Failed to post comment: {response.status_code} — {response.text}")

if __name__ == "__main__":
    import sys
    pr_number = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    post_fix_comment(pr_number)