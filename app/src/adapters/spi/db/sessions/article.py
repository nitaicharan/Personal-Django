from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .session import Base


class Article(Base):
    tablename__ = "articles"
    slug = Column(String)
    title = Column(String)
    description = Column(String)
    body = Column(String)
    tags = relationship([str])
    createdAt = Column(String)
    updatedAt = Column(String)
    favoritesCount = Column(Integer)

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    username = Column(String, unique=True)
    password = Column(String)
    bio = Column(String)
    image = Column(String)
    author = relationship("User")
