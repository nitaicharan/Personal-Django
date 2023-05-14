from injector import Inject
from app.src.application.persistences.article import ArticlePersistency

# from app.src.application.persistences.athor import AuthorPersistency
from app.src.entities.article import ArticleEntity


class CreateArticlesUseCase:
    def __init__(
        self,
        persistancy: Inject[ArticlePersistency],
        # authorPersistency: Inject[AuthorPersistency],
    ):
        self.persitency = persistancy
        # self.authorPersistency = authorPersistency

    def add(self, article: ArticleEntity):
        # author = await self.authorPersistency.find(article.author.id)
        # print(author)
        return self.persitency.add(article)
