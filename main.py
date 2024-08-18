from pathlib import Path
from fastapi import FastAPI

from src.domain.board.controller.BoardController import BoardRouter

BASE_DIR = Path(__file__).resolve().parent.parent

app = FastAPI()

app.include_router(BoardRouter)
