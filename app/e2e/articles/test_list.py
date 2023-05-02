import pytest
from app.main import app
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_list():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/api/articles")
    assert response.status_code == 200
