from typing import Annotated
from fastapi import APIRouter, Body
from fastapi_injector import Injected
from app.src.adapters.api.articles.dto.create import CreateArticleDto
from app.src.application.use_cases.articles.create_article import CreateArticlesUseCase
from app.src.application.use_cases.articles.list_articles import ListArticlesUseCase
from app.src.entities.article import ArticleEntity

router = APIRouter()

@router.get("")
async def list(use_case: ListArticlesUseCase = Injected(ListArticlesUseCase)):
    return await use_case.list()

@router.post("", status_code=201)
async def add(
    article: Annotated[CreateArticleDto, Body()],
    use_case: CreateArticlesUseCase = Injected(CreateArticlesUseCase),
):
    entity = ArticleEntity()
    entity.title = article.title
    await use_case.add(entity)
