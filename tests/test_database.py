import uuid

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker

from flexjob.db.models import FlexJob


async def test_postgres(mock_engine: AsyncEngine) -> None:
    """
    Demonstrates how to configure a database connection with the testing setup.
    """

    async_session = async_sessionmaker(mock_engine, expire_on_commit=False)
    # Help out pycharm
    session: AsyncSession

    async with async_session() as session:
        session.add(FlexJob(instance="foo", job_id=str(uuid.uuid4())))
        await session.commit()

    async with async_session() as session:
        query = await session.execute(select(FlexJob))
        assert len(query.all()) == 1


async def test_postgres_again(mock_engine: AsyncEngine) -> None:
    """
    Running the tests for a second time to ensure that the tables are actually
    destroyed in between runs. If multiple values for the query appear, then
    we didn't drop the tables correctly in between runs.
    """

    async_session = async_sessionmaker(mock_engine, expire_on_commit=False)
    # Help out pycharm
    session: AsyncSession

    async with async_session() as session:
        session.add(FlexJob(instance="foo", job_id=str(uuid.uuid4())))
        await session.commit()

    async with async_session() as session:
        query = await session.execute(select(FlexJob))
        assert len(query.all()) == 1


async def test_ops_store(mock_engine: AsyncEngine) -> None:
    """
    Running the tests for a second time to ensure that the tables are actually
    destroyed in between runs. If multiple values for the query appear, then
    we didn't drop the tables correctly in between runs.
    """

    async_session = async_sessionmaker(mock_engine, expire_on_commit=False)
    # Help out pycharm
    session: AsyncSession

    from flexjob.protos.google.longrunning.operations_pb2 import Operation
    from flexjob.server.store import OpsStore

    instance, job_id = "foo", str(uuid.uuid4())

    async with async_session() as session:
        store = OpsStore(session)
        ops = Operation(name=f"{instance}/{job_id}")
        await store.set_ops(ops)

    async with async_session() as session:
        store = OpsStore(session)
        ops = await store.get_ops(instance, job_id)
        assert ops.name == f"{instance}/{job_id}"
