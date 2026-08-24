"""Offline tests for the supervised team workflow components."""

from __future__ import annotations

import tempfile
from pathlib import Path

from ai.runtime.decision_manager import DecisionManager, HumanDecision, DecisionStatus
from ai.runtime.execution_gate import ExecutionRequest, execute_if_authorized
from ai.runtime.permissions import PermissionLevel, PermissionRequest, authorize
from ai.runtime.project_state import ProjectState, ProjectStateStore
from ai.runtime.proactive_recommendations import scan_project_state
from ai.runtime.role_assignment import assign_role
from ai.runtime.task_planner import DependencyGraph, Task, TaskStatus, validate_task_plan


def test_dependency_graph_blocks_until_dependency_completed():
    a = Task("A", "Build foundation", role="PROGRAMMER", expected_output="code")
    b = Task("B", "Test foundation", role="QA", dependencies=["A"], expected_output="report")
    graph = validate_task_plan([a, b])
    assert [task.task_id for task in graph.ready()] == ["A"]
    a.status = TaskStatus.COMPLETED
    assert [task.task_id for task in graph.ready()] == ["B"]


def test_dependency_cycle_is_rejected():
    a = Task("A", "A", dependencies=["B"], expected_output="x")
    b = Task("B", "B", dependencies=["A"], expected_output="x")
    try:
        validate_task_plan([a, b])
    except ValueError:
        return
    raise AssertionError("cycle should be rejected")


def test_least_privilege_and_critical_actions():
    assert authorize(PermissionRequest("RESEARCHER", PermissionLevel.L0_READ))[0]
    assert not authorize(PermissionRequest("RESEARCHER", PermissionLevel.L2_CODE))[0]
    assert not authorize(PermissionRequest("PROGRAMMER", PermissionLevel.L2_CODE, critical=True))[0]


def test_project_state_round_trip():
    with tempfile.TemporaryDirectory() as directory:
        store = ProjectStateStore(Path(directory) / "state.json")
        state = ProjectState(current_objectives=["finish foundation"])
        store.save(state)
        loaded = store.load()
        assert loaded.current_objectives == ["finish foundation"]


def test_pending_decision_and_approval_gate():
    with tempfile.TemporaryDirectory() as directory:
        manager = DecisionManager(Path(directory) / "decisions.json")
        manager.create(HumanDecision(
            decision_id="D1", problem="major change", context="ctx",
            options=["approve", "reject"], recommendation="approve",
        ))
        try:
            execute_if_authorized(ExecutionRequest(
                task_id="T1", role="PROGRAMMER", action=lambda: "ran", critical=True, decision_id="D1"
            ), manager)
        except PermissionError:
            pass
        else:
            raise AssertionError("pending decision must block execution")
        manager.resolve("D1", DecisionStatus.APPROVED, "human approved")
        assert execute_if_authorized(ExecutionRequest(
            task_id="T1", role="PROGRAMMER", action=lambda: "ran", critical=True, decision_id="D1"
        ), manager) == "ran"


def test_proactive_recommendation_scanner():
    state = ProjectState(blockers=["UE validation"], pending_decisions=["D1"])
    suggestions = scan_project_state(state)
    assert len(suggestions) == 2
    assert any(item.status == "PENDING_HUMAN" for item in suggestions)


def test_role_assignment():
    assert assign_role("implement Unreal C++ movement") == "PROGRAMMER"
    assert assign_role("design factions and lore") == "WORLD_DESIGNER"
    assert assign_role("run regression tests") == "QA"


if __name__ == "__main__":
    tests = [
        test_dependency_graph_blocks_until_dependency_completed,
        test_dependency_cycle_is_rejected,
        test_least_privilege_and_critical_actions,
        test_project_state_round_trip,
        test_pending_decision_and_approval_gate,
        test_proactive_recommendation_scanner,
        test_role_assignment,
    ]
    for test in tests:
        test()
        print("PASS", test.__name__)
    print(f"{len(tests)}/{len(tests)} passed")
