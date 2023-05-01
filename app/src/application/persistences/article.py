from abc import ABC, abstractmethod

from app.src.entities.article import ArticleEntity


class ArticlePersistency(ABC):
    @abstractmethod
    async def list(self) -> str:
        raise NotImplementedError

    @abstractmethod
    async def add(self, entity: ArticleEntity) -> str:
        raise NotImplementedError
