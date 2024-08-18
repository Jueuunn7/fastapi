from pydantic import BaseModel


class BoardReqDto(BaseModel):
    title: str
    content: str
