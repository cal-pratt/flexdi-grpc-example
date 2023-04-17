from typing import AsyncIterator

import pytest
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine
from testcontainers.postgres import PostgresContainer  # type: ignore

from flexjob.db.models import Base


@pytest.fixture(scope="session")
def postgres_container() -> PostgresContainer:
    """
    Uses testcontainers-postgres to create a fresh DB for the pytest run.
    To minimize test time, the database should be refreshed in between each run.
    """

    class PostgresContainerNoPipe(PostgresContainer):  # type: ignore
        def get_connection_url(self, host=None):  # type: ignore
            return super().get_connection_url().replace("localnpipe", "localhost")

    postgres_container = PostgresContainerNoPipe("postgres:12")
    with postgres_container as postgres:
        yield postgres


@pytest.fixture
async def mock_engine(
    postgres_container: PostgresContainer,
) -> AsyncIterator[AsyncEngine]:
    """
    Using the postgres container, configure the database for the application.
    The database should be reset for each test ensuring that test data does not
    leak across the individual tests.
    """

    postgres_container.driver = "asyncpg"
    engine = create_async_engine(postgres_container.get_connection_url())
    try:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        yield engine
    finally:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
        await engine.dispose()
