from abc import ABC, abstractmethod

class ArticlePersistency(ABC):

    @abstractmethod
    async def list(self) -> str:
        raise NotImplementedError
