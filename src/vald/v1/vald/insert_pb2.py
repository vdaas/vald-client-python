# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vald/v1/vald/insert.proto
# Protobuf Python Version: 4.25.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from vald.v1.payload import payload_pb2 as vald_dot_v1_dot_payload_dot_payload__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19vald/v1/vald/insert.proto\x12\x07vald.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1dvald/v1/payload/payload.proto2\x9f\x02\n\x06Insert\x12U\n\x06Insert\x12\x1a.payload.v1.Insert.Request\x1a\x1b.payload.v1.Object.Location\"\x12\x82\xd3\xe4\x93\x02\x0c\"\x07/insert:\x01*\x12S\n\x0cStreamInsert\x12\x1a.payload.v1.Insert.Request\x1a!.payload.v1.Object.StreamLocation\"\x00(\x01\x30\x01\x12i\n\x0bMultiInsert\x12\x1f.payload.v1.Insert.MultiRequest\x1a\x1c.payload.v1.Object.Locations\"\x1b\x82\xd3\xe4\x93\x02\x15\"\x10/insert/multiple:\x01*BS\n\x1aorg.vdaas.vald.api.v1.valdB\nValdInsertP\x01Z\'github.com/vdaas/vald/apis/grpc/v1/valdb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'vald.v1.vald.insert_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\032org.vdaas.vald.api.v1.valdB\nValdInsertP\001Z\'github.com/vdaas/vald/apis/grpc/v1/vald'
  _globals['_INSERT'].methods_by_name['Insert']._options = None
  _globals['_INSERT'].methods_by_name['Insert']._serialized_options = b'\202\323\344\223\002\014\"\007/insert:\001*'
  _globals['_INSERT'].methods_by_name['MultiInsert']._options = None
  _globals['_INSERT'].methods_by_name['MultiInsert']._serialized_options = b'\202\323\344\223\002\025\"\020/insert/multiple:\001*'
  _globals['_INSERT']._serialized_start=100
  _globals['_INSERT']._serialized_end=387
# @@protoc_insertion_point(module_scope)
