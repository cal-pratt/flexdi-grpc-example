import logging
import uuid

import grpc.aio

from flexjob.protos.flexjob import flexjob_pb2, flexjob_pb2_grpc
from flexjob.protos.google.longrunning import operations_pb2
from flexjob.server.store import OpsStore
from flexjob.server.util import ServicerContext

LOGGER = logging.getLogger(__name__)


class FlexJobServicer(flexjob_pb2_grpc.FlexJobServicer):
    def __init__(self, server: grpc.aio.Server) -> None:
        flexjob_pb2_grpc.add_FlexJobServicer_to_server(self, server)

    async def CreateJob(  # type: ignore[override]
        self,
        request: flexjob_pb2.CreateJobRequest,
        context: ServicerContext,
        store: OpsStore,
    ) -> operations_pb2.Operation:
        LOGGER.info("Creating Job")
        ops = operations_pb2.Operation(
            name=f"{request.instance}/{str(uuid.uuid4())}", done=False
        )
        return await store.set_ops(ops)
