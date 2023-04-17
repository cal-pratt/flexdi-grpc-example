import logging

import grpc.aio

from flexjob.protos.google.longrunning import operations_pb2, operations_pb2_grpc
from flexjob.server.store import OpsStore
from flexjob.server.util import ServicerContext

LOGGER = logging.getLogger(__name__)


class OperationsServicer(operations_pb2_grpc.OperationsServicer):
    def __init__(self, server: grpc.aio.Server) -> None:
        operations_pb2_grpc.add_OperationsServicer_to_server(self, server)

    async def GetOperation(  # type: ignore[override]
        self,
        request: operations_pb2.GetOperationRequest,
        context: ServicerContext,
        store: OpsStore,
    ) -> operations_pb2.Operation:
        LOGGER.info("In the operation")
        return await store.get_ops(*request.name.split("/"))
