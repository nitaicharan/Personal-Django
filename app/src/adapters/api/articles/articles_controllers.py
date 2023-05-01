from fastapi import APIRouter
from fastapi_injector import Injected
from app.src.application.use_cases.article.list_articles import ArticleUseCase

router = APIRouter()

@router.get("")
async def create_product(use_case: ArticleUseCase = Injected(ArticleUseCase)):
    return await use_case.list()
