def aggregate_agent(state):

    findings = []

    findings.extend(
        state["security_review"].get(
            "findings",
            []
        )
    )

    findings.extend(
        state["performance_review"].get(
            "findings",
            []
        )
    )

    findings.extend(
        state["quality_review"].get(
            "findings",
            []
        )
    )

    findings.extend(
        state["architecture_review"].get(
            "findings",
            []
        )
    )

    overall_severity = "NONE"

    severities = {
        finding["severity"]
        for finding in findings
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