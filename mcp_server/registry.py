TOOL_REGISTRY = {
    "read_ci_logs": "Fetches and returns raw CI log content",
    "diagnose": "Analyzes CI logs and identifies the failure type and root cause",
    "suggest_fix": "Generates a minimal fix suggestion based on diagnosis"
}

def get_registered_tools():
    return TOOL_REGISTRY