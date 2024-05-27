"""Build the server."""
from pathlib import Path

import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import os

package_path = Path(os.path.dirname(__file__))

app = FastAPI()


@app.post("/clicked")
async def clicked():
    """Response to button click."""
    return "Clicked"


# Mount after other paths so it does not overwrite it
app.mount(
    "/",
    StaticFiles(directory=package_path / "static", html=True),
    name="static",
)


def run():
    """Run the application."""
    uvicorn.run(app)
