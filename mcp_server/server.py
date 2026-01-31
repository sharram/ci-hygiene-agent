from mcp import Server
from agent.ci_hygiene_agent import analyze_ci_failure

server = Server("dietcode-ci-agent")

@server.tool()
def read_ci_logs(log_path: str = "ci_logs.txt") -> dict:
    """Reads the CI log file and returns its contents."""
    try:
        with open(log_path, "r") as f:
            content = f.read()
        return {"status": "ok", "logs": content}
    except FileNotFoundError:
        return {"status": "error", "message": f"Log file not found: {log_path}"}

@server.tool()
def diagnose(log_path: str = "ci_logs.txt") -> dict:
    """Reads CI logs and runs the diagnosis agent on them."""
    log_result = read_ci_logs(log_path)
    if log_result["status"] == "error":
        return log_result
    diagnosis = analyze_ci_failure(log_result["logs"])
    return {"status": "ok", "diagnosis": diagnosis}

@server.tool()
def suggest_fix(log_path: str = "ci_logs.txt") -> dict:
    """Returns a human-readable fix suggestion based on CI logs."""
    result = diagnose(log_path)
    if result["status"] == "error":
        return result
    return {
        "status": "ok",
        "diagnosis": result["diagnosis"],
        "message": "Fix suggestion ready. Awaiting human approval before any changes."
    }

if __name__ == "__main__":
    server.run()