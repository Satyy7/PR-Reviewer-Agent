import time

from app.services.github_service import (
    GitHubService
)

from app.formatters.github_comment_formatter import (
    GitHubCommentFormatter
)

from app.graphs.review_graph import (
    review_graph
)

from app.core.logger import (
    logger
)

from app.services.langfuse_service import (
    langfuse
)


class PRReviewService:

    @staticmethod
    def review_pull_request(
        payload: dict
    ):

        logger.info(
            "Extracting PR information"
        )

        pr_info = (
            GitHubService.extract_pr_info(
                payload
            )
        )

        logger.info(
            f"PR #{pr_info['pr_number']}"
        )

        pr_details = (
            GitHubService.get_pr_details(
                owner=pr_info["owner"],
                repo=pr_info["repo_name"],
                pr_number=pr_info["pr_number"]
            )
        )

        logger.info(
            "Downloading diff"
        )

        diff_content = (
            GitHubService.get_pr_diff(
                pr_details["diff_url"]
            )
        )

        MAX_DIFF_SIZE = 50000

        if len(diff_content) > MAX_DIFF_SIZE:

            logger.warning(
                "Diff exceeds limit. Truncating."
            )

            diff_content = (
                diff_content[
                    :MAX_DIFF_SIZE
                ]
            )

        logger.info(
            "Starting LangGraph review"
        )

        start_time = time.time()

        result = (
            review_graph.invoke(
                {
                    "diff": diff_content
                }
            )
        )

        duration = (
            time.time() - start_time
        )

        review = result[
            "final_review"
        ]

        logger.info(
            f"Total findings: "
            f"{review['summary']['total_findings']}"
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

        logger.info(
            "Comment posted successfully"
        )

        logger.info(
            f"Review completed in "
            f"{duration:.2f} seconds"
        )

        langfuse.create_event(
            name="pr_review_completed",
            input={
                "repo": pr_info["repo_name"],
                "pr_number": pr_info["pr_number"]
            },
            output={
                "total_findings": review[
                    "summary"
                ][
                    "total_findings"
                ],
                "duration_seconds": round(
                    duration,
                    2
                )
            }
        )

        langfuse.flush()
        

        return review