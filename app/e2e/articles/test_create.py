from fastapi.testclient import TestClient
from app.main import app
import random
import string


client = TestClient(app)


def test_create():
    letters = string.ascii_lowercase
    body = {
        # "slug": "".join(random.choice(letters) for _ in range(10)),
        "title": "".join(random.choice(letters) for _ in range(10)),
        # "description": "".join(random.choice(letters) for _ in range(10)),
        # "body": "".join(random.choice(letters) for _ in range(10)),
        # "tagList": list[str],
        # "createdAt": datetime,
        # "updatedAt": datetime,
        # "favorited": False,
        # "favoritesCount": 1,
        # "author": Auth,
    }

    response = client.post(
        url="/api/articles",
        json=body,
    )
    assert response.status_code == 201
