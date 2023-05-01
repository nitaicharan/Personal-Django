from app.src.adapters.spi.db.repositories.articles import Base


class AuthorEntity(Base):
    __tablename__ = "authors"
    # def __init__(self) -> None:
    #     self.username = str
    #     self.bio = str
    #     self.image = str
    #     self.following = bool
