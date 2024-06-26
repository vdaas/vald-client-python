# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from vald.v1.payload import payload_pb2 as vald_dot_v1_dot_payload_dot_payload__pb2


class FilterStub(object):
    """Represent the ingress filter service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GenVector = channel.unary_unary(
                '/filter.ingress.v1.Filter/GenVector',
                request_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Blob.SerializeToString,
                response_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Vector.FromString,
                _registered_method=True)
        self.FilterVector = channel.unary_unary(
                '/filter.ingress.v1.Filter/FilterVector',
                request_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Vector.SerializeToString,
                response_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Vector.FromString,
                _registered_method=True)


class FilterServicer(object):
    """Represent the ingress filter service.
    """

    def GenVector(self, request, context):
        """Represent the RPC to generate the vector.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FilterVector(self, request, context):
        """Represent the RPC to filter the vector.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FilterServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GenVector': grpc.unary_unary_rpc_method_handler(
                    servicer.GenVector,
                    request_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Blob.FromString,
                    response_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Vector.SerializeToString,
            ),
            'FilterVector': grpc.unary_unary_rpc_method_handler(
                    servicer.FilterVector,
                    request_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Vector.FromString,
                    response_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Vector.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'filter.ingress.v1.Filter', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('filter.ingress.v1.Filter', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Filter(object):
    """Represent the ingress filter service.
    """

    @staticmethod
    def GenVector(request,
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
            '/filter.ingress.v1.Filter/GenVector',
            vald_dot_v1_dot_payload_dot_payload__pb2.Object.Blob.SerializeToString,
            vald_dot_v1_dot_payload_dot_payload__pb2.Object.Vector.FromString,
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
    def FilterVector(request,
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
            '/filter.ingress.v1.Filter/FilterVector',
            vald_dot_v1_dot_payload_dot_payload__pb2.Object.Vector.SerializeToString,
            vald_dot_v1_dot_payload_dot_payload__pb2.Object.Vector.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
