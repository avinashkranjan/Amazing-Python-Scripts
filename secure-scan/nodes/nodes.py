
"""LangGraph workflow nodes for SecureScan AI."""
import ipaddress
import socket
from urllib.parse import urlparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

from langchain_core.messages import AIMessage, SystemMessage
from langchain_ollama import ChatOllama

# from audit import AuditRecorder  # Reserved for later audit integration.
from config import (
    ALLOWED_DOMAINS,
    OLLAMA_MODEL,
    OLLAMA_TEMPERATURE,
    REPORT_DIR,
    SEVERITY_ORDER,
    SEVERITY_WEIGHT,
)
from state import ScanState
from tools.browser import collect_page


LLM = ChatOllama(model=OLLAMA_MODEL, temperature=OLLAMA_TEMPERATURE)

ANALYZERS = [
    "analyze_headers",
    "analyze_cookies",
    "analyze_csrf",
    "analyze_scripts",
    "detect_tech",
]

ICON = {
    "critical": "🛑",
    "high": "🔴",
    "medium": "🟠",
    "low": "🟡",
    "info": "🔵",
}


def intake(state: ScanState) -> dict:
    """Extract a URL from the latest user message without using an LLM."""
    if not state.get("messages"):
        return {"url": ""}

    message = state["messages"][-1].content
    match = re.search(r"https?://[^\s]+", message) or re.search(
        r"\b(?:[a-z0-9-]+\.)+[a-z]{2,}(?:/[^\s]*)?",
        message,
        re.IGNORECASE,
    )

    if not match:
        return {"url": ""}

    url = match.group(0).rstrip(".,;)")
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    return {
        "url": url,
        "error": "",
        "findings": [{"reset": True}],
    }


def route_intake(state: ScanState) -> str:
    return "scope_check" if state.get("url") else "followup"



def scope_check(state: ScanState) -> dict:
    """Validate a target URL before allowing the browser to open it."""
    url = state.get("url", "").strip()

    if not url:
        return {"error": "No URL provided."}

    try:
        parsed = urlparse(url)

        if parsed.scheme not in {"http", "https"}:
            return {"error": "Only HTTP and HTTPS URLs are supported."}

        if not parsed.hostname:
            return {"error": "The URL must contain a valid hostname."}

        if parsed.username or parsed.password:
            return {"error": "URLs containing embedded credentials are not allowed."}

        hostname = parsed.hostname.rstrip(".").lower()

        # Restrict scanning to standard web ports for this initial version.
        try:
            port = parsed.port
        except ValueError:
            return {"error": "The URL contains an invalid port."}

        allowed_port = port is None or port in {80, 443}
        if not allowed_port:
            return {"error": "Only standard web ports 80 and 443 are allowed."}

        # Reject localhost names and local-only hostnames.
        if hostname == "localhost" or hostname.endswith(".localhost"):
            return {"error": "Localhost targets are not allowed."}

        if not hostname or hostname.endswith(".local"):
            return {"error": "Local network hostnames are not allowed."}

        # Resolve the hostname and reject private or non-public addresses.
        try:
            addresses = socket.getaddrinfo(
                hostname,
                port or (443 if parsed.scheme == "https" else 80),
                type=socket.SOCK_STREAM,
            )
        except socket.gaierror:
            return {"error": "The hostname could not be resolved."}

        if not addresses:
            return {"error": "The hostname has no resolved addresses."}

        for address in addresses:
            ip_text = address[4][0].split("%")[0]
            ip = ipaddress.ip_address(ip_text)

            if not ip.is_global:
                return {
                    "error": (
                        "The target resolves to a non-public IP address. "
                        "Scanning this destination is blocked."
                    )
                }

        return {"error": ""}

    except (ValueError, TypeError):
        return {"error": "The URL is invalid."}


def route_scope(state: ScanState) -> str:
    return "reject" if state.get("error") else "load_page"


def load_page(state: ScanState) -> dict:
    """Collect browser data after scope_check has authorized the URL."""
    # collect_page owns the Selenium lifecycle and closes the browser.
    return collect_page(state["url"])


def route_after_load(state: ScanState) -> list[str]:
    """Fan out to independent analyzers, or reject if page collection failed."""
    return ["reject"] if state.get("error") else ANALYZERS


def score_report(state: ScanState) -> dict:
    """Aggregate analyzer results, calculate a score, and save the report."""
    page = state["page"]

    findings = sorted(
        state.get("findings", []),
        key=lambda item: SEVERITY_ORDER.index(item["severity"]),
    )

    counts = {
        severity: sum(
            1 for item in findings if item["severity"] == severity
        )
        for severity in SEVERITY_ORDER
    }

    score = max(
        0,
        100 - sum(SEVERITY_WEIGHT[item["severity"]] for item in findings),
    )
    grade = (
        "A" if score >= 90
        else "B" if score >= 75
        else "C" if score >= 60
        else "D" if score >= 40
        else "F"
    )

    report = {
        "scanned_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "url": state["url"],
        "final_url": page["final_url"],
        "title": page["dom"]["title"],
        "status_code": page["status"],
        "https": page["final_url"].startswith("https://"),
        "http_protocol": page["protocol"],
        "tls": {
            key: page["security_details"].get(key)
            for key in ("protocol", "issuer", "subjectName")
        },
        "redirects": page["redirects"],
        "load_time_sec": page["load_time"],
        "technologies": state.get("tech", []),
        "cookies": [
            {
                "name": cookie["name"],
                "secure": cookie.get("secure"),
                "httpOnly": cookie.get("httpOnly"),
                "sameSite": cookie.get("sameSite"),
            }
            for cookie in page["cookies"]
        ],
        "csrf": state.get("csrf", {}),
        "score": score,
        "grade": grade,
        "counts": counts,
        "findings": findings,
    }

    report_dir = Path(REPORT_DIR)
    report_dir.mkdir(parents=True, exist_ok=True)

    hostname = urlparse(state["url"]).hostname or "unknown-host"
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_path = report_dir / f"{hostname}_{timestamp}.json"

    with report_path.open("w", encoding="utf-8") as file:
        json.dump(report, file, indent=2, ensure_ascii=False)

    report["saved_to"] = str(report_path)

    print(render_report(report))
    return {"report": report}


def render_report(report: dict) -> str:
    """Format a report for terminal output."""
    line = "=" * 60
    counts = "  ".join(
        f"{ICON[severity]}{number}"
        for severity, number in report["counts"].items()
        if number
    )

    output = [
        f"\n{line}",
        "              WEBSITE SECURITY REPORT",
        line,
        f"URL          : {report['final_url']} (title: {report['title'] or 'n/a'})",
        f"Status/HTTPS : {report['status_code']} / "
        f"{'✅' if report['https'] else '❌'}",
        f"Protocol     : {report['http_protocol']} "
        f"TLS: {report['tls'].get('protocol')}",
        f"Redirects    : {report['redirects']} "
        f"Load time: {report['load_time_sec']}s",
        f"Tech stack   : {', '.join(report['technologies']) or 'nothing detected'}",
        f"Cookies      : {len(report['cookies'])} "
        f"Forms: {len(report['csrf'].get('forms', []))}",
        f"SCORE        : {report['score']}/100 (grade {report['grade']}) {counts}",
        "-" * 60,
        "FINDINGS",
        "-" * 60,
    ]

    for finding in report["findings"]:
        severity = finding["severity"]
        output.append(
            f"{ICON[severity]} [{severity.upper()}] {finding['title']}"
        )
        if finding.get("detail"):
            output.append(f"     ↳ {finding['detail'][:160]}")
        if finding.get("fix"):
            output.append(f"     ✔ Fix: {finding['fix']}")

    output.extend([
        line,
        f"JSON saved to {report['saved_to']}" if report.get("saved_to") else "",
        line,
    ])

    return "\n".join(output)


def clean(text: str) -> str:
    """Remove Qwen reasoning tags from text when present."""
    return re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL).strip()


def summarize(state: ScanState) -> dict:
    """Generate a short natural-language summary from the structured report."""
    report = state["report"]
    compact_findings = [
        f"[{item['severity']}] {item['title']} -> {item['fix']}"
        for item in report["findings"][:25]
    ]

    prompt = (
        "You are a web security analyst. Using ONLY the data below, write a "
        "short summary: overall posture, the top 3 priorities to fix first, "
        "and one sentence on what this scan cannot detect "
        "(it is a passive scan, no SQLi/XSS exploitation).\n\n"
        f"Score: {report['score']}/100 grade {report['grade']}\n"
        f"Tech: {report['technologies']}\n"
        f"CSRF: {json.dumps(report['csrf'])[:600]}\n"
        "Findings:\n" + "\n".join(compact_findings)
    )

    reply = clean(LLM.invoke(prompt).content)
    return {"messages": [AIMessage(content=reply)]}


def followup(state: ScanState) -> dict:
    """Answer questions about the latest report, or explain how to start."""
    report = state.get("report")

    if not report:
        return {
            "messages": [
                AIMessage(
                    content="Send me a URL to scan, e.g. https://your-site.com"
                )
            ]
        }

    system = SystemMessage(
        content=(
            "You are a web security analyst. Answer using this scan report:\n"
            + json.dumps(report)[:6000]
        )
    )
    reply = clean(LLM.invoke([system] + state["messages"]).content)
    return {"messages": [AIMessage(content=reply)]}


def reject(state: ScanState) -> dict:
    return {
        "messages": [
            AIMessage(content=f"⚠️ {state.get('error', 'Scan rejected.')}")
        ]
    }
