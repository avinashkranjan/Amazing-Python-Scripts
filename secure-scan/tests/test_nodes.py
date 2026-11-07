
import json
from langchain_core.messages import HumanMessage
import nodes.nodes as nodes



def test_intake_extracts_url_and_resets_findings():
    result = nodes.intake({
        "messages": [
            HumanMessage(content="Please scan https://example.com")
        ]
    })

    assert result["url"] == "https://example.com"
    assert result["error"] == ""
    assert result["findings"] == [{"reset": True}]


def test_intake_routes_messages_without_url_to_followup():
    result = nodes.intake({
        "messages": [
            HumanMessage(content="Explain my last report")
        ]
    })

    assert result["url"] == ""
    assert nodes.route_intake(result) == "followup"


def test_scope_check_rejects_out_of_scope_domain():
    result = nodes.scope_check({"url": "https://example.com"})

    assert result["error"]
    assert nodes.route_scope(result) == "reject"


def test_load_page_delegates_to_browser_collector(monkeypatch):
    expected = {"page": {"final_url": "https://example.com"}, "error": ""}
    called = {}

    def fake_collect_page(url):
        called["url"] = url
        return expected

    monkeypatch.setattr(nodes, "collect_page", fake_collect_page)

    result = nodes.load_page({"url": "https://example.com"})

    assert called["url"] == "https://example.com"
    assert result == expected


def test_score_report_saves_json_and_calculates_score(monkeypatch, tmp_path):
    monkeypatch.setattr(nodes, "REPORT_DIR", str(tmp_path))

    state = {
        "url": "https://rag-based-pdf-chatbot.netlify.app",
        "page": {
            "final_url": "https://rag-based-pdf-chatbot.netlify.app",
            "status": 200,
            "protocol": "h2",
            "security_details": {
                "protocol": "TLS 1.3",
                "issuer": "Test CA",
                "subjectName": "example.test",
            },
            "redirects": 1,
            "load_time": 1.25,
            "dom": {"title": "Test site"},
            "cookies": [],
        },
        "findings": [
            {
                "check": "headers",
                "severity": "medium",
                "title": "Missing CSP",
                "detail": "",
                "fix": "Add a CSP",
            }
        ],
        "tech": ["Framework: React"],
        "csrf": {"forms": []},
    }

    result = nodes.score_report(state)
    report = result["report"]

    assert report["score"] == 90
    assert report["grade"] == "A"
    assert report["counts"]["medium"] == 1
    assert report["saved_to"]

    with open(report["saved_to"], encoding="utf-8") as file:
        saved_report = json.load(file)

    assert saved_report["score"] == 90
    assert saved_report["findings"][0]["title"] == "Missing CSP"
    assert nodes.route_after_load({"error": ""}) == nodes.ANALYZERS
    assert nodes.route_after_load({"error": "load failed"}) == ["reject"]
