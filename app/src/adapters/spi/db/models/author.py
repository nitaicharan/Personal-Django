from datetime import datetime
from pydantic import Field
from sqlmodel import SQLModel


class AuthorModel(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    email: str
    username: str
    token: str | None
    bio: str | None
    image: str | None
    password: str | None
    createdAt: datetime | None
    updatedAt: datetime | None
    # articles: List[ArticleModel]

    class Config:
        orm_mode = True
