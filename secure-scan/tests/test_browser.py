
import json

from tools.browser import make_driver, parse_perf_logs


def make_log(method, params):
    """Build a Chrome performance-log entry for a test."""
    return {
        "message": json.dumps({
            "message": {
                "method": method,
                "params": params,
            }
        })
    }


def test_parse_perf_logs_extracts_document_response():
    entries = [
        make_log(
            "Network.responseReceived",
            {
                "type": "Document",
                "response": {
                    "status": 200,
                    "headers": {"Content-Type": "text/html"},
                    "protocol": "h2",
                },
            },
        )
    ]

    main, requests, redirects = parse_perf_logs(entries)

    assert main["status"] == 200
    assert main["protocol"] == "h2"
    assert requests == []
    assert redirects == 0


def test_parse_perf_logs_tracks_requests_and_redirects():
    entries = [
        make_log(
            "Network.requestWillBeSent",
            {
                "type": "Document",
                "request": {"url": "https://example.com/"},
            },
        ),
        make_log(
            "Network.requestWillBeSent",
            {
                "type": "Document",
                "request": {"url": "https://example.com/home"},
                "redirectResponse": {"status": 301},
            },
        ),
        make_log(
            "Network.requestWillBeSent",
            {
                "type": "Script",
                "request": {"url": "https://example.com/app.js"},
            },
        ),
    ]

    main, requests, redirects = parse_perf_logs(entries)

    assert main == {}
    assert requests == [
        "https://example.com/",
        "https://example.com/app.js",
        "https://example.com/home",
    ]
    assert redirects == 1


def test_parse_perf_logs_ignores_malformed_entries():
    entries = [
        {},
        {"message": "not-json"},
        make_log(
            "Network.responseReceived",
            {
                "type": "Document",
                "response": {"status": 204},
            },
        ),
    ]

    main, requests, redirects = parse_perf_logs(entries)

    assert main["status"] == 204
    assert requests == []
    assert redirects == 0


def test_make_driver_uses_headless_chrome(monkeypatch):
    captured = {}

    class FakeChrome:
        def __init__(self, options):
            captured["options"] = options

    monkeypatch.setattr(
        "tools.browser.webdriver.Chrome",
        FakeChrome,
    )

    driver = make_driver()
    options = captured["options"]

    assert driver is not None
    assert "--headless=new" in options.arguments
    assert "--window-size=1366,900" in options.arguments
    assert "--disable-gpu" in options.arguments

    capabilities = options.to_capabilities()
    assert capabilities["goog:loggingPrefs"] == {
        "performance": "ALL",
        "browser": "ALL",
    }
