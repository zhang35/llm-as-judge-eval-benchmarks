"""Slim the AgentRewardBench trajectories to what a text-only judge reads.

The Hugging Face dataset McGill-NLP/agent-reward-bench stores, for every step of every trajectory, the full
accessibility tree twice (text and object form), the agent's whole prompt (chat_messages, which repeats the
tree), bounding boxes and element properties. That is ~30 GB for ~1,400 trajectories. The benchmark's own
judge (agent_reward_bench/judge/__init__.py) reads only: the goal, each step's url / action / reasoning,
and the LAST step's accessibility tree (plus the last screenshot, which text-only judges don't use).

Run this where the download is, then copy the output folder to benchmarks/agent-reward-bench/trajectories/cleaned
in the repo. The folder layout and file names are unchanged, so the benchmark's scoring scripts still work.

    python -I slim_agent_reward_bench.py <path-to>/cleaned <output-dir> [--no-axtree]

--no-axtree drops the last step's tree too (actions only, the paper's "Neither" setting). Default keeps it.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

STEP_KEYS = ("num", "url", "action", "reasoning", "last_action_error")
TRAJ_KEYS = ("benchmark", "agent", "model", "valid", "experiment", "goal", "seed", "summary_info")


def slim(traj: dict, keep_axtree: bool) -> dict:
    out = {k: traj[k] for k in TRAJ_KEYS if k in traj}
    steps = traj.get("steps") or []
    out["steps"] = [{k: s.get(k) for k in STEP_KEYS} for s in steps]
    out["num_steps"] = len(steps)
    if keep_axtree and steps:
        last = steps[-1]
        # the text form is what the judge template inserts; the pruned variant when the dataset has it
        out["last_axtree"] = last.get("axtree_pruned") or last.get("axtree") or ""
        out["last_screenshot_path"] = last.get("screenshot_path")
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("src", type=Path, help="the downloaded cleaned/ folder")
    ap.add_argument("dst", type=Path, help="where to write the slim copy (same layout)")
    ap.add_argument("--no-axtree", action="store_true", help="drop the last step's accessibility tree too")
    a = ap.parse_args()

    files = sorted(a.src.rglob("*.json"))
    if not files:
        print(f"no .json files under {a.src}", file=sys.stderr)
        return 1
    before = after = 0
    for i, f in enumerate(files, 1):
        rel = f.relative_to(a.src)
        try:
            traj = json.loads(f.read_bytes())
        except (json.JSONDecodeError, UnicodeDecodeError) as e:
            print(f"skip {rel}: {e}", file=sys.stderr)
            continue
        out = a.dst / rel
        out.parent.mkdir(parents=True, exist_ok=True)
        data = json.dumps(slim(traj, keep_axtree=not a.no_axtree), ensure_ascii=False).encode()
        out.write_bytes(data)
        before += f.stat().st_size
        after += len(data)
        if i % 100 == 0 or i == len(files):
            print(f"{i}/{len(files)}  {before / 1e9:.2f} GB -> {after / 1e6:.1f} MB", file=sys.stderr)
    print(f"done: {len(files)} trajectories, {before / 1e9:.2f} GB -> {after / 1e6:.1f} MB, written to {a.dst}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
