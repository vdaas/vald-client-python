# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from vald.v1.payload import payload_pb2 as vald_dot_v1_dot_payload_dot_payload__pb2


class ObjectStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Exists = channel.unary_unary(
                '/vald.v1.Object/Exists',
                request_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.ID.SerializeToString,
                response_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.ID.FromString,
                )
        self.GetObject = channel.unary_unary(
                '/vald.v1.Object/GetObject',
                request_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.ID.SerializeToString,
                response_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Vector.FromString,
                )
        self.StreamGetObject = channel.stream_stream(
                '/vald.v1.Object/StreamGetObject',
                request_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.ID.SerializeToString,
                response_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.StreamVector.FromString,
                )


class ObjectServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Exists(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetObject(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamGetObject(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ObjectServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Exists': grpc.unary_unary_rpc_method_handler(
                    servicer.Exists,
                    request_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.ID.FromString,
                    response_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.ID.SerializeToString,
            ),
            'GetObject': grpc.unary_unary_rpc_method_handler(
                    servicer.GetObject,
                    request_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.ID.FromString,
                    response_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Vector.SerializeToString,
            ),
            'StreamGetObject': grpc.stream_stream_rpc_method_handler(
                    servicer.StreamGetObject,
                    request_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.ID.FromString,
                    response_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.StreamVector.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'vald.v1.Object', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Object(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Exists(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/vald.v1.Object/Exists',
            vald_dot_v1_dot_payload_dot_payload__pb2.Object.ID.SerializeToString,
            vald_dot_v1_dot_payload_dot_payload__pb2.Object.ID.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetObject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/vald.v1.Object/GetObject',
            vald_dot_v1_dot_payload_dot_payload__pb2.Object.ID.SerializeToString,
            vald_dot_v1_dot_payload_dot_payload__pb2.Object.Vector.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StreamGetObject(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/vald.v1.Object/StreamGetObject',
            vald_dot_v1_dot_payload_dot_payload__pb2.Object.ID.SerializeToString,
            vald_dot_v1_dot_payload_dot_payload__pb2.Object.StreamVector.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
