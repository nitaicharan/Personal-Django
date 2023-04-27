from fastapi_injector import Injected

from ...persistences.article_persistency import ArticlePersistency


class ListArticleUseCase:
    def __init__(self, persistency: ArticlePersistency = Injected(ArticlePersistency)):
        self.persistency = persistency

    def list(self):
        self.persistency.list()
