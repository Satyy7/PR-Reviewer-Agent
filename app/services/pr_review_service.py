from app.services.github_service import GitHubService
from app.services.gemini_service import GeminiService

from app.formatters.github_comment_formatter import (
    GitHubCommentFormatter
)


class PRReviewService:

    @staticmethod
    def review_pull_request(
        payload: dict
    ):

        pr_info = (
            GitHubService.extract_pr_info(
                payload
            )
        )

        pr_details = (
            GitHubService.get_pr_details(
                owner=pr_info["owner"],
                repo=pr_info["repo_name"],
                pr_number=pr_info["pr_number"]
            )
        )

        diff_content = (
            GitHubService.get_pr_diff(
                pr_details["diff_url"]
            )
        )

        MAX_DIFF_SIZE = 50000

        if len(diff_content) > MAX_DIFF_SIZE:

            diff_content = diff_content[
                :MAX_DIFF_SIZE
            ]

        review = (
            GeminiService()
            .review_diff(
                diff_content
            )
        )

        comment = (
            GitHubCommentFormatter
            .format(review)
        )

        GitHubService.post_pr_comment(
            owner=pr_info["owner"],
            repo=pr_info["repo_name"],
            pr_number=pr_info["pr_number"],
            comment=comment
        )

        return review