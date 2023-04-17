from typing import AsyncIterator

import grpc.aio
import pytest
from sqlalchemy.ext.asyncio import AsyncEngine

from flexjob.protos.flexjob.flexjob_pb2 import CreateJobRequest
from flexjob.protos.flexjob.flexjob_pb2_grpc import FlexJobStub
from flexjob.protos.google.longrunning.operations_pb2 import GetOperationRequest
from flexjob.protos.google.longrunning.operations_pb2_grpc import OperationsStub
from flexjob.server import server


@pytest.fixture(autouse=True)
async def test_server(mock_engine: AsyncEngine) -> AsyncIterator[grpc.aio.Server]:
    with server.graph.override():
        server.graph.bind_instance(mock_engine, resolves=AsyncEngine)
        async with server.create_server(port="localhost:50051") as s:
            yield s


@pytest.fixture(autouse=True)
async def test_channel(test_server: grpc.aio.Server) -> AsyncIterator[grpc.aio.Channel]:
    async with grpc.aio.insecure_channel("localhost:50051") as channel:
        yield channel


async def test_creating_job(test_channel: grpc.aio.Channel) -> None:
    job_stub = FlexJobStub(test_channel)
    create_response = await job_stub.CreateJob(CreateJobRequest(instance="foo"))
    print(create_response.name, create_response.done)

    ops_stub = OperationsStub(test_channel)
    get_response = await ops_stub.GetOperation(
        GetOperationRequest(name=create_response.name)
    )
    print(get_response.name, get_response.done)
