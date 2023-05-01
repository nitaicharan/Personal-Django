from injector import Inject
from app.src.application.persistences.article import ArticlePersistency


class ListArticlesUseCase:
    def __init__(self, persistancy: Inject[ArticlePersistency]):
        self.persitency = persistancy

    def list(self):
        return self.persitency.list()
