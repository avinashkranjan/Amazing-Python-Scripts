
import re
import time
from urllib.parse import urlparse

from config import SENSITIVE_PATHS
from state import finding


def analyze_scripts(state):
    page = state["page"]
    dom = page["dom"]
    findings = []
    https = page["final_url"].startswith("https://")
    host = urlparse(page["final_url"]).hostname

    third_party = [
        script["src"]
        for script in dom["scripts"]
        if (
            script["src"]
            and urlparse(script["src"]).hostname not in (host, None)
            and not script["integrity"]
        )
    ]

    if third_party:
        findings.append(finding(
            "supply-chain", "low",
            f"{len(third_party)} third-party script(s) without Subresource Integrity",
            ", ".join(third_party[:4]),
            "Add integrity= and crossorigin= attributes, or self-host.",
        ))

    if https:
        mixed = [
            url for url in page["requests_seen"]
            if url.startswith("http://")
        ]
        if mixed:
            findings.append(finding(
                "mixed-content", "medium",
                f"{len(mixed)} insecure http:// resource request(s) on an HTTPS page",
                ", ".join(mixed[:3]),
                "Load every resource over HTTPS.",
            ))

    jquery = dom.get("jquery")
    if jquery:
        try:
            version = tuple(int(part) for part in jquery.split(".")[:3])
        except ValueError:
            version = (99,)

        if version < (3, 5, 0):
            findings.append(finding(
                "outdated-lib", "medium",
                f"Outdated jQuery {jquery} (known XSS issues before 3.5.0)",
                "", "Upgrade jQuery to the latest 3.x.",
            ))

    for probe in page["probes"]:
        path = probe["path"]
        pattern = SENSITIVE_PATHS.get(path)

        if (
            pattern
            and probe["status"] == 200
            and re.search(pattern, probe["snippet"], re.MULTILINE)
        ):
            findings.append(finding(
                "exposure", "critical",
                f"Sensitive file exposed: {path}",
                "",
                "Remove it from the web root and rotate any secrets inside.",
            ))

    if page["console_issues"]:
        findings.append(finding(
            "console", "info",
            f"{len(page['console_issues'])} browser console warning(s)/error(s)",
            page["console_issues"][0][:150],
        ))

    # Certificate details are collected by Chrome, not inferred from the URL.
    security = page["security_details"]
    if https and security:
        days = (
            int((security["validTo"] - time.time()) // 86400)
            if security.get("validTo") else None
        )

        if days is not None and days < 0:
            findings.append(finding(
                "tls", "high", "TLS certificate has expired",
                "", "Renew the certificate.",
            ))
        elif days is not None and days < 15:
            findings.append(finding(
                "tls", "medium",
                f"TLS certificate expires in {days} days",
                "", "Renew soon / automate renewal.",
            ))

        protocol = security.get("protocol")
        if protocol in ("TLS 1.0", "TLS 1.1"):
            findings.append(finding(
                "tls", "high",
                f"Legacy protocol negotiated: {protocol}",
                "", "Require TLS 1.2+.",
            ))

    return {"findings": findings}
