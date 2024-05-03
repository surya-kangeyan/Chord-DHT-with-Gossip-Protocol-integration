# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from proto import chord_pb2 as proto_dot_chord__pb2

GRPC_GENERATED_VERSION = '1.63.0'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in proto/chord_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class ChordServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetSuccessor = channel.unary_unary(
                '/chord.ChordService/GetSuccessor',
                request_serializer=proto_dot_chord__pb2.Empty.SerializeToString,
                response_deserializer=proto_dot_chord__pb2.NodeInfo.FromString,
                _registered_method=True)
        self.GetSuccessorList = channel.unary_unary(
                '/chord.ChordService/GetSuccessorList',
                request_serializer=proto_dot_chord__pb2.NodeInfo.SerializeToString,
                response_deserializer=proto_dot_chord__pb2.SuccessorListResponse.FromString,
                _registered_method=True)
        self.GetPredecessor = channel.unary_unary(
                '/chord.ChordService/GetPredecessor',
                request_serializer=proto_dot_chord__pb2.NodeInfo.SerializeToString,
                response_deserializer=proto_dot_chord__pb2.NodeInfo.FromString,
                _registered_method=True)
        self.FindSuccessor = channel.unary_unary(
                '/chord.ChordService/FindSuccessor',
                request_serializer=proto_dot_chord__pb2.FindSuccessorRequest.SerializeToString,
                response_deserializer=proto_dot_chord__pb2.NodeInfo.FromString,
                _registered_method=True)
        self.FindPredecessor = channel.unary_unary(
                '/chord.ChordService/FindPredecessor',
                request_serializer=proto_dot_chord__pb2.NodeInfo.SerializeToString,
                response_deserializer=proto_dot_chord__pb2.NodeInfo.FromString,
                _registered_method=True)
        self.InitFingerTable = channel.unary_unary(
                '/chord.ChordService/InitFingerTable',
                request_serializer=proto_dot_chord__pb2.NodeInfo.SerializeToString,
                response_deserializer=proto_dot_chord__pb2.FingerTable.FromString,
                _registered_method=True)


class ChordServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetSuccessor(self, request, context):
        """RPC to get the successor of a node
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSuccessorList(self, request, context):
        """RPC to get the successor list of a node
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPredecessor(self, request, context):
        """RPC to get the predecessor of a node
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FindSuccessor(self, request, context):
        """RPC to find the successor of a node
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FindPredecessor(self, request, context):
        """RPC to find the predecessor of a node
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def InitFingerTable(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ChordServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetSuccessor': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSuccessor,
                    request_deserializer=proto_dot_chord__pb2.Empty.FromString,
                    response_serializer=proto_dot_chord__pb2.NodeInfo.SerializeToString,
            ),
            'GetSuccessorList': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSuccessorList,
                    request_deserializer=proto_dot_chord__pb2.NodeInfo.FromString,
                    response_serializer=proto_dot_chord__pb2.SuccessorListResponse.SerializeToString,
            ),
            'GetPredecessor': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPredecessor,
                    request_deserializer=proto_dot_chord__pb2.NodeInfo.FromString,
                    response_serializer=proto_dot_chord__pb2.NodeInfo.SerializeToString,
            ),
            'FindSuccessor': grpc.unary_unary_rpc_method_handler(
                    servicer.FindSuccessor,
                    request_deserializer=proto_dot_chord__pb2.FindSuccessorRequest.FromString,
                    response_serializer=proto_dot_chord__pb2.NodeInfo.SerializeToString,
            ),
            'FindPredecessor': grpc.unary_unary_rpc_method_handler(
                    servicer.FindPredecessor,
                    request_deserializer=proto_dot_chord__pb2.NodeInfo.FromString,
                    response_serializer=proto_dot_chord__pb2.NodeInfo.SerializeToString,
            ),
            'InitFingerTable': grpc.unary_unary_rpc_method_handler(
                    servicer.InitFingerTable,
                    request_deserializer=proto_dot_chord__pb2.NodeInfo.FromString,
                    response_serializer=proto_dot_chord__pb2.FingerTable.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'chord.ChordService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ChordService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetSuccessor(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/chord.ChordService/GetSuccessor',
            proto_dot_chord__pb2.Empty.SerializeToString,
            proto_dot_chord__pb2.NodeInfo.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetSuccessorList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/chord.ChordService/GetSuccessorList',
            proto_dot_chord__pb2.NodeInfo.SerializeToString,
            proto_dot_chord__pb2.SuccessorListResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetPredecessor(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/chord.ChordService/GetPredecessor',
            proto_dot_chord__pb2.NodeInfo.SerializeToString,
            proto_dot_chord__pb2.NodeInfo.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def FindSuccessor(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/chord.ChordService/FindSuccessor',
            proto_dot_chord__pb2.FindSuccessorRequest.SerializeToString,
            proto_dot_chord__pb2.NodeInfo.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def FindPredecessor(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/chord.ChordService/FindPredecessor',
            proto_dot_chord__pb2.NodeInfo.SerializeToString,
            proto_dot_chord__pb2.NodeInfo.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def InitFingerTable(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/chord.ChordService/InitFingerTable',
            proto_dot_chord__pb2.NodeInfo.SerializeToString,
            proto_dot_chord__pb2.FingerTable.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)