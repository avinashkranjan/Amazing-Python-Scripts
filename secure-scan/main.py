
"""Interactive CLI for SecureScan AI."""

import re

from config import PRINT_GRAPH, AUDIT_DIR
from audit import AuditRecorder
from graph import graph
from nodes.nodes import ANALYZERS


URL_PATTERN = re.compile(r"https?://[^\s<>\"']+", re.IGNORECASE)
LLM_NODES = {"summarize", "followup"}


def extract_url(query: str) -> str:
    """Extract the first HTTP(S) URL from a user query."""
    match = URL_PATTERN.search(query)
    if not match:
        return ""

    return match.group(0).rstrip(".,;:!?) ]}")


def extract_token_usage(update: dict) -> dict:
    """Extract token counts from an LLM node update when available."""
    messages = update.get("messages", [])

    if not messages:
        return {
            "input_tokens": None,
            "output_tokens": None,
            "total_tokens": None,
            "token_source": "unavailable",
        }

    message = messages[-1]

    # LangChain's normalized usage fields, when provided by the model.
    usage = getattr(message, "usage_metadata", None) or {}

    input_tokens = usage.get("input_tokens")
    output_tokens = usage.get("output_tokens")
    total_tokens = usage.get("total_tokens")

    # Ollama may expose counts in response_metadata instead.
    metadata = getattr(message, "response_metadata", None) or {}

    if input_tokens is None:
        input_tokens = metadata.get("prompt_eval_count")

    if output_tokens is None:
        output_tokens = metadata.get("eval_count")

    if total_tokens is None and input_tokens is not None and output_tokens is not None:
        total_tokens = input_tokens + output_tokens

    available = any(
        value is not None
        for value in (input_tokens, output_tokens, total_tokens)
    )

    return {
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "total_tokens": total_tokens,
        "token_source": "model_metadata" if available else "unavailable",
    }


def record_node_usage(
    audit: AuditRecorder,
    node_name: str,
    update: dict,
) -> None:
    """Record each executed graph node without inventing token counts."""
    if node_name in LLM_NODES:
        usage = extract_token_usage(update)
        audit.record_tool(node_name, **usage)
    else:
        # These nodes do not call an LLM directly.
        audit.record_tool(
            node_name,
            input_tokens=0,
            output_tokens=0,
            total_tokens=0,
            token_source="no_llm",
        )


def main() -> None:
    if PRINT_GRAPH:
        print(graph.get_graph().draw_mermaid())

    thread_config = {"configurable": {"thread_id": "secure-scan-cli"}}

    print(
        "\nSecureScan AI ready. Submit a URL, ask a follow-up, "
        "or type 'bye' to exit."
    )
    print("Only scan websites you own or are authorized to test.")

    while True:
        try:
            query = input("\nYou: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting SecureScan AI.")
            break

        if not query:
            continue

        if "bye" in query.lower():
            print(" Thank you for using SecureScan AI. Goodbye!")
            break

        audit = AuditRecorder(
            query=query,
            url=extract_url(query),
            audit_dir=AUDIT_DIR,
        )

        try:
            for event in graph.stream(
                {"messages": [("user", query)]},
                config=thread_config,
                stream_mode="updates",
            ):
                for node_name, update in event.items():
                    update = update or {}

                    record_node_usage(audit, node_name, update)

                    if node_name in {"intake", "scope_check", "load_page"}:
                        print(f"  [Running] {node_name}")

                    elif node_name in ANALYZERS:
                        print(f"  [Complete] {node_name}")

                    elif node_name in {"summarize", "followup", "reject"}:
                        messages = update.get("messages", [])
                        if messages:
                            print(f"\nSecureScan AI:\n{messages[-1].content}")

        except Exception as exc:
            print(f"\nAn error occurred while processing the request: {exc}")

        finally:
            try:
                audit_path = audit.save()
                print(f"\nAudit saved: {audit_path}")
            except OSError as exc:
                print(f"\nCould not save audit log: {exc}")

    print("Thank you for using SecureScan AI.")


if __name__ == "__main__":
    main()
