import asyncio
from typing import AsyncGenerator

import pytest
from httpx import AsyncClient, ASGITransport
from sqlalchemy import text, pool
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker, AsyncEngine
from sqlalchemy.engine import make_url

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "../backend"))

from backend.app.main import app
from backend.app.database.session import Base, get_db
from backend.app.core.config import settings

TEST_DB_NAME = "event_manager_test"
TEST_DB_URL = settings.DB_URL.rsplit("/", 1)[0] + f"/{TEST_DB_NAME}"

@pytest.fixture(scope="session", autouse=True)
def setup_test_db():
    async def _setup():
        current_url = make_url(settings.DB_URL)
        app_user = current_url.username

        root_url = current_url.set(username="root", password="root", database="mysql")
        root_engine = create_async_engine(root_url, echo=False, isolation_level="AUTOCOMMIT")

        try:
            async with root_engine.connect() as conn:
                await conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {TEST_DB_NAME}"))
                await conn.execute(text(f"GRANT ALL PRIVILEGES ON {TEST_DB_NAME}.* TO '{app_user}'@'%'"))
                print(f"✅ Test database '{TEST_DB_NAME}' ensured.")
        except Exception as e:
            print(f"❌ Error setting up test database: {e}")
        finally:
            await root_engine.dispose()

    asyncio.run(_setup())

@pytest.fixture(scope="function")
async def db_engine() -> AsyncGenerator[AsyncEngine, None]:
    engine = create_async_engine(TEST_DB_URL, echo=False, poolclass=pool.NullPool)
    yield engine
    await engine.dispose()

@pytest.fixture(scope="function")
def session_factory(db_engine):
    return async_sessionmaker(db_engine, class_=AsyncSession, expire_on_commit=False)

@pytest.fixture(scope="function")
async def db_session(db_engine, session_factory) -> AsyncGenerator[AsyncSession, None]:
    async with db_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with session_factory() as session:
        yield session

    async with db_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest.fixture(scope="function")
async def client(db_session) -> AsyncGenerator[AsyncClient, None]:
    async def override_get_db():
        yield db_session

    app.dependency_overrides[get_db] = override_get_db

    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac

    app.dependency_overrides.clear()

@pytest.fixture
async def create_user_fixture(client):
    user_data = {
        "first_name": "Test",
        "last_name": "User",
        "email": "test@test.com",
        "password": "password123"
    }
    response = await client.post("/api/v1/users/", json=user_data)
    return response.json()


@pytest.fixture
async def create_event_fixture(client):
    event_data = {
        "name": "Test Event",
        "starts_at": "2025-01-01T12:00:00",
        "ends_at": "2025-01-01T15:00:00"
    }
    response = await client.post("/api/v1/events/", json=event_data)
    return response.json()