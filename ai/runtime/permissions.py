"""Least-privilege permission policy for Merge AI roles."""

from __future__ import annotations

from dataclasses import dataclass
from enum import IntEnum


class PermissionLevel(IntEnum):
    L0_READ = 0
    L1_DOCS = 1
    L2_CODE = 2
    L3_COMMIT = 3
    L4_MERGE = 4
    L5_CRITICAL = 5


ROLE_MAX_LEVEL = {
    "RESEARCHER": PermissionLevel.L0_READ,
    "REVIEWER": PermissionLevel.L0_READ,
    "DEVIL_ADVOCATE": PermissionLevel.L0_READ,
    "QA": PermissionLevel.L2_CODE,
    "DOCUMENTATION": PermissionLevel.L1_DOCS,
    "GAMEPLAY_DESIGNER": PermissionLevel.L1_DOCS,
    "WORLD_DESIGNER": PermissionLevel.L1_DOCS,
    "ARCHITECT": PermissionLevel.L2_CODE,
    "PROGRAMMER": PermissionLevel.L3_COMMIT,
    "RELEASE": PermissionLevel.L4_MERGE,
}


@dataclass(frozen=True)
class PermissionRequest:
    role: str
    required_level: PermissionLevel
    critical: bool = False
    destructive: bool = False


def authorize(request: PermissionRequest) -> tuple[bool, str]:
    if request.role not in ROLE_MAX_LEVEL:
        return False, f"unknown role: {request.role}"
    if request.critical or request.destructive:
        return False, "critical/destructive actions require explicit human authorization"
    allowed = ROLE_MAX_LEVEL[request.role]
    if request.required_level > allowed:
        return False, f"role {request.role} is limited to {allowed.name}"
    return True, "authorized"


def assert_authorized(request: PermissionRequest) -> None:
    ok, reason = authorize(request)
    if not ok:
        raise PermissionError(reason)
