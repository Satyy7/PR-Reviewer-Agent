import requests

from app.core.config import settings


class GitHubService:

    @staticmethod
    def extract_pr_info(payload: dict):

        return {
            "action": payload["action"],
            "pr_number": payload["number"],
            "repo_name": payload["repository"]["name"],
            "owner": payload["repository"]["owner"]["login"],
            "head_branch": payload["pull_request"]["head"]["ref"],
            "base_branch": payload["pull_request"]["base"]["ref"]
            "action": payload.get("action"),
            "repository": payload.get("repository", {}).get("name"),
            "pr_number": payload.get("pull_request", {}).get("number"),
        }

    @staticmethod
    def get_authenticated_user():

        response = requests.get(
            "https://api.github.com/user",
            headers={
                "Authorization": f"Bearer {settings.github_token}"
            }
        )

        return response.json()