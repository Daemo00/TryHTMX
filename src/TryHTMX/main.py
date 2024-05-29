"""Run the server."""

import fastapi_cli.cli
from .app.main import app_path


def run(mode="dev"):
    """Run the FastAPI CLI."""
    match mode:
        case "dev":
            runner = fastapi_cli.cli.dev
        case _:
            runner = fastapi_cli.cli.run
    runner(app_path)
