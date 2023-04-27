from abc import ABC, abstractmethod


class ArticlePersistency(ABC):
    @abstractmethod
    def list(self) -> str:
        raise NotImplementedError
