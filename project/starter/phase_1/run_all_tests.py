"""Runs all phase_1 demo scripts and records their output to a single .txt file.

Must be run with the `agentic` conda env active (needs openai, pandas,
python-dotenv, sentence-transformers). These scripts make real LLM API
calls, so this prompts for confirmation unless --yes/--dry-run is passed.
"""
import argparse
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

PHASE_1_DIR = Path(__file__).resolve().parent

SCRIPTS = [
    "direct_prompt_agent.py",
    "augmented_prompt_agent.py",
    "knowledge_augmented_prompt_agent.py",
    "action_planning_agent.py",
    "rag_knowledge_prompt_agent.py",
    "routing_agent.py",
    "evaluation_agent.py",
]


def run_script(script_name):
    start = time.monotonic()
    try:
        result = subprocess.run(
            [sys.executable, script_name],
            cwd=PHASE_1_DIR,
            capture_output=True,
            text=True,
            timeout=600,
        )
        elapsed = time.monotonic() - start
        return {
            "returncode": result.returncode,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "elapsed": elapsed,
        }
    except subprocess.TimeoutExpired as e:
        elapsed = time.monotonic() - start
        return {
            "returncode": None,
            "stdout": e.stdout or "",
            "stderr": (e.stderr or "") + "\n[TIMED OUT after 600s]",
            "elapsed": elapsed,
        }


def format_section(script_name, outcome):
    status = "OK" if outcome["returncode"] == 0 else f"FAILED (exit {outcome['returncode']})"
    lines = [
        "=" * 80,
        f"{script_name} — {status} — {outcome['elapsed']:.1f}s",
        "=" * 80,
        "--- stdout ---",
        outcome["stdout"].rstrip() or "(empty)",
    ]
    if outcome["stderr"].strip():
        lines += ["--- stderr ---", outcome["stderr"].rstrip()]
    return "\n".join(lines) + "\n\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="List scripts that would run and exit, no API calls")
    parser.add_argument("-y", "--yes", action="store_true", help="Skip the confirmation prompt")
    parser.add_argument("-o", "--output", type=Path, default=None, help="Output .txt file path")
    args = parser.parse_args()

    if args.dry_run:
        print("Would run, in order:")
        for name in SCRIPTS:
            print(f"  - {name}")
        return

    if not args.yes:
        print("This will run all 7 scripts, making real LLM API calls (billed).")
        reply = input("Proceed? [y/N] ").strip().lower()
        if reply != "y":
            print("Aborted.")
            return

    output_path = args.output or PHASE_1_DIR / f"test_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

    results = []
    with open(output_path, "w") as f:
        f.write(f"Test run: {datetime.now().isoformat()}\n\n")
        for script_name in SCRIPTS:
            print(f"Running {script_name} ...", end=" ", flush=True)
            outcome = run_script(script_name)
            results.append((script_name, outcome))
            status = "OK" if outcome["returncode"] == 0 else f"FAILED (exit {outcome['returncode']})"
            print(f"{status} ({outcome['elapsed']:.1f}s)")
            f.write(format_section(script_name, outcome))

        passed = sum(1 for _, o in results if o["returncode"] == 0)
        total_elapsed = sum(o["elapsed"] for _, o in results)
        summary = f"Summary: {passed}/{len(results)} passed, total {total_elapsed:.1f}s\n"
        f.write(summary)

    print(f"\n{summary}")
    print(f"Results saved to {output_path}")


if __name__ == "__main__":
    main()
