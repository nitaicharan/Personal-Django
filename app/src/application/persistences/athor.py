from abc import ABC, abstractmethod
from app.src.adapters.spi.db.models.author import AuthorModel


class AuthorPersistency(ABC):
    @abstractmethod
    async def find(self, id: int) -> AuthorModel:
        raise NotImplementedError
