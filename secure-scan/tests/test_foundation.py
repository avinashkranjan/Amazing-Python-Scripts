import json
from audit import AuditRecorder
from config import ACTIVE_PROBES, ALLOWED_DOMAINS, SEVERITY_WEIGHT
from state import finding, merge_findings


def test_existing_scan_scope_is_preserved():
    assert ALLOWED_DOMAINS == {
        "rag-based-pdf-chatbot.netlify.app"
    }
    assert ACTIVE_PROBES is True


def test_severity_weights_are_available():
    assert SEVERITY_WEIGHT["critical"] > SEVERITY_WEIGHT["high"]


def test_finding_has_expected_fields():
    result = finding(
        "headers",
        "medium",
        "Missing header",
        "The header was not found.",
        "Configure the header.",
    )

    assert result["check"] == "headers"
    assert result["severity"] == "medium"
    assert result["title"] == "Missing header"


def test_findings_are_appended():
    old = [{"title": "First"}]
    new = [{"title": "Second"}]

    assert merge_findings(old, new) == [
        {"title": "First"},
        {"title": "Second"},
    ]


def test_findings_can_be_reset():
    old = [{"title": "Old finding"}]
    new = [{"reset": True}, {"title": "New finding"}]

    assert merge_findings(old, new) == [
        {"title": "New finding"}
    ]


def test_audit_is_saved_as_json(tmp_path):
    recorder = AuditRecorder(
        query="Check security headers",
        url="https://example.com",
        audit_dir=tmp_path,
    )
    recorder.record_tool(
        "selenium_page_collection",
        input_tokens=0,
        output_tokens=0,
        total_tokens=0,
        token_source="not_applicable",
    )
    recorder.record_tool(
        "ollama_summary",
        input_tokens=20,
        output_tokens=10,
        token_source="model_response_usage",
    )

    output_path = recorder.save()

    assert output_path.exists()

    with output_path.open(encoding="utf-8") as file:
        data = json.load(file)

    assert data["query"] == "Check security headers"
    assert data["url"] == "https://example.com"
    assert len(data["tools_used"]) == 2
    assert data["total_tokens"] == 30
    assert data["token_usage_complete"] is True


def test_unknown_token_usage_is_not_invented(tmp_path):
    recorder = AuditRecorder(
        query="Inspect the target",
        url="https://example.com",
        audit_dir=tmp_path,
    )
    recorder.record_tool("unknown_usage_tool")

    data = recorder.to_dict()

    assert data["tools_used"][0]["total_tokens"] is None
    assert data["total_tokens"] is None
    assert data["token_usage_complete"] is False
