from datetime import datetime


class ArticleEntity:
    slug: str
    title: str
    description: str
    body: str
    tagList: list[str] = []
    created_at: datetime = None
    updated_at: datetime = None
    favorited: bool = False
    favorites_count: int = 0
    # author: Auth
