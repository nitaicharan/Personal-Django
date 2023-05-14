from datetime import datetime
from fastapi.testclient import TestClient
import pytest
from app.main import app
import random
import string
from httpx import AsyncClient


client = TestClient(app)


@pytest.mark.asyncio
async def test_find():
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
        "author_id": 0,
        # "author": Auth,
    }

    async with AsyncClient(app=app, base_url="http://test") as client:
        saved_request = await client.post(
            url="/api/articles",
            json=body,
        )
        saved_entity = saved_request.json()

        found_request = await client.get(url="/api/articles/" + str(saved_entity["id"]))
        found_entity = found_request.json()

        assert found_request.status_code == 200
        assert found_entity["id"] == saved_entity["id"]
