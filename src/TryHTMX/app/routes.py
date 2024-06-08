"""Routes for FastAPI app."""
from fastapi.responses import FileResponse
from fastapi import APIRouter

from .dependencies import static_path

router = APIRouter()


@router.get("/")
async def root():
    """Root."""
    return FileResponse(static_path / "static" / "index.html")


@router.post("/clicked")
async def clicked():
    """Response to button click."""
    return "Clicked"


@router.post("/mouse_entered")
async def mouse_entered():
    """Response to mouse entered."""
    return "Mouse entered"


@router.get("/trigger_delay")
async def trigger_delay(q=None):
    """Response to search query."""
    return f"After delayed trigger with {q}"
