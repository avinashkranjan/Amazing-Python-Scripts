
from types import SimpleNamespace

from audit import AuditRecorder
from main import extract_url, extract_token_usage, record_node_usage


def test_extract_url_from_query():
    assert extract_url(
        "Please scan https://example.com and summarize the risks."
    ) == "https://example.com"


def test_extract_url_without_url():
    assert extract_url("Explain my previous report") == ""


def test_extract_token_usage_from_normalized_metadata():
    message = SimpleNamespace(
        usage_metadata={
            "input_tokens": 100,
            "output_tokens": 25,
            "total_tokens": 125,
        },
        response_metadata={},
    )

    usage = extract_token_usage({"messages": [message]})

    assert usage["input_tokens"] == 100
    assert usage["output_tokens"] == 25
    assert usage["total_tokens"] == 125
    assert usage["token_source"] == "model_metadata"


def test_unknown_llm_usage_stays_unknown():
    message = SimpleNamespace(
        usage_metadata={},
        response_metadata={},
    )

    usage = extract_token_usage({"messages": [message]})

    assert usage["total_tokens"] is None
    assert usage["token_source"] == "unavailable"


def test_non_llm_node_records_zero_tokens(tmp_path):
    audit = AuditRecorder(
        query="Scan https://example.com",
        url="https://example.com",
        audit_dir=tmp_path,
    )

    record_node_usage(audit, "analyze_headers", {})

    entry = audit.to_dict()["tools_used"][0]
    assert entry["tool"] == "analyze_headers"
    assert entry["total_tokens"] == 0
    assert entry["token_source"] == "no_llm"
