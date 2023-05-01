from injector import Inject
from app.src.application.persistences.article import ArticlePersistency
from app.src.entities.article import ArticleEntity


class CreateArticlesUseCase:
    def __init__(self, persistancy: Inject[ArticlePersistency]):
        self.persitency = persistancy

    def add(self, article: ArticleEntity):
        return self.persitency.add(article)
