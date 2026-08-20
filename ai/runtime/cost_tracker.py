"""Persistent-friendly cost/usage accounting primitives."""

from __future__ import annotations

from dataclasses import asdict, dataclass
import json
from pathlib import Path
from typing import Any


@dataclass
class UsageRecord:
    timestamp: str
    provider: str
    model: str
    task_id: str
    input_tokens: int
    output_tokens: int
    cost_usd: float
    status: str


class CostTracker:
    def __init__(self, log_path: Path) -> None:
        self.log_path = log_path
        self.log_path.parent.mkdir(parents=True, exist_ok=True)

    def append(self, record: UsageRecord) -> None:
        with self.log_path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(asdict(record), ensure_ascii=False) + "\n")

    def totals(self) -> dict[str, Any]:
        if not self.log_path.exists():
            return {"calls": 0, "input_tokens": 0, "output_tokens": 0, "cost_usd": 0.0}

        calls = input_tokens = output_tokens = 0
        cost = 0.0
        for line in self.log_path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            row = json.loads(line)
            calls += 1
            input_tokens += int(row.get("input_tokens", 0))
            output_tokens += int(row.get("output_tokens", 0))
            cost += float(row.get("cost_usd", 0.0))
        return {
            "calls": calls,
            "input_tokens": input_tokens,
            "output_tokens": output_tokens,
            "cost_usd": round(cost, 8),
        }
