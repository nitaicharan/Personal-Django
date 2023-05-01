from datetime import datetime
from httpx import Auth


class ArticleEntity:
    def __init__(self) -> None:
        self.slug: str
        self.title: str
        self.description: str
        self.body: str
        self.tagList: list[str]
        self.createdAt: datetime
        self.updatedAt: datetime
        self.favorited: bool
        self.favoritesCount: int
        self.author: Auth
