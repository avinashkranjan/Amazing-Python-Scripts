
from graph import build_graph
from nodes.nodes import ANALYZERS


def test_graph_compiles_with_expected_nodes():
    app = build_graph()
    node_names = set(app.get_graph().nodes)

    expected = {
        "__start__",
        "__end__",
        "intake",
        "scope_check",
        "load_page",
        "score_report",
        "summarize",
        "followup",
        "reject",
        *ANALYZERS,
    }

    assert expected.issubset(node_names)


def test_graph_has_expected_workflow_edges():
    app = build_graph()
    edges = {
        (edge.source, edge.target)
        for edge in app.get_graph().edges
    }

    expected_edges = {
        ("__start__", "intake"),
        ("score_report", "summarize"),
        ("summarize", "__end__"),
        ("followup", "__end__"),
        ("reject", "__end__"),
    }

    assert expected_edges.issubset(edges)


def test_analyzers_fan_in_to_score_report():
    app = build_graph()
    edges = {
        (edge.source, edge.target)
        for edge in app.get_graph().edges
    }

    for analyzer in ANALYZERS:
        assert (analyzer, "score_report") in edges
