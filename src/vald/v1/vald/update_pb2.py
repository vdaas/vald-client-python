# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: vald/v1/vald/update.proto
# Protobuf Python Version: 5.28.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    2,
    '',
    'vald/v1/vald/update.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from vald.v1.payload import payload_pb2 as vald_dot_v1_dot_payload_dot_payload__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19vald/v1/vald/update.proto\x12\x07vald.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1dvald/v1/payload/payload.proto2\x92\x03\n\x06Update\x12U\n\x06Update\x12\x1a.payload.v1.Update.Request\x1a\x1b.payload.v1.Object.Location\"\x12\x82\xd3\xe4\x93\x02\x0c\"\x07/update:\x01*\x12S\n\x0cStreamUpdate\x12\x1a.payload.v1.Update.Request\x1a!.payload.v1.Object.StreamLocation\"\x00(\x01\x30\x01\x12i\n\x0bMultiUpdate\x12\x1f.payload.v1.Update.MultiRequest\x1a\x1c.payload.v1.Object.Locations\"\x1b\x82\xd3\xe4\x93\x02\x15\"\x10/update/multiple:\x01*\x12q\n\x0fUpdateTimestamp\x12#.payload.v1.Update.TimestampRequest\x1a\x1b.payload.v1.Object.Location\"\x1c\x82\xd3\xe4\x93\x02\x16\"\x11/update/timestamp:\x01*BS\n\x1aorg.vdaas.vald.api.v1.valdB\nValdUpdateP\x01Z\'github.com/vdaas/vald/apis/grpc/v1/valdb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'vald.v1.vald.update_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\032org.vdaas.vald.api.v1.valdB\nValdUpdateP\001Z\'github.com/vdaas/vald/apis/grpc/v1/vald'
  _globals['_UPDATE'].methods_by_name['Update']._loaded_options = None
  _globals['_UPDATE'].methods_by_name['Update']._serialized_options = b'\202\323\344\223\002\014\"\007/update:\001*'
  _globals['_UPDATE'].methods_by_name['MultiUpdate']._loaded_options = None
  _globals['_UPDATE'].methods_by_name['MultiUpdate']._serialized_options = b'\202\323\344\223\002\025\"\020/update/multiple:\001*'
  _globals['_UPDATE'].methods_by_name['UpdateTimestamp']._loaded_options = None
  _globals['_UPDATE'].methods_by_name['UpdateTimestamp']._serialized_options = b'\202\323\344\223\002\026\"\021/update/timestamp:\001*'
  _globals['_UPDATE']._serialized_start=100
  _globals['_UPDATE']._serialized_end=502
# @@protoc_insertion_point(module_scope)
