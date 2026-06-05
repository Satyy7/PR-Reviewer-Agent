from urllib import response

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
        }

    @staticmethod
    def get_authenticated_user():

        response = requests.get(
            "https://api.github.com/user",
            headers={
                "Authorization": f"Bearer {settings.github_token}",
                "Accept": "application/vnd.github+json"
            }
        )

        response.raise_for_status()

        return response.json()

    @staticmethod
    def get_pr_details(
        owner: str,
        repo: str,
        pr_number: int
    ):

        url = (
            f"https://api.github.com/repos/"
            f"{owner}/{repo}/pulls/{pr_number}"
        )

        response = requests.get(
            url,
            headers={
                "Authorization": f"Bearer {settings.github_token}",
                "Accept": "application/vnd.github+json"
            }
        )

        response.raise_for_status()

        return response.json()
    
    @staticmethod
    def get_pr_diff(diff_url: str):

        response = requests.get(
            diff_url,
            headers={
                "Authorization": f"Bearer {settings.github_token}"
            }
        )

        response.raise_for_status()

        return response.text
    
    @staticmethod
    def post_pr_comment(
        owner: str,
        repo: str,
        pr_number: int,
        comment: str
    ):

        url = (
            f"https://api.github.com/repos/"
            f"{owner}/{repo}/issues/{pr_number}/comments"
        )

        response = requests.post(
            url,
            headers={
                "Authorization": f"Bearer {settings.github_token}",
                "Accept": "application/vnd.github+json"
            },
            json={
                "body": comment
            }
        )

        if not response.ok:
            print("=" * 80)
            print("GITHUB ERROR")
            print("=" * 80)
            print(response.status_code)
            print(response.text)

        response.raise_for_status()

        return response.json()