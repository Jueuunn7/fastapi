from pydantic import BaseModel


class BoardResDto(BaseModel):
    id: int
    title: str
    content: str
