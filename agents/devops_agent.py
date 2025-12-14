#!/usr/bin/env python3
"""
Simulated DevOps agent.
Usage:
  python agents/devops_agent.py "deploy backend"
Outputs JSON to stdout.
"""

import sys
import time
import json
from helper_scripts import simulate_deploy, simulate_logs, simulate_scale

def run_assistant(query):
    q = query.lower()

    # Deploy simulation
    if "deploy" in q:
        # optional parse component name
        component = "backend"
        if "frontend" in q:
            component = "frontend"
        logs, duration = simulate_deploy(component)
        return {
            "status": "ok",
            "action": "deploy",
            "message": f"Simulated deployment of {component} completed.",
            "logs": logs,
            "meta": {"component": component, "duration_s": duration}
        }

    # Logs simulation
    if "log" in q or "logs" in q:
        target = "ci-cd"
        logs = simulate_logs(target)
        return {
            "status": "ok",
            "action": "logs",
            "message": f"Simulated logs for {target}.",
            "logs": logs,
            "meta": {"target": target}
        }

    # Scale simulation
    if "scale" in q:
        # try to parse replica number
        replicas = None
        for token in q.split():
            if token.isdigit():
                replicas = int(token)
                break
        if replicas is None:
            replicas = 3  # default simulated replicas
        logs, duration = simulate_scale(replicas)
        return {
            "status": "ok",
            "action": "scale",
            "message": f"Simulated scaling to {replicas} replicas.",
            "logs": logs,
            "meta": {"replicas": replicas, "duration_s": duration}
        }

    # Generic reply simulation
    return {
        "status": "ok",
        "action": "reply",
        "message": f"AI response for: {query}",
        "logs": [f"Received input: {query}", "Generated simulated reply."],
        "meta": {}
    }

def main():
    if len(sys.argv) < 2:
        print(json.dumps({"status":"error","message":"No query provided"}))
        sys.exit(1)

    query = " ".join(sys.argv[1:])
    # Run agent and print JSON
    result = run_assistant(query)
    print(json.dumps(result))

if __name__ == "__main__":
    main()
