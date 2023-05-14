from injector import Inject
from app.src.application.persistences.article import ArticlePersistency


class FindArticlesUseCase:
    def __init__(self, persistancy: Inject[ArticlePersistency]):
        self.persitency = persistancy

    def find(self, id: int):
        return self.persitency.find(id)
