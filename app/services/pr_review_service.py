from app.services.github_service import GitHubService
from app.services.gemini_service import GeminiService


class PRReviewService:

    @staticmethod
    def review_pull_request(payload: dict):

        pr_info = GitHubService.extract_pr_info(payload)

        pr_details = GitHubService.get_pr_details(
            owner=pr_info["owner"],
            repo=pr_info["repo_name"],
            pr_number=pr_info["pr_number"]
        )

        diff_content = GitHubService.get_pr_diff(
            pr_details["diff_url"]
        )

        review = GeminiService().review_diff(
            diff_content
        )

        return {
            "pr_info": pr_info,
            "review": review
        }