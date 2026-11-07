
"""JSON audit logging for SecureScan AI."""

import json
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class AuditRecorder:
    """Collect a query, its URL, tool calls, and measurable token usage."""

    def __init__(
        self,
        query: str,
        url: str,
        audit_dir: str | Path = "reports/audit",
    ) -> None:
        self.query = query
        self.url = url
        self.audit_dir = Path(audit_dir)
        self.created_at = datetime.now(timezone.utc).isoformat()
        self.audit_id = uuid.uuid4().hex
        self.tools_used: list[dict[str, Any]] = []

    def record_tool(
        self,
        tool_name: str,
        *,
        input_tokens: int | None = None,
        output_tokens: int | None = None,
        total_tokens: int | None = None,
        token_source: str = "unavailable",
    ) -> None:
        """Record one tool call without guessing missing token counts."""

        if total_tokens is None:
            if input_tokens is not None and output_tokens is not None:
                total_tokens = input_tokens + output_tokens

        self.tools_used.append(
            {
                "tool": tool_name,
                "input_tokens": input_tokens,
                "output_tokens": output_tokens,
                "total_tokens": total_tokens,
                "token_source": token_source,
            }
        )

    def to_dict(self) -> dict[str, Any]:
        """Return the audit record in a JSON-serializable format."""

        usage_complete = all(
            entry["total_tokens"] is not None
            for entry in self.tools_used
        )

        total_tokens = (
            sum(entry["total_tokens"] for entry in self.tools_used)
            if usage_complete
            else None
        )

        return {
            "audit_id": self.audit_id,
            "created_at": self.created_at,
            "query": self.query,
            "url": self.url,
            "tools_used": self.tools_used,
            "total_tokens": total_tokens,
            "token_usage_complete": usage_complete,
        }

    def save(self) -> Path:
        """Write this audit record to a unique JSON file."""

        self.audit_dir.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now(timezone.utc).strftime(
            "%Y%m%dT%H%M%S%fZ"
        )
        output_path = self.audit_dir / (
            f"scan_{timestamp}_{self.audit_id[:8]}.json"
        )

        with output_path.open("w", encoding="utf-8") as file:
            json.dump(self.to_dict(), file, indent=2, ensure_ascii=False)

        return output_path
