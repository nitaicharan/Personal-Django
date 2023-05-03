from datetime import datetime
from app.src.entities.author import AuthorEntity


class ArticleEntity:
    slug: str
    title: str
    description: str
    body: str
    tagList: list[str] = []
    created_at: datetime | None
    updated_at: datetime | None
    favorited: bool = False
    favorites_count: int = 0
    author: AuthorEntity
