from datetime import datetime
from fastapi.testclient import TestClient
import pytest
from app.main import app
import random
import string
from httpx import AsyncClient


client = TestClient(app)


@pytest.mark.asyncio
async def test_create():
    letters = string.ascii_lowercase
    body = {
        "slug": "".join(random.choice(letters) for _ in range(10)),
        "title": "".join(random.choice(letters) for _ in range(10)),
        "description": "".join(random.choice(letters) for _ in range(10)),
        "body": "".join(random.choice(letters) for _ in range(10)),
        "tagList": [],
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat(),
        "favorited": False,
        "favoritesCount": 1,
        # "author": Auth,
    }

    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post(
            url="/api/articles",
            json=body,
        )

    assert response.status_code == 201
