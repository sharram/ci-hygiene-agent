import argparse
from agent.ci_hygiene_agent import analyze_ci_failure

def main():
    parser = argparse.ArgumentParser(description="CI Hygiene MCP Server")
    parser.add_argument("--ci-log", required=True, help="Path to CI log file")
    args = parser.parse_args()

    with open(args.ci_log, "r") as f:
        ci_log = f.read()

    print("🔍 CI Hygiene Agent invoked")

    result = analyze_ci_failure(ci_log)

    print("\n--- CI Diagnosis ---")
    for key, value in result.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
