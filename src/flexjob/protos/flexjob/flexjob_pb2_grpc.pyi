"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import flexjob.protos.flexjob.flexjob_pb2
import flexjob.protos.google.longrunning.operations_pb2
import grpc.aio as grpc
import typing

class FlexJobStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    CreateJob: grpc.UnaryUnaryMultiCallable[
        flexjob.protos.flexjob.flexjob_pb2.CreateJobRequest,
        flexjob.protos.google.longrunning.operations_pb2.Operation,
    ]

class FlexJobServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def CreateJob(
        self,
        request: flexjob.protos.flexjob.flexjob_pb2.CreateJobRequest,
        context: grpc.ServicerContext[typing.Any, typing.Any],
    ) -> flexjob.protos.google.longrunning.operations_pb2.Operation: ...

def add_FlexJobServicer_to_server(
    servicer: FlexJobServicer, server: grpc.Server
) -> None: ...