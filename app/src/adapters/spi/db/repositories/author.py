from sqlmodel import Session
from app.src.adapters.spi.db.models.author import AuthorModel
from app.src.application.persistences.athor import AuthorPersistency
from .schema import engine


class AuthorRepository(AuthorPersistency):
    async def find(self, id: int):
        with Session(engine) as session:
            model = session.get(AuthorModel, id)
            session.close()
            return model
