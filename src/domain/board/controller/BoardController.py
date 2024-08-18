from typing import List

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from src.domain.board.dto.req.BoardReqDto import BoardReqDto
from src.domain.board.dto.res.BoardResDto import BoardResDto
from src.domain.board.service.BoardService import BoardService

BoardRouter = APIRouter(prefix="/board", tags=["board"])


@BoardRouter.get("/", response_model=List[BoardResDto])
def get_board_list(boardService=Depends(BoardService)):
    return boardService.get_board_list()


@BoardRouter.post("/", response_model=BoardResDto, status_code=201)
def post_board(
        boardReqDto: BoardReqDto,
        boardService=Depends(BoardService)):
    return boardService.upload_board(boardReqDto)


@BoardRouter.put("/{id}", response_model=BoardResDto)
def update_board(
        id: int,
        boardReqDto: BoardReqDto,
        boardService=Depends(BoardService)):
    return boardService.update_board(id, boardReqDto)


@BoardRouter.delete("/{id}")
def delete_board(
        id: int,
        boardService=Depends(BoardService)):
    boardService.delete_board(id)
    return JSONResponse("", status_code=204)
