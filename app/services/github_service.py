import requests

from app.core.config import settings


class GitHubService:

    @staticmethod
    def get_authenticated_user():

        response = requests.get(
            "https://api.github.com/user",
            headers={
                "Authorization": f"Bearer {settings.github_token}"
            }
        )

        return response.json()