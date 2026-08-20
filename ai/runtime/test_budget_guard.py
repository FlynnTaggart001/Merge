"""Deterministic offline safety tests. No provider/API is called."""

from budget_guard import BudgetDecision, BudgetGuard, BudgetLimits, Usage


def test_allow_under_limits() -> None:
    guard = BudgetGuard()
    assert guard.authorize(0.10) == BudgetDecision.ALLOW


def test_warn_at_task_threshold() -> None:
    guard = BudgetGuard()
    guard.record_call(Usage(cost_usd=1.40))
    assert guard.authorize(0.10) == BudgetDecision.WARN


def test_warn_at_monthly_threshold_after_resets() -> None:
    guard = BudgetGuard()
    guard.record_call(Usage(cost_usd=35.00))
    guard.reset_day()
    guard.reset_task()
    assert guard.authorize(0.10) == BudgetDecision.WARN


def test_deny_call_limit() -> None:
    guard = BudgetGuard()
    assert guard.authorize(0.51) == BudgetDecision.DENY


def test_deny_task_limit() -> None:
    guard = BudgetGuard()
    guard.record_call(Usage(cost_usd=1.90))
    assert guard.authorize(0.10) == BudgetDecision.WARN
    assert guard.authorize(0.11) == BudgetDecision.DENY


def test_deny_daily_limit_after_task_reset() -> None:
    guard = BudgetGuard()
    guard.record_call(Usage(cost_usd=4.90))
    guard.reset_task()
    assert guard.authorize(0.10) == BudgetDecision.WARN
    assert guard.authorize(0.11) == BudgetDecision.DENY


def test_fail_closed_when_cost_unknown() -> None:
    guard = BudgetGuard()
    assert guard.authorize(None) == BudgetDecision.DENY


def test_retry_limit() -> None:
    guard = BudgetGuard(BudgetLimits(max_retries=3))
    for _ in range(3):
        guard.record_retry()
    try:
        guard.record_retry()
    except RuntimeError as exc:
        assert "Maximum retries exceeded" in str(exc)
    else:
        raise AssertionError("Retry guard failed to stop the fourth retry")


def test_iteration_and_handoff_limits() -> None:
    guard = BudgetGuard(BudgetLimits(max_iterations=2, max_handoffs=2))
    guard.record_iteration()
    guard.record_iteration()
    guard.record_handoff()
    guard.record_handoff()
    for operation in (guard.record_iteration, guard.record_handoff):
        try:
            operation()
        except RuntimeError:
            pass
        else:
            raise AssertionError("Safety limit failed to stop excess activity")


def test_cost_estimation() -> None:
    guard = BudgetGuard()
    # 100k input @ $1/M + 50k output @ $2/M = $0.20
    assert guard.estimate_call(100_000, 50_000, 1.0, 2.0) == 0.20
