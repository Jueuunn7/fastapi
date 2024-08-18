from http.client import HTTPException
from xml.dom import NotFoundErr

from fastapi import Depends
from sqlalchemy.orm import Session

from database import get_db
from src.domain.board.model.BoardModel import BoardModel


class BoardRepository:
    db: Session

    def __init__(
            self,
            db: Session = Depends(get_db)
    ) -> None:
        self.db = db

    def find_all(self) -> list[BoardModel]:
        return self.db.query(BoardModel).all()

    def save(self, board: BoardModel) -> BoardModel:
        self.db.add(board)
        self.db.commit()
        self.db.refresh(board)
        return board

    def update(self, id: int, board: BoardModel) -> BoardModel:
        board.id = id
        self.db.merge(board)
        self.db.commit()
        return board

    def delete(self, id: int) -> None:
        board = self.db.query(BoardModel).filter_by(id=id).one_or_none()
        if board is None:
            raise NotFoundErr
        self.db.delete(board)
        self.db.commit()
