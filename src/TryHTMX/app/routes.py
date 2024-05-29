"""Routes for FastAPI app."""
from .main import app, app_path
from fastapi.responses import FileResponse


@app.get("/")
async def root():
    """Root."""
    return FileResponse(app_path / "static" / "index.html")


@app.post("/clicked")
async def clicked():
    """Response to button click."""
    return "Clicked"
