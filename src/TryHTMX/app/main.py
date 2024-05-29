"""Build the server."""
import os
from pathlib import Path

from fastapi import FastAPI

app_path = Path(os.path.dirname(__file__))

app = FastAPI()
