"""Build the server."""
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
import os

import fastapi_cli.cli

package_path = Path(os.path.dirname(__file__))

app = FastAPI()


@app.get("/")
async def root():
    """Root."""
    return FileResponse(package_path / "static" / "index.html")


@app.post("/clicked")
async def clicked():
    """Response to button click."""
    return "Clicked"


def run():
    """Run the FastAPI CLI."""
    fastapi_cli.cli.dev(package_path)
