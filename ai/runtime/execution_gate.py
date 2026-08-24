"""Execution gate for validated AI work.

No workflow component may execute a critical/destructive action implicitly.
A human decision ID must be APPROVED before the action can be dispatched.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

from .decision_manager import DecisionManager, DecisionStatus
from .permissions import PermissionLevel, PermissionRequest, authorize


@dataclass(frozen=True)
class ExecutionRequest:
    task_id: str
    role: str
    action: Callable[[], object]
    required_level: PermissionLevel = PermissionLevel.L2_CODE
    critical: bool = False
    destructive: bool = False
    decision_id: str | None = None


def execute_if_authorized(request: ExecutionRequest, decisions: DecisionManager) -> object:
    critical_action = request.critical or request.destructive or request.required_level >= PermissionLevel.L4_MERGE
    if critical_action:
        if not request.decision_id:
            raise PermissionError("explicit human decision required")
        data = decisions._load()
        raw = next((d for d in data["decisions"] if d["decision_id"] == request.decision_id), None)
        if raw is None:
            raise PermissionError(f"unknown decision {request.decision_id}")
        status = DecisionStatus(raw["status"])
        if status is not DecisionStatus.APPROVED:
            raise PermissionError(f"decision {request.decision_id} is {status.value}, not APPROVED")

    ok, reason = authorize(PermissionRequest(
        role=request.role,
        required_level=request.required_level,
        critical=False,
        destructive=False,
    ))
    if not ok:
        raise PermissionError(reason)
    return request.action()
