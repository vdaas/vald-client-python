# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from vald.v1.payload import payload_pb2 as vald_dot_v1_dot_payload_dot_payload__pb2


class ValdStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Exists = channel.unary_unary(
                '/vald.v1.Vald/Exists',
                request_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.ID.SerializeToString,
                response_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.ID.FromString,
                )
        self.Search = channel.unary_unary(
                '/vald.v1.Vald/Search',
                request_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Search.Request.SerializeToString,
                response_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Search.Response.FromString,
                )
        self.SearchByID = channel.unary_unary(
                '/vald.v1.Vald/SearchByID',
                request_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Search.IDRequest.SerializeToString,
                response_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Search.Response.FromString,
                )
        self.StreamSearch = channel.stream_stream(
                '/vald.v1.Vald/StreamSearch',
                request_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Search.Request.SerializeToString,
                response_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Search.Response.FromString,
                )
        self.StreamSearchByID = channel.stream_stream(
                '/vald.v1.Vald/StreamSearchByID',
                request_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Search.IDRequest.SerializeToString,
                response_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Search.Response.FromString,
                )
        self.Insert = channel.unary_unary(
                '/vald.v1.Vald/Insert',
                request_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Vector.SerializeToString,
                response_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Location.FromString,
                )
        self.StreamInsert = channel.stream_stream(
                '/vald.v1.Vald/StreamInsert',
                request_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Vector.SerializeToString,
                response_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Location.FromString,
                )
        self.MultiInsert = channel.unary_unary(
                '/vald.v1.Vald/MultiInsert',
                request_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Vectors.SerializeToString,
                response_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Locations.FromString,
                )
        self.Update = channel.unary_unary(
                '/vald.v1.Vald/Update',
                request_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Vector.SerializeToString,
                response_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Location.FromString,
                )
        self.StreamUpdate = channel.stream_stream(
                '/vald.v1.Vald/StreamUpdate',
                request_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Vector.SerializeToString,
                response_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Location.FromString,
                )
        self.MultiUpdate = channel.unary_unary(
                '/vald.v1.Vald/MultiUpdate',
                request_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Vectors.SerializeToString,
                response_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Locations.FromString,
                )
        self.Upsert = channel.unary_unary(
                '/vald.v1.Vald/Upsert',
                request_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Vector.SerializeToString,
                response_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Location.FromString,
                )
        self.StreamUpsert = channel.stream_stream(
                '/vald.v1.Vald/StreamUpsert',
                request_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Vector.SerializeToString,
                response_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Location.FromString,
                )
        self.MultiUpsert = channel.unary_unary(
                '/vald.v1.Vald/MultiUpsert',
                request_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Vectors.SerializeToString,
                response_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Locations.FromString,
                )
        self.Remove = channel.unary_unary(
                '/vald.v1.Vald/Remove',
                request_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.ID.SerializeToString,
                response_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Location.FromString,
                )
        self.StreamRemove = channel.stream_stream(
                '/vald.v1.Vald/StreamRemove',
                request_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.ID.SerializeToString,
                response_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Location.FromString,
                )
        self.MultiRemove = channel.unary_unary(
                '/vald.v1.Vald/MultiRemove',
                request_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.IDs.SerializeToString,
                response_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Locations.FromString,
                )
        self.GetObject = channel.unary_unary(
                '/vald.v1.Vald/GetObject',
                request_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.ID.SerializeToString,
                response_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Vector.FromString,
                )
        self.StreamGetObject = channel.stream_stream(
                '/vald.v1.Vald/StreamGetObject',
                request_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.ID.SerializeToString,
                response_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Vector.FromString,
                )


class ValdServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Exists(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Search(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SearchByID(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamSearch(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamSearchByID(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

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

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamUpdate(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MultiUpdate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Upsert(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamUpsert(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MultiUpsert(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Remove(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamRemove(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MultiRemove(self, request, context):
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


def add_ValdServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Exists': grpc.unary_unary_rpc_method_handler(
                    servicer.Exists,
                    request_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.ID.FromString,
                    response_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.ID.SerializeToString,
            ),
            'Search': grpc.unary_unary_rpc_method_handler(
                    servicer.Search,
                    request_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Search.Request.FromString,
                    response_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Search.Response.SerializeToString,
            ),
            'SearchByID': grpc.unary_unary_rpc_method_handler(
                    servicer.SearchByID,
                    request_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Search.IDRequest.FromString,
                    response_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Search.Response.SerializeToString,
            ),
            'StreamSearch': grpc.stream_stream_rpc_method_handler(
                    servicer.StreamSearch,
                    request_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Search.Request.FromString,
                    response_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Search.Response.SerializeToString,
            ),
            'StreamSearchByID': grpc.stream_stream_rpc_method_handler(
                    servicer.StreamSearchByID,
                    request_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Search.IDRequest.FromString,
                    response_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Search.Response.SerializeToString,
            ),
            'Insert': grpc.unary_unary_rpc_method_handler(
                    servicer.Insert,
                    request_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Vector.FromString,
                    response_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Location.SerializeToString,
            ),
            'StreamInsert': grpc.stream_stream_rpc_method_handler(
                    servicer.StreamInsert,
                    request_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Vector.FromString,
                    response_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Location.SerializeToString,
            ),
            'MultiInsert': grpc.unary_unary_rpc_method_handler(
                    servicer.MultiInsert,
                    request_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Vectors.FromString,
                    response_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Locations.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Vector.FromString,
                    response_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Location.SerializeToString,
            ),
            'StreamUpdate': grpc.stream_stream_rpc_method_handler(
                    servicer.StreamUpdate,
                    request_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Vector.FromString,
                    response_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Location.SerializeToString,
            ),
            'MultiUpdate': grpc.unary_unary_rpc_method_handler(
                    servicer.MultiUpdate,
                    request_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Vectors.FromString,
                    response_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Locations.SerializeToString,
            ),
            'Upsert': grpc.unary_unary_rpc_method_handler(
                    servicer.Upsert,
                    request_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Vector.FromString,
                    response_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Location.SerializeToString,
            ),
            'StreamUpsert': grpc.stream_stream_rpc_method_handler(
                    servicer.StreamUpsert,
                    request_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Vector.FromString,
                    response_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Location.SerializeToString,
            ),
            'MultiUpsert': grpc.unary_unary_rpc_method_handler(
                    servicer.MultiUpsert,
                    request_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Vectors.FromString,
                    response_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Locations.SerializeToString,
            ),
            'Remove': grpc.unary_unary_rpc_method_handler(
                    servicer.Remove,
                    request_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.ID.FromString,
                    response_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Location.SerializeToString,
            ),
            'StreamRemove': grpc.stream_stream_rpc_method_handler(
                    servicer.StreamRemove,
                    request_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.ID.FromString,
                    response_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Location.SerializeToString,
            ),
            'MultiRemove': grpc.unary_unary_rpc_method_handler(
                    servicer.MultiRemove,
                    request_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.IDs.FromString,
                    response_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Locations.SerializeToString,
            ),
            'GetObject': grpc.unary_unary_rpc_method_handler(
                    servicer.GetObject,
                    request_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.ID.FromString,
                    response_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Vector.SerializeToString,
            ),
            'StreamGetObject': grpc.stream_stream_rpc_method_handler(
                    servicer.StreamGetObject,
                    request_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.ID.FromString,
                    response_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Vector.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'vald.v1.Vald', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Vald(object):
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
        return grpc.experimental.unary_unary(request, target, '/vald.v1.Vald/Exists',
            vald_dot_v1_dot_payload_dot_payload__pb2.Object.ID.SerializeToString,
            vald_dot_v1_dot_payload_dot_payload__pb2.Object.ID.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Search(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/vald.v1.Vald/Search',
            vald_dot_v1_dot_payload_dot_payload__pb2.Search.Request.SerializeToString,
            vald_dot_v1_dot_payload_dot_payload__pb2.Search.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SearchByID(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/vald.v1.Vald/SearchByID',
            vald_dot_v1_dot_payload_dot_payload__pb2.Search.IDRequest.SerializeToString,
            vald_dot_v1_dot_payload_dot_payload__pb2.Search.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StreamSearch(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/vald.v1.Vald/StreamSearch',
            vald_dot_v1_dot_payload_dot_payload__pb2.Search.Request.SerializeToString,
            vald_dot_v1_dot_payload_dot_payload__pb2.Search.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StreamSearchByID(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/vald.v1.Vald/StreamSearchByID',
            vald_dot_v1_dot_payload_dot_payload__pb2.Search.IDRequest.SerializeToString,
            vald_dot_v1_dot_payload_dot_payload__pb2.Search.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

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
        return grpc.experimental.unary_unary(request, target, '/vald.v1.Vald/Insert',
            vald_dot_v1_dot_payload_dot_payload__pb2.Object.Vector.SerializeToString,
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
        return grpc.experimental.stream_stream(request_iterator, target, '/vald.v1.Vald/StreamInsert',
            vald_dot_v1_dot_payload_dot_payload__pb2.Object.Vector.SerializeToString,
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
        return grpc.experimental.unary_unary(request, target, '/vald.v1.Vald/MultiInsert',
            vald_dot_v1_dot_payload_dot_payload__pb2.Object.Vectors.SerializeToString,
            vald_dot_v1_dot_payload_dot_payload__pb2.Object.Locations.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/vald.v1.Vald/Update',
            vald_dot_v1_dot_payload_dot_payload__pb2.Object.Vector.SerializeToString,
            vald_dot_v1_dot_payload_dot_payload__pb2.Object.Location.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StreamUpdate(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/vald.v1.Vald/StreamUpdate',
            vald_dot_v1_dot_payload_dot_payload__pb2.Object.Vector.SerializeToString,
            vald_dot_v1_dot_payload_dot_payload__pb2.Object.Location.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MultiUpdate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/vald.v1.Vald/MultiUpdate',
            vald_dot_v1_dot_payload_dot_payload__pb2.Object.Vectors.SerializeToString,
            vald_dot_v1_dot_payload_dot_payload__pb2.Object.Locations.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Upsert(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/vald.v1.Vald/Upsert',
            vald_dot_v1_dot_payload_dot_payload__pb2.Object.Vector.SerializeToString,
            vald_dot_v1_dot_payload_dot_payload__pb2.Object.Location.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StreamUpsert(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/vald.v1.Vald/StreamUpsert',
            vald_dot_v1_dot_payload_dot_payload__pb2.Object.Vector.SerializeToString,
            vald_dot_v1_dot_payload_dot_payload__pb2.Object.Location.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MultiUpsert(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/vald.v1.Vald/MultiUpsert',
            vald_dot_v1_dot_payload_dot_payload__pb2.Object.Vectors.SerializeToString,
            vald_dot_v1_dot_payload_dot_payload__pb2.Object.Locations.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

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
        return grpc.experimental.unary_unary(request, target, '/vald.v1.Vald/Remove',
            vald_dot_v1_dot_payload_dot_payload__pb2.Object.ID.SerializeToString,
            vald_dot_v1_dot_payload_dot_payload__pb2.Object.Location.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

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
        return grpc.experimental.stream_stream(request_iterator, target, '/vald.v1.Vald/StreamRemove',
            vald_dot_v1_dot_payload_dot_payload__pb2.Object.ID.SerializeToString,
            vald_dot_v1_dot_payload_dot_payload__pb2.Object.Location.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

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
        return grpc.experimental.unary_unary(request, target, '/vald.v1.Vald/MultiRemove',
            vald_dot_v1_dot_payload_dot_payload__pb2.Object.IDs.SerializeToString,
            vald_dot_v1_dot_payload_dot_payload__pb2.Object.Locations.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/vald.v1.Vald/GetObject',
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
        return grpc.experimental.stream_stream(request_iterator, target, '/vald.v1.Vald/StreamGetObject',
            vald_dot_v1_dot_payload_dot_payload__pb2.Object.ID.SerializeToString,
            vald_dot_v1_dot_payload_dot_payload__pb2.Object.Vector.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
