
from tools.headers import analyze_headers
from tools.cookies import analyze_cookies
from tools.csrf import analyze_csrf
from tools.scripts import analyze_scripts
from tools.technologies import detect_tech


def sample_state():
    return {
        "url": "https://example.com",
        "page": {
            "final_url": "https://example.com",
            "headers": {},
            "cookies": [],
            "dom": {
                "title": "Example",
                "forms": [],
                "loose_password_inputs": 0,
                "metas": [],
                "scripts": [],
                "jquery": None,
                "globals": {
                    "next": False,
                    "react": False,
                    "vue": False,
                    "angular": False,
                },
            },
            "requests_seen": [],
            "console_issues": [],
            "security_details": {},
            "hints": {
                "next": False,
                "wordpress": False,
                "php": False,
            },
            "probes": [],
        },
    }


def test_headers_report_missing_security_headers():
    result = analyze_headers(sample_state())
    titles = [item["title"] for item in result["findings"]]

    assert "Missing Content-Security-Policy" in titles
    assert "Missing Strict-Transport-Security (HSTS)" in titles


def test_cookies_report_when_none_are_set():
    result = analyze_cookies(sample_state())

    assert result["findings"][0]["check"] == "cookies"
    assert result["findings"][0]["severity"] == "info"


def test_csrf_reports_no_forms():
    result = analyze_csrf(sample_state())

    assert result["csrf"]["forms"] == []
    assert any(
        "No HTML forms" in item["title"]
        for item in result["findings"]
    )


def test_scripts_returns_empty_findings_for_clean_sample():
    result = analyze_scripts(sample_state())

    assert result == {"findings": []}


def test_technology_detection_returns_empty_results():
    result = detect_tech(sample_state())

    assert result == {"tech": [], "findings": []}
