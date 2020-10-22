# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from vald.v1.payload import payload_pb2 as vald_dot_v1_dot_payload_dot_payload__pb2


class InsertStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Insert = channel.unary_unary(
                '/vald.v1.Insert/Insert',
                request_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Insert.Request.SerializeToString,
                response_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Location.FromString,
                )
        self.StreamInsert = channel.stream_stream(
                '/vald.v1.Insert/StreamInsert',
                request_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Insert.Request.SerializeToString,
                response_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Location.FromString,
                )
        self.MultiInsert = channel.unary_unary(
                '/vald.v1.Insert/MultiInsert',
                request_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Insert.MultiRequest.SerializeToString,
                response_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Locations.FromString,
                )


class InsertServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Insert(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamInsert(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MultiInsert(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_InsertServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Insert': grpc.unary_unary_rpc_method_handler(
                    servicer.Insert,
                    request_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Insert.Request.FromString,
                    response_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Location.SerializeToString,
            ),
            'StreamInsert': grpc.stream_stream_rpc_method_handler(
                    servicer.StreamInsert,
                    request_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Insert.Request.FromString,
                    response_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Location.SerializeToString,
            ),
            'MultiInsert': grpc.unary_unary_rpc_method_handler(
                    servicer.MultiInsert,
                    request_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Insert.MultiRequest.FromString,
                    response_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Locations.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'vald.v1.Insert', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Insert(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Insert(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/vald.v1.Insert/Insert',
            vald_dot_v1_dot_payload_dot_payload__pb2.Insert.Request.SerializeToString,
            vald_dot_v1_dot_payload_dot_payload__pb2.Object.Location.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StreamInsert(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/vald.v1.Insert/StreamInsert',
            vald_dot_v1_dot_payload_dot_payload__pb2.Insert.Request.SerializeToString,
            vald_dot_v1_dot_payload_dot_payload__pb2.Object.Location.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MultiInsert(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/vald.v1.Insert/MultiInsert',
            vald_dot_v1_dot_payload_dot_payload__pb2.Insert.MultiRequest.SerializeToString,
            vald_dot_v1_dot_payload_dot_payload__pb2.Object.Locations.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
