
import re
from state import finding


def analyze_headers(state):
    page = state["page"]
    headers = page["headers"]
    findings = []
    https = page["final_url"].startswith("https://")
    csp = headers.get("content-security-policy", "")

    if not https:
        findings.append(finding(
            "transport", "high", "Site is served over plain HTTP",
            page["final_url"],
            "Serve everything over HTTPS and redirect HTTP to HTTPS.",
        ))

    if not csp:
        findings.append(finding(
            "headers", "medium", "Missing Content-Security-Policy",
            "No CSP means injected scripts run unrestricted (XSS impact is higher).",
            "Add a CSP, e.g. default-src 'self'; script-src 'self'.",
        ))
    elif "unsafe-inline" in csp or "unsafe-eval" in csp:
        findings.append(finding(
            "headers", "medium", "CSP allows 'unsafe-inline' / 'unsafe-eval'",
            csp[:200],
            "Use nonces or hashes instead of unsafe-inline/unsafe-eval.",
        ))

    if "x-frame-options" not in headers and "frame-ancestors" not in csp:
        findings.append(finding(
            "headers", "medium", "No clickjacking protection",
            "Neither X-Frame-Options nor CSP frame-ancestors is set.",
            "Add X-Frame-Options: DENY or CSP frame-ancestors 'none'.",
        ))

    if https and "strict-transport-security" not in headers:
        findings.append(finding(
            "headers", "medium", "Missing Strict-Transport-Security (HSTS)",
            "",
            "Add Strict-Transport-Security: max-age=31536000; includeSubDomains.",
        ))

    if headers.get("x-content-type-options", "").lower() != "nosniff":
        findings.append(finding(
            "headers", "low", "Missing X-Content-Type-Options: nosniff",
            "", "Add X-Content-Type-Options: nosniff.",
        ))

    if "referrer-policy" not in headers:
        findings.append(finding(
            "headers", "low", "Missing Referrer-Policy",
            "", "Add Referrer-Policy: strict-origin-when-cross-origin.",
        ))

    if "permissions-policy" not in headers:
        findings.append(finding(
            "headers", "low", "Missing Permissions-Policy",
            "", "Restrict browser features you don't use.",
        ))

    for name in ("server", "x-powered-by", "x-aspnet-version"):
        if name in headers and re.search(r"\d", headers[name]):
            findings.append(finding(
                "disclosure", "low",
                f"Version disclosed in '{name}' header",
                headers[name], "Remove or genericise version banners.",
            ))

    if headers.get("access-control-allow-origin") == "*":
        findings.append(finding(
            "cors", "low", "CORS allows any origin (*)",
            "Fine for public APIs, risky if responses contain private data.",
            "Restrict Access-Control-Allow-Origin to trusted origins.",
        ))

    return {"findings": findings}
