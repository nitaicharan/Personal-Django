from pydantic import BaseModel, Field


class CreateArticleDto(BaseModel):
    title: str = Field(
        title="The title of the article",
        min_length=1,
        max_length=100,
    )
