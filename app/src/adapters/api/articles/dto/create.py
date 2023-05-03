from pydantic import BaseModel

from app.src.entities.article import ArticleEntity


class CreateArticleDto(BaseModel):
    title: str
    slug: str
    description: str
    body: str
    tagList: list[str] = []
    favorited: bool = False
    favorites_count: int = 0
    # author: Auth

    def to_entity(self):
        entity = ArticleEntity()
        entity.title = self.title
        entity.slug = self.slug
        entity.description = self.description
        entity.body = self.body
        entity.favorited = self.favorited
        entity.favorites_count = self.favorites_count
        entity.tagList = self.tagList
        return entity
