from sqlmodel import Field, SQLModel


class ArticleModel(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    # slug = Column(String)
    title: str
    # description = Column(String)
    # body = Column(String)
    # tagList = Column(String)
    # createdAt = Column(Date)
    # updatedAt = Column(Date)
    # favorited = Column(Boolean)
    # favoritesCount = Column(Integer)
    # # author_id = Column(Integer,ForeignKey("authors.id"))
    # # author = relationship("AuthorTable", back_populates="authors")

    class Config:
        orm_mode = True
