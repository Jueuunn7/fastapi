from typing import List

from fastapi import Depends

from src.domain.board.dto.req.BoardReqDto import BoardReqDto
from src.domain.board.dto.res.BoardResDto import BoardResDto
from src.domain.board.model.BoardModel import BoardModel
from src.domain.board.repo.BoardRepository import BoardRepository


class BoardService:

    def __init__(
            self,
            boardRepository: BoardRepository = Depends(),
    ) -> None:
        self.boardRepository = boardRepository

    def get_board_list(self) -> List[BoardResDto]:
        return [
            BoardResDto(
                id=b.id,
                title=b.title,
                content=b.content
            )
            for b in self.boardRepository.find_all()
        ]

    def upload_board(self, boardReqDto: BoardReqDto) -> BoardResDto:
        board: BoardModel = self.boardRepository.save(BoardModel(
            title=boardReqDto.title,
            content=boardReqDto.content
        ))

        return BoardResDto(
            id=board.id,
            title=board.title,
            content=board.content
        )

    def update_board(self, id: int, boardReqDto: BoardReqDto) -> BoardResDto:
        board: BoardModel = self.boardRepository.update(id, BoardModel(
            title=boardReqDto.title,
            content=boardReqDto.content
        ))
        return BoardResDto(
            id=board.id,
            title=board.title,
            content=board.content
        )

    def delete_board(self, id: int):
        self.boardRepository.delete(id)
