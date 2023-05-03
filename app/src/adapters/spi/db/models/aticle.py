from sqlmodel import Field, SQLModel

from app.src.entities.article import ArticleEntity


class ArticleModel(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    slug: str
    title: str
    description: str
    body: str
    # tagList: list[str]
    created_at: str | None
    updated_at: str | None
    favorited: bool
    favorites_count: int
    # self.author_id = Column(Integer,ForeignKey("authors.id"))
    # self.author = relationship("AuthorTable", back_populates="authors")

    @staticmethod
    def from_entity(entity: ArticleEntity):
        model = ArticleModel()
        model.slug = entity.slug
        model.title = entity.title
        model.description = entity.description
        model.body = entity.body
        # model.tagList = entity.tagList
        model.favorited = entity.favorited
        model.favorites_count = entity.favorites_count
        return model

    class Config:
        orm_mode = True
