from injector import Inject
from app.src.application.persistences.article_persistency import ArticlePersistency


class ArticleUseCase:
    def __init__(self, persistancy: Inject[ArticlePersistency]):
        self.persitency = persistancy

    def list(self):
        return self.persitency.list()
