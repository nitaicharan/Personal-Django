from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.orm import relationship
from app.src.adapters.spi.db.repositories.schema import Base

class AuthorTable(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    token= Column(String, unique=True, index=True)
    username= Column(String, unique=True, index=True)
    bio= Column(String)
    image= Column(String)
    password= Column(String)
    createdAt= Column(Date)
    updatedAt= Column(Date)
    # articles = relationship("ArticleTable", back_populates="author")

    class Config:
        orm_mode = True

