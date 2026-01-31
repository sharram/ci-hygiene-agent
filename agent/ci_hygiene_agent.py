
def analyze_ci_log(log_text):
    if "No module named" in log_text:
        missing_module = log_text.split("No module named")[-1].strip().strip("'\"")
        return {
            "error_type": "Missing Dependency",
            "root_cause": f"{missing_module} is imported but not listed in requirements.txt",
            "suggested_fix": f"Add {missing_module} to requirements.txt",
            "confidence": 0.95
        }

    return {
        "error_type": "Unknown",
        "root_cause": "Could not classify error",
        "suggested_fix": "Manual inspection required",
        "confidence": 0.2
    }
