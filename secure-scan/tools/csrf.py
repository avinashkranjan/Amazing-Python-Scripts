
import re

from state import finding

TOKEN_RE = re.compile(
    r"csrf|xsrf|authenticity_token|_token|requestverificationtoken|nonce",
    re.IGNORECASE,
)


def analyze_csrf(state):
    page = state["page"]
    dom = page["dom"]
    findings = []
    https = page["final_url"].startswith("https://")

    meta_token = any(
        TOKEN_RE.search(meta["name"])
        for meta in dom["metas"]
        if meta["name"]
    )

    cookie_token = any(
        re.search(r"csrf|xsrf", cookie.get("name", ""), re.IGNORECASE)
        for cookie in page["cookies"]
    )

    cookies = page["cookies"]
    samesite_ok = bool(cookies) and all(
        cookie.get("sameSite") in ("Lax", "Strict")
        for cookie in cookies
    )

    form_report = []

    for index, form in enumerate(dom["forms"]):
        inputs = form["inputs"]
        names = [item["name"] for item in inputs if item["name"]]
        has_password = any(item["type"] == "password" for item in inputs)
        has_token = any(TOKEN_RE.search(name) for name in names)
        label = form.get("id") or f"form #{index + 1}"

        form_report.append({
            "form": label,
            "method": form["method"],
            "action": form["action"],
            "has_csrf_token": has_token,
            "has_password": has_password,
        })

        if form["method"] == "post" and not has_token and not meta_token:
            note = (
                " SameSite cookies reduce but don't replace CSRF tokens."
                if samesite_ok else ""
            )
            findings.append(finding(
                "csrf", "high" if has_password else "medium",
                f"POST {label} has no CSRF token",
                f"Inputs: {names[:8]}.{note}",
                "Add a per-session anti-CSRF token (hidden field or custom "
                "header) and validate it server-side.",
            ))

        if form["method"] == "get" and has_password:
            findings.append(finding(
                "forms", "high", f"{label} sends a password via GET",
                "Credentials end up in URLs, logs and history.",
                "Use POST.",
            ))

        if https and form["action"].startswith("http://"):
            findings.append(finding(
                "forms", "high",
                f"{label} submits to an insecure http:// action",
                form["action"], "Point the form action at HTTPS.",
            ))

        if has_password and not https:
            findings.append(finding(
                "forms", "high",
                f"Password field on {label} over plain HTTP",
                "", "Serve login pages over HTTPS only.",
            ))

    if dom["loose_password_inputs"] and not dom["forms"] and not https:
        findings.append(finding(
            "forms", "high",
            "Password input found on a plain-HTTP page",
            "", "Serve login pages over HTTPS only.",
        ))

    if not dom["forms"]:
        findings.append(finding(
            "csrf", "info",
            "No HTML forms on this page - CSRF check not applicable here",
            "SPA tokens: meta tag %s, cookie %s. Scan the login/checkout "
            "pages too."
            % (
                "found" if meta_token else "not found",
                "found" if cookie_token else "not found",
            ),
        ))

    return {
        "findings": findings,
        "csrf": {
            "forms": form_report,
            "meta_token": meta_token,
            "cookie_token": cookie_token,
        },
    }
