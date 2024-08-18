from database import Base

from sqlalchemy import (Column, Integer, String)


class BoardModel(Base):
    __tablename__ = 'board'

    id = Column(Integer, primary_key=True, autoincrement=True)

    title = Column(String)

    content = Column(String)
