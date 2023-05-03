from sqlmodel import Field, SQLModel
from app.src.entities.article import ArticleEntity


class ArticleModel(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    slug: str
    title: str
    description: str
    body: str
    # tagList: list[str]
    created_at: str | None = None
    updated_at: str | None = None
    favorited: bool
    favorites_count: int
    author_id: int | None = Field(default=None, foreign_key="articlemodel.id")

    @staticmethod
    def from_entity(entity: ArticleEntity):
        model = ArticleModel(
            slug=entity.slug,
            title=entity.title,
            description=entity.description,
            body=entity.body,
            # tagList = entity.tagList,
            favorited=entity.favorited,
            favorites_count=entity.favorites_count,
        )
        return model

    class Config:
        orm_mode = True
