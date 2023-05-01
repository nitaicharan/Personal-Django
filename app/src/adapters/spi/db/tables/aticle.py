from sqlalchemy import Boolean, Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.src.adapters.spi.db.repositories.schema import Base

class ArticleTable(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    slug = Column(String)
    title = Column(String)
    description = Column(String)
    body = Column(String)
    tagList = Column(String)
    createdAt = Column(Date)
    updatedAt = Column(Date)
    favorited = Column(Boolean)
    favoritesCount = Column(Integer)
    # author_id = Column(Integer,ForeignKey("authors.id"))
    # author = relationship("AuthorTable", back_populates="authors")

    class Config:
        orm_mode = True
