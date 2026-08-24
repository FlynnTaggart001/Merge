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

ROLE_MIN_LEVEL = {
    "RESEARCHER": PermissionLevel.L0_READ,
    "REVIEWER": PermissionLevel.L0_READ,
    "DEVIL_ADVOCATE": PermissionLevel.L0_READ,
    "DOCUMENTATION": PermissionLevel.L1_DOCS,
    "GAMEPLAY_DESIGNER": PermissionLevel.L1_DOCS,
    "WORLD_DESIGNER": PermissionLevel.L1_DOCS,
    "QA": PermissionLevel.L2_CODE,
    "ARCHITECT": PermissionLevel.L2_CODE,
    "PROGRAMMER": PermissionLevel.L2_CODE,
    "RELEASE": PermissionLevel.L3_COMMIT,
}


@dataclass(frozen=True)
class PermissionRequest:
    role: str
    required_level: PermissionLevel
    critical: bool = False
    destructive: bool = False


def minimum_level_for_role(role: str) -> PermissionLevel:
    normalized = role.strip().upper()
    try:
        return ROLE_MIN_LEVEL[normalized]
    except KeyError as exc:
        raise ValueError(f"unknown role: {normalized}") from exc


def authorize(request: PermissionRequest) -> tuple[bool, str]:
    role = request.role.strip().upper()
    if role not in ROLE_MAX_LEVEL:
        return False, f"unknown role: {role}"
    if request.critical or request.destructive:
        return False, "critical/destructive actions require explicit human authorization"
    allowed = ROLE_MAX_LEVEL[role]
    if request.required_level > allowed:
        return False, f"role {role} is limited to {allowed.name}"
    return True, "authorized"


def assert_authorized(request: PermissionRequest) -> None:
    ok, reason = authorize(request)
    if not ok:
        raise PermissionError(reason)
