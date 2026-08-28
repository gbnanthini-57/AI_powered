import base64
import requests

from backend.app.config import GITHUB_TOKEN, GITHUB_REPO_OWNER, GITHUB_REPO_NAME

GITHUB_API_URL = "https://api.github.com"

HEADERS = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json",
}


def get_default_branch_sha():
    """Get the latest commit SHA of the main branch, so we know where to branch from."""
    url = f"{GITHUB_API_URL}/repos/{GITHUB_REPO_OWNER}/{GITHUB_REPO_NAME}/git/ref/heads/main"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json()["object"]["sha"]


def create_branch(branch_name):
    """Create a new branch pointing at the current tip of main."""
    base_sha = get_default_branch_sha()

    url = f"{GITHUB_API_URL}/repos/{GITHUB_REPO_OWNER}/{GITHUB_REPO_NAME}/git/refs"
    payload = {
        "ref": f"refs/heads/{branch_name}",
        "sha": base_sha,
    }
    response = requests.post(url, headers=HEADERS, json=payload)
    response.raise_for_status()
    return response.json()


def commit_file(branch_name, file_path, file_content, commit_message):
    """Create or update a file on the given branch with the given content."""
    url = f"{GITHUB_API_URL}/repos/{GITHUB_REPO_OWNER}/{GITHUB_REPO_NAME}/contents/{file_path}"

    encoded_content = base64.b64encode(file_content.encode("utf-8")).decode("utf-8")

    existing_sha = None
    get_response = requests.get(url, headers=HEADERS, params={"ref": branch_name})
    if get_response.status_code == 200:
        existing_sha = get_response.json()["sha"]

    payload = {
        "message": commit_message,
        "content": encoded_content,
        "branch": branch_name,
    }
    if existing_sha:
        payload["sha"] = existing_sha

    response = requests.put(url, headers=HEADERS, json=payload)
    response.raise_for_status()
    return response.json()
def create_pull_request(branch_name, title, body):
    """Open a Pull Request from branch_name into main."""
    url = f"{GITHUB_API_URL}/repos/{GITHUB_REPO_OWNER}/{GITHUB_REPO_NAME}/pulls"
    payload = {
        "title": title,
        "head": branch_name,
        "base": "main",
        "body": body,
    }
    response = requests.post(url, headers=HEADERS, json=payload)
    response.raise_for_status()
    return response.json()