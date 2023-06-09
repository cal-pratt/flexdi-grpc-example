# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from flexjob.protos.flexjob import flexjob_pb2 as flexjob_dot_flexjob__pb2
from flexjob.protos.google.longrunning import (
    operations_pb2 as google_dot_longrunning_dot_operations__pb2,
)


class FlexJobStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateJob = channel.unary_unary(
            "/flexjob.FlexJob/CreateJob",
            request_serializer=flexjob_dot_flexjob__pb2.CreateJobRequest.SerializeToString,
            response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
        )


class FlexJobServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateJob(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_FlexJobServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "CreateJob": grpc.unary_unary_rpc_method_handler(
            servicer.CreateJob,
            request_deserializer=flexjob_dot_flexjob__pb2.CreateJobRequest.FromString,
            response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "flexjob.FlexJob", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class FlexJob(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateJob(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/flexjob.FlexJob/CreateJob",
            flexjob_dot_flexjob__pb2.CreateJobRequest.SerializeToString,
            google_dot_longrunning_dot_operations__pb2.Operation.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
