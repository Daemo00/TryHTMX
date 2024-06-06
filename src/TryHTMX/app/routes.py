"""Routes for FastAPI app."""
from fastapi.responses import FileResponse
from fastapi import APIRouter

from .dependencies import app_path

router = APIRouter()


@router.get("/")
async def root():
    """Root."""
    return FileResponse(app_path / "static" / "index.html")


@router.post("/clicked")
async def clicked():
    """Response to button click."""
    return "Clicked"
