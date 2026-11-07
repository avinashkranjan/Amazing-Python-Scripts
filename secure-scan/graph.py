
"""LangGraph workflow assembly for SecureScan AI."""


from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import END, START, StateGraph

from state import ScanState
from nodes.nodes import (
    ANALYZERS,
    intake,
    route_intake,
    scope_check,
    route_scope,
    load_page,
    route_after_load,
    score_report,
    summarize,
    followup,
    reject,
)
from tools.headers import analyze_headers
from tools.cookies import analyze_cookies
from tools.csrf import analyze_csrf
from tools.scripts import analyze_scripts
from tools.technologies import detect_tech


def build_graph():
    """Build and compile the SecureScan AI workflow."""

    builder = StateGraph(ScanState)

    # Register the workflow nodes.
    node_functions = {
        "intake": intake,
        "scope_check": scope_check,
        "load_page": load_page,
        "analyze_headers": analyze_headers,
        "analyze_cookies": analyze_cookies,
        "analyze_csrf": analyze_csrf,
        "analyze_scripts": analyze_scripts,
        "detect_tech": detect_tech,
        "score_report": score_report,
        "summarize": summarize,
        "followup": followup,
        "reject": reject,
    }

    for name, function in node_functions.items():
        builder.add_node(name, function)

    # Start by interpreting the user's message.
    builder.add_edge(START, "intake")

    builder.add_conditional_edges(
        "intake",
        route_intake,
        ["scope_check", "followup"],
    )

    # Validate scope before opening the target website.
    builder.add_conditional_edges(
        "scope_check",
        route_scope,
        ["load_page", "reject"],
    )

    # After loading, run the analyzers or reject a failed scan.
    builder.add_conditional_edges(
        "load_page",
        route_after_load,
        ANALYZERS + ["reject"],
    )

    # Wait for every analyzer before scoring the combined findings.
    builder.add_edge(ANALYZERS, "score_report")
    builder.add_edge("score_report", "summarize")

    # Terminal paths.
    builder.add_edge("summarize", END)
    builder.add_edge("followup", END)
    builder.add_edge("reject", END)

    # Preserve conversation state across turns.
    memory = MemorySaver()
    return builder.compile(checkpointer=memory)


# Shared compiled graph for the application.
graph = build_graph()
