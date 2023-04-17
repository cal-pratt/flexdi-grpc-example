import logging
from contextlib import asynccontextmanager
from typing import AsyncIterator

import grpc.aio
from flexdi import FlexGraph
from flexdi.grpc import FlexInterceptor
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine

from ..db.models import Base
from .flexjob import FlexJobServicer
from .operations import OperationsServicer
from .store import OpsStore

LOGGER = logging.getLogger(__name__)

graph = FlexGraph()


@graph.bind(scope="application", eager=True)
async def provide_engine() -> AsyncIterator[AsyncEngine]:
    engine = create_async_engine("sqlite+aiosqlite:///mydb.db")
    try:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        yield engine
    finally:
        await engine.dispose()


@graph.bind
async def provide_session(engine: AsyncEngine) -> AsyncIterator[AsyncSession]:
    async with AsyncSession(engine) as session:
        yield session


# TODO Fix the need for this dummy binding.
# The Server object and the app scope have a co-dependency. The server cant
# be created without the app scope being attached to the interceptor, and the
# servicer objects have a dependency on the server. We could make all of the
# bindings after the app scope is created, but this makes it awkward to override
# values during startup.
# Should it be possible to create the application scope instance without validating
# that all dependencies are resolvable?
graph.bind_instance(None, resolves=grpc.aio.Server)

graph.bind(OpsStore, scope="application", eager=True)
graph.bind(OperationsServicer, scope="application", eager=True)
graph.bind(FlexJobServicer, scope="application", eager=True)


@asynccontextmanager
async def create_server(port: str = "[::]:50051") -> AsyncIterator[grpc.aio.Server]:
    app_scope = graph.application_scope()
    app_scope.bind_instance(
        server := grpc.aio.server(interceptors=[FlexInterceptor(app_scope)]),
        resolves=grpc.aio.Server,
    )

    async with app_scope:
        server.add_insecure_port(port)
        await server.start()
        try:
            yield server
        finally:
            await server.stop(grace=None)


async def serve(port: str = "[::]:50051") -> None:
    async with create_server(port) as server:
        await server.wait_for_termination()
