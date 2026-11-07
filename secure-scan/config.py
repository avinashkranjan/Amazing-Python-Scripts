
"""Central configuration for SecureScan AI."""

import re

# Only scan domains you own or have explicit permission to test.
ALLOWED_DOMAINS = {"rag-based-pdf-chatbot.netlify.app"}

# Preserve the existing scan behavior for this refactor.
ACTIVE_PROBES = True

SENSITIVE_PATHS = {
    "/.env": r"^[A-Z0-9_]+\s*=",
    "/.git/HEAD": r"^ref:\s*refs/",
    "/.git/config": r"\[core\]",
    "/phpinfo.php": r"phpinfo\(\)|PHP Version",
    "/server-status": r"Apache Server Status",
    "/.DS_Store": r"Bud1",
    "/backup.zip": r"^PK",
}

PRINT_GRAPH = False
REPORT_DIR = "reports"
AUDIT_DIR = "reports/audit"

# Model configuration. The model will be initialized in a later step.
OLLAMA_MODEL = "qwen3:1.7b"
OLLAMA_TEMPERATURE = 0

SEVERITY_WEIGHT = {
    "critical": 30,
    "high": 20,
    "medium": 10,
    "low": 4,
    "info": 0,
}

SEVERITY_ORDER = ["critical", "high", "medium", "low", "info"]

TOKEN_RE = re.compile(
    r"csrf|xsrf|authenticity_token|_token|requestverificationtoken|nonce",
    re.IGNORECASE,
)

SESSION_RE = re.compile(
    r"sess|sid|auth|token|jwt|login",
    re.IGNORECASE,
)
