def format_review(review: dict) -> str:

    summary = review["summary"]

    comment = f"""
# 🤖 AI PR Review

## Summary

- Total Findings: {summary["total_findings"]}
- Overall Severity: {summary["overall_severity"]}

---
"""

    findings = review.get("findings", [])

    if not findings:

        comment += "\n✅ No significant issues found.\n"
        return comment

    for finding in findings:

        comment += f"""
### {finding["severity"]} | {finding["category"]}

**{finding["title"]}**

{finding["description"]}

**Recommendation**

{finding["recommendation"]}

---
"""

    return comment