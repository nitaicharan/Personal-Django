from pydantic import BaseModel
from .user import UserShema


class ArticleShema(BaseModel):
    slug = str
    title = str
    description = str
    body = str
    tagList = str
    createdAt = str
    updatedAt = str
    favorited = str
    favoritesCount = str
    author: list[UserShema]

    class Config:
        orm_mode = True
