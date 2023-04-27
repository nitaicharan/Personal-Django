from fastapi import FastAPI
from injector import Injector
from fastapi_injector import attach_injector
from app.src.adapters.api.articles import articles_controllers


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(articles_controllers.router, prefix="/api/articles")

    attach_injector(app, Injector())
    return app
