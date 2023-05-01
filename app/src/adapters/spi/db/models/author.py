from sqlalchemy import Column, Date, Integer, String, table
from sqlmodel import Field, SQLModel


class AuthorModel(SQLModel, table=True):
    id: int= Field(primary_key=True)
    # email = Column(String, unique=True, index=True)
    # token = Column(String, unique=True, index=True)
    # username = Column(String, unique=True, index=True)
    # bio = Column(String)
    # image = Column(String)
    # password = Column(String)
    # createdAt = Column(Date)
    # updatedAt = Column(Date)
    # articles = relationship("ArticleTable", back_populates="author")

    class Config:
        orm_mode = True
