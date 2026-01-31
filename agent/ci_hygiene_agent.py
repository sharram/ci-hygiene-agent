def analyze_ci_failure(ci_log: str) -> dict:
    """
    Analyze CI logs and return diagnosis and fix suggestion.
    """

    if "No module named" in ci_log:
        missing_module = (
            ci_log.split("No module named")[-1]
            .strip()
            .strip("'\"")
            .split()[0]
        )

        return {
            "failure_type": "Missing Dependency",
            "root_cause": f"Module '{missing_module}' is imported but not declared in requirements.txt",
            "suggested_patch": f"Add '{missing_module}' to requirements.txt",
            "confidence": 0.95
        }

    return {
        "failure_type": "Unknown",
        "root_cause": "CI failure could not be classified automatically",
        "suggested_patch": "Manual inspection required",
        "confidence": 0.2
    }
