from datetime import datetime
from pydantic import Field
from sqlmodel import SQLModel

from app.src.entities.author import AuthorEntity


class AuthorModel(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    email: str
    username: str
    token: str | None = None
    bio: str | None = None
    image: str | None = None
    password: str | None = None
    createdAt: datetime | None = None
    updatedAt: datetime | None = None
    # articles: List[ArticleModel]

    @staticmethod
    def from_entity(entity: AuthorEntity):
        model = AuthorModel(
            id=entity.id,
            email=entity.email,
            username=entity.username,
            bio=entity.bio,
            image=entity.image,
            password=entity.password,
            token=entity.token,
        )
        return model

    class Config:
        orm_mode = True
