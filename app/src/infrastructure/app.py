from fastapi import FastAPI
from fastapi_injector import attach_injector
from injector import Injector
from app.src.adapters.api.articles import articles_controllers
from app.src.adapters.spi.db.repositories.article import ArticleRepository
from app.src.application.persistences.article import ArticlePersistency

# from app.src.adapters.spi.db.repositories.author import AuthorRepository
# from app.src.application.persistences.athor import AuthorPersistency


def create_app() -> FastAPI:
    app = FastAPI()

    injector = Injector()
    injector.binder.bind(interface=ArticlePersistency, to=ArticleRepository)
    # injector.binder.bind(interface=AuthorPersistency, to=AuthorRepository)
    attach_injector(app, injector)

    app.include_router(articles_controllers.router, prefix="/api/articles")
    return app
