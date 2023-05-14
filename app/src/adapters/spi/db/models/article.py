from datetime import datetime
from sqlmodel import Field, SQLModel
from app.src.entities.article import ArticleEntity


class ArticleModel(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    slug: str
    title: str
    description: str
    body: str
    # tagList: list[str]
    created_at: datetime | None = None
    updated_at: datetime | None = None
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

    def to_entity(self):
        entity = ArticleEntity()
        entity.id = self.id
        entity.slug = self.slug
        entity.description = self.description
        entity.body = self.body
        entity.created_at = self.created_at
        entity.updated_at = self.updated_at
        entity.favorited = self.favorited
        entity.favorites_count = self.favorites_count
        return entity

    class Config:
        orm_mode = True
