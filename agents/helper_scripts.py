import time
import random

def simulate_deploy(component="backend"):
    logs = []
    start = time.time()

    steps = [
        f"Preparing container image for {component}...",
        "Pulling base image...",
        "Installing dependencies...",
        "Building application...",
        "Running unit tests...",
        "Packaging container image...",
        "Pushing image to registry (simulated)...",
        "Updating deployment (simulated)...",
        "Waiting for pods to become ready (simulated)..."
    ]

    for s in steps:
        logs.append(s)
        # simulate variable work
        time.sleep(0.12 + random.random()*0.18)

    # final checks
    logs.append("Health checks passed (simulated).")
    logs.append(f"{component} deployed successfully (simulated).")

    duration = round(time.time() - start, 2)
    return logs, duration

def simulate_logs(target="ci-cd"):
    # produce a set of log lines resembling CI/CD output
    lines = [
        "[ci] Checkout repository",
        "[ci] Install dependencies",
        "[ci] Run tests",
        "[ci] Build container image",
        "[ci] Push container image to registry (simulated)",
        "[ci] Deploy to cluster (simulated)",
        "[ci] Post-deploy smoke tests (simulated)"
    ]
    # add timestamps and small randomization
    out = []
    for i, l in enumerate(lines):
        out.append(f"{2025}-{12:02d}-{12:02d} 12:{10+i:02d} - {l}")
    out.append("----- End of simulated logs -----")
    return out

def simulate_scale(replicas=3):
    logs = []
    start = time.time()
    logs.append(f"Requested scale to {replicas} replicas (simulated).")
    # simulate scaling steps
    for i in range(1, replicas + 1):
        logs.append(f"Creating pod replica-{i} (simulated)...")
        time.sleep(0.08)
    logs.append("All replicas are ready (simulated).")
    duration = round(time.time() - start, 2)
    return logs, duration
