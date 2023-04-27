from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .session import Base


class User(Base):
    tablename__ = "articles"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    username = Column(String, unique=True)
    password = Column(String)
    bio = Column(String)
    image = Column(String)
    author = relationship("Article")
