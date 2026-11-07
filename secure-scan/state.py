
"""Shared LangGraph state and finding utilities."""

from typing import Annotated

from langgraph.graph.message import MessagesState


def merge_findings(old: list | None, new: list | None) -> list:
    """Append findings from parallel analyzers, or reset for a new scan."""
    old = old or []
    new = new or []

    # The intake node uses this marker to start a fresh scan.
    if new and isinstance(new[0], dict) and new[0].get("reset"):
        return new[1:]

    return old + new


class ScanState(MessagesState):
    """State shared by the scan workflow and its nodes."""

    url: str
    error: str
    page: dict
    tech: list
    csrf: dict
    findings: Annotated[list, merge_findings]
    report: dict


def finding(
    check: str,
    severity: str,
    title: str,
    detail: str = "",
    fix: str = "",
) -> dict:
    """Build a consistently structured security finding."""
    return {
        "check": check,
        "severity": severity,
        "title": title,
        "detail": detail,
        "fix": fix,
    }
