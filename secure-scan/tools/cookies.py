
import re

from state import finding

SESSION_RE = re.compile(r"sess|sid|auth|token|jwt|login", re.IGNORECASE)


def analyze_cookies(state):
    page = state["page"]
    findings = []
    https = page["final_url"].startswith("https://")
    cookies = page["cookies"]

    if not cookies:
        return {
            "findings": [
                finding("cookies", "info", "No cookies set on first load")
            ]
        }

    for cookie in cookies:
        name = cookie.get("name", "?")
        session_like = bool(SESSION_RE.search(name))

        if https and not cookie.get("secure"):
            findings.append(finding(
                "cookies", "medium",
                f"Cookie '{name}' lacks the Secure flag",
                "", "Set the Secure attribute.",
            ))

        if not cookie.get("httpOnly"):
            findings.append(finding(
                "cookies", "medium" if session_like else "low",
                f"Cookie '{name}' lacks HttpOnly",
                "Readable by JavaScript (XSS theft risk).",
                "Set HttpOnly on session/auth cookies.",
            ))

        if cookie.get("sameSite") in (None, "None"):
            findings.append(finding(
                "cookies", "low",
                f"Cookie '{name}' has no SameSite protection",
                "", "Set SameSite=Lax or Strict.",
            ))

    return {"findings": findings}
