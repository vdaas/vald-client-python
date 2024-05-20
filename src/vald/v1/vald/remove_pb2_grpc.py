# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from vald.v1.payload import payload_pb2 as vald_dot_v1_dot_payload_dot_payload__pb2


class RemoveStub(object):
    """Remove service provides ways to remove indexed vectors.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Remove = channel.unary_unary(
                '/vald.v1.Remove/Remove',
                request_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Remove.Request.SerializeToString,
                response_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Location.FromString,
                _registered_method=True)
        self.RemoveByTimestamp = channel.unary_unary(
                '/vald.v1.Remove/RemoveByTimestamp',
                request_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Remove.TimestampRequest.SerializeToString,
                response_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Locations.FromString,
                _registered_method=True)
        self.StreamRemove = channel.stream_stream(
                '/vald.v1.Remove/StreamRemove',
                request_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Remove.Request.SerializeToString,
                response_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.StreamLocation.FromString,
                _registered_method=True)
        self.MultiRemove = channel.unary_unary(
                '/vald.v1.Remove/MultiRemove',
                request_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Remove.MultiRequest.SerializeToString,
                response_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Locations.FromString,
                _registered_method=True)


class RemoveServicer(object):
    """Remove service provides ways to remove indexed vectors.
    """

    def Remove(self, request, context):
        """A method to remove an indexed vector.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RemoveByTimestamp(self, request, context):
        """A method to remove an indexed vector based on timestamp.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamRemove(self, request_iterator, context):
        """A method to remove multiple indexed vectors by bidirectional streaming.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MultiRemove(self, request, context):
        """A method to remove multiple indexed vectors in a single request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RemoveServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Remove': grpc.unary_unary_rpc_method_handler(
                    servicer.Remove,
                    request_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Remove.Request.FromString,
                    response_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Location.SerializeToString,
            ),
            'RemoveByTimestamp': grpc.unary_unary_rpc_method_handler(
                    servicer.RemoveByTimestamp,
                    request_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Remove.TimestampRequest.FromString,
                    response_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Locations.SerializeToString,
            ),
            'StreamRemove': grpc.stream_stream_rpc_method_handler(
                    servicer.StreamRemove,
                    request_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Remove.Request.FromString,
                    response_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.StreamLocation.SerializeToString,
            ),
            'MultiRemove': grpc.unary_unary_rpc_method_handler(
                    servicer.MultiRemove,
                    request_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Remove.MultiRequest.FromString,
                    response_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Locations.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'vald.v1.Remove', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('vald.v1.Remove', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Remove(object):
    """Remove service provides ways to remove indexed vectors.
    """

    @staticmethod
    def Remove(request,
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
            '/vald.v1.Remove/Remove',
            vald_dot_v1_dot_payload_dot_payload__pb2.Remove.Request.SerializeToString,
            vald_dot_v1_dot_payload_dot_payload__pb2.Object.Location.FromString,
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
    def RemoveByTimestamp(request,
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
            '/vald.v1.Remove/RemoveByTimestamp',
            vald_dot_v1_dot_payload_dot_payload__pb2.Remove.TimestampRequest.SerializeToString,
            vald_dot_v1_dot_payload_dot_payload__pb2.Object.Locations.FromString,
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
    def StreamRemove(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(
            request_iterator,
            target,
            '/vald.v1.Remove/StreamRemove',
            vald_dot_v1_dot_payload_dot_payload__pb2.Remove.Request.SerializeToString,
            vald_dot_v1_dot_payload_dot_payload__pb2.Object.StreamLocation.FromString,
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
    def MultiRemove(request,
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
            '/vald.v1.Remove/MultiRemove',
            vald_dot_v1_dot_payload_dot_payload__pb2.Remove.MultiRequest.SerializeToString,
            vald_dot_v1_dot_payload_dot_payload__pb2.Object.Locations.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
