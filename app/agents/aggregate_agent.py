def aggregate_agent(state):

    findings = []

    findings.extend(
        state.get(
            "security_review",
            []
        )
    )

    findings.extend(
        state.get(
            "performance_review",
            []
        )
    )

    findings.extend(
        state.get(
            "quality_review",
            []
        )
    )

    findings.extend(
        state.get(
            "architecture_review",
            []
        )
    )

    overall_severity = "NONE"

    severities = {
        item.get(
            "severity",
            "LOW"
        )
        for item in findings
    }

    if "HIGH" in severities:
        overall_severity = "HIGH"

    elif "MEDIUM" in severities:
        overall_severity = "MEDIUM"

    elif "LOW" in severities:
        overall_severity = "LOW"

    return {
        "final_review": {
            "summary": {
                "total_findings": len(
                    findings
                ),
                "overall_severity": overall_severity
            },
            "findings": findings
        }
    }