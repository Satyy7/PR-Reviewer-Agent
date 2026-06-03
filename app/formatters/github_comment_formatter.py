class GitHubCommentFormatter:

    @staticmethod
    def format(review: dict) -> str:

        findings = review.get(
            "findings",
            []
        )

        summary = review.get(
            "summary",
            {}
        )

        if not findings:

            return """
# 🤖 AI PR Review

No significant issues were found.
"""

        markdown = "# 🤖 AI PR Review\n\n"

        markdown += (
            f"**Total Findings:** "
            f"{summary.get('total_findings', 0)}\n\n"
        )

        markdown += (
            f"**Overall Severity:** "
            f"{summary.get('overall_severity', 'NONE')}\n\n"
        )

        markdown += "---\n\n"

        for finding in findings:

            markdown += (
                f"## {finding['severity']} | "
                f"{finding['category']}\n\n"
            )

            markdown += (
                f"### {finding['title']}\n\n"
            )

            markdown += (
                f"{finding['description']}\n\n"
            )

            markdown += (
                f"**Recommendation:** "
                f"{finding['recommendation']}\n\n"
            )

            markdown += "---\n\n"

        return markdown