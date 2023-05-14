# from app.src.entities.article import ArticleEntity


class AuthorEntity:
    id: int
    email: str
    username: str
    password: str
    token: str | None = None
    bio: str | None = None
    image: str | None = None
    following: bool = False
    # articles: list[ArticleEntity] | None = []
