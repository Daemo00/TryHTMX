"""Run the server."""

import fastapi_cli.cli
from .dependencies import static_path


def run(mode="dev"):
    """Run the FastAPI CLI."""
    match mode:
        case "dev":
            runner = fastapi_cli.cli.dev
        case _:
            runner = fastapi_cli.cli.run
    runner(
        static_path,
        host="0.0.0.0",  # nosec: B104:hardcoded_bind_all_interfaces
    )
