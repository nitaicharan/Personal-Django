from fastapi import FastAPI
from fastapi_injector import Injected, attach_injector
from injector import Injector
from app.src.adapters.api.articles import articles_controllers
from app.src.adapters.spi.db.repositories.articles import ArticleRepository
from app.src.application.persistences.article_persistency import ArticlePersistency
from app.src.application.use_cases.article.list_articles import ArticleUseCase


def create_app() -> FastAPI:
    app = FastAPI()

    injector = Injector()
    injector.binder.bind(interface=ArticlePersistency, to=ArticleRepository)
    attach_injector(app, injector)

    app.include_router(articles_controllers.router, prefix="/api/articles")
    return app
