import asyncio

import grpc.aio

from flexjob.protos.google.longrunning import operations_pb2, operations_pb2_grpc
from flexjob.protos.flexjob import flexjob_pb2, flexjob_pb2_grpc


async def client():
    async with grpc.aio.insecure_channel('localhost:50051') as channel:
        job_stub = flexjob_pb2_grpc.FlexJobStub(channel)
        create_response = await job_stub.CreateJob(flexjob_pb2.CreateJobRequest(instance="foo"))
        print(create_response.name, create_response.done)

        ops_stub = operations_pb2_grpc.OperationsStub(channel)
        get_response = await ops_stub.GetOperation(operations_pb2.GetOperationRequest(name=create_response.name))
        print(get_response.name, get_response.done)


if __name__ == "__main__":
    asyncio.run(client())
