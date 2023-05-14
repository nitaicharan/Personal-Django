from typing import Annotated
from fastapi import APIRouter, Body
from fastapi_injector import Injected
from app.src.adapters.api.articles.dto.create import CreateArticleDto
from app.src.application.use_cases.articles.create_article import CreateArticlesUseCase
from app.src.application.use_cases.articles.find_article import FindArticlesUseCase
from app.src.application.use_cases.articles.list_articles import ListArticlesUseCase

router = APIRouter()


@router.get("")
async def list(use_case: ListArticlesUseCase = Injected(ListArticlesUseCase)):
    return await use_case.list()


@router.get("/{id}")
async def find(id: int, use_case: FindArticlesUseCase = Injected(FindArticlesUseCase)):
    return await use_case.find(id)


@router.post("")
async def add(
    dto: Annotated[CreateArticleDto, Body()],
    use_case: CreateArticlesUseCase = Injected(CreateArticlesUseCase),
):
    entity = dto.to_entity()
    return await use_case.add(entity)
