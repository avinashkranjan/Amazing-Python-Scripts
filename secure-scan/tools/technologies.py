from state import finding

def detect_tech(state):
    page = state["page"]
    headers = page["headers"]
    hints = page["hints"]
    globals_found = page["dom"]["globals"]

    technologies = []
    findings = []

    if headers.get("server"):
        technologies.append(f"Server: {headers['server']}")

    if headers.get("x-powered-by"):
        technologies.append(f"Powered by: {headers['x-powered-by']}")

    for meta in page["dom"]["metas"]:
        if meta["name"].lower() == "generator" and meta["content"]:
            technologies.append(f"Generator: {meta['content']}")

    if "cf-ray" in headers:
        technologies.append("CDN: Cloudflare")

    if "x-vercel-id" in headers:
        technologies.append("Host: Vercel")

    if (
        "x-nf-request-id" in headers
        or "netlify" in headers.get("server", "").lower()
    ):
        technologies.append("Host: Netlify")

    for key, label in (
        ("next", "Next.js"),
        ("react", "React"),
        ("vue", "Vue"),
        ("angular", "Angular"),
    ):
        if globals_found.get(key) or hints.get(key):
            technologies.append(f"Framework: {label}")

    jquery = page["dom"].get("jquery")
    if jquery:
        technologies.append(f"Library: jQuery {jquery}")

    if hints["wordpress"]:
        technologies.append("CMS: WordPress")
        findings.append(finding(
            "tech", "info", "WordPress detected",
            "", "Keep core, themes and plugins updated.",
        ))

    if hints["php"]:
        technologies.append("Language: PHP")

    return {"tech": technologies, "findings": findings}
