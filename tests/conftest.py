import pytest_asyncio
import httpx


@pytest_asyncio.fixture(scope='function')
async def client() -> httpx.AsyncClient:
    return httpx.AsyncClient()
