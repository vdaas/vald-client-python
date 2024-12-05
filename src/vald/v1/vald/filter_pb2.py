# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: vald/v1/vald/filter.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'vald/v1/vald/filter.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from vald.v1.payload import payload_pb2 as vald_dot_v1_dot_payload_dot_payload__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19vald/v1/vald/filter.proto\x12\x07vald.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1dvald/v1/payload/payload.proto2\xac\n\n\x06\x46ilter\x12h\n\x0cSearchObject\x12 .payload.v1.Search.ObjectRequest\x1a\x1b.payload.v1.Search.Response\"\x19\x82\xd3\xe4\x93\x02\x13\"\x0e/search/object:\x01*\x12|\n\x11MultiSearchObject\x12%.payload.v1.Search.MultiObjectRequest\x1a\x1c.payload.v1.Search.Responses\"\"\x82\xd3\xe4\x93\x02\x1c\"\x17/search/object/multiple:\x01*\x12_\n\x12StreamSearchObject\x12 .payload.v1.Search.ObjectRequest\x1a!.payload.v1.Search.StreamResponse\"\x00(\x01\x30\x01\x12h\n\x0cInsertObject\x12 .payload.v1.Insert.ObjectRequest\x1a\x1b.payload.v1.Object.Location\"\x19\x82\xd3\xe4\x93\x02\x13\"\x0e/insert/object:\x01*\x12_\n\x12StreamInsertObject\x12 .payload.v1.Insert.ObjectRequest\x1a!.payload.v1.Object.StreamLocation\"\x00(\x01\x30\x01\x12|\n\x11MultiInsertObject\x12%.payload.v1.Insert.MultiObjectRequest\x1a\x1c.payload.v1.Object.Locations\"\"\x82\xd3\xe4\x93\x02\x1c\"\x17/insert/object/multiple:\x01*\x12h\n\x0cUpdateObject\x12 .payload.v1.Update.ObjectRequest\x1a\x1b.payload.v1.Object.Location\"\x19\x82\xd3\xe4\x93\x02\x13\"\x0e/update/object:\x01*\x12_\n\x12StreamUpdateObject\x12 .payload.v1.Update.ObjectRequest\x1a!.payload.v1.Object.StreamLocation\"\x00(\x01\x30\x01\x12|\n\x11MultiUpdateObject\x12%.payload.v1.Update.MultiObjectRequest\x1a\x1c.payload.v1.Object.Locations\"\"\x82\xd3\xe4\x93\x02\x1c\"\x17/update/object/multiple:\x01*\x12h\n\x0cUpsertObject\x12 .payload.v1.Upsert.ObjectRequest\x1a\x1b.payload.v1.Object.Location\"\x19\x82\xd3\xe4\x93\x02\x13\"\x0e/upsert/object:\x01*\x12_\n\x12StreamUpsertObject\x12 .payload.v1.Upsert.ObjectRequest\x1a!.payload.v1.Object.StreamLocation\"\x00(\x01\x30\x01\x12|\n\x11MultiUpsertObject\x12%.payload.v1.Upsert.MultiObjectRequest\x1a\x1c.payload.v1.Object.Locations\"\"\x82\xd3\xe4\x93\x02\x1c\"\x17/upsert/object/multiple:\x01*BS\n\x1aorg.vdaas.vald.api.v1.valdB\nValdFilterP\x01Z\'github.com/vdaas/vald/apis/grpc/v1/valdb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'vald.v1.vald.filter_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\032org.vdaas.vald.api.v1.valdB\nValdFilterP\001Z\'github.com/vdaas/vald/apis/grpc/v1/vald'
  _globals['_FILTER'].methods_by_name['SearchObject']._loaded_options = None
  _globals['_FILTER'].methods_by_name['SearchObject']._serialized_options = b'\202\323\344\223\002\023\"\016/search/object:\001*'
  _globals['_FILTER'].methods_by_name['MultiSearchObject']._loaded_options = None
  _globals['_FILTER'].methods_by_name['MultiSearchObject']._serialized_options = b'\202\323\344\223\002\034\"\027/search/object/multiple:\001*'
  _globals['_FILTER'].methods_by_name['InsertObject']._loaded_options = None
  _globals['_FILTER'].methods_by_name['InsertObject']._serialized_options = b'\202\323\344\223\002\023\"\016/insert/object:\001*'
  _globals['_FILTER'].methods_by_name['MultiInsertObject']._loaded_options = None
  _globals['_FILTER'].methods_by_name['MultiInsertObject']._serialized_options = b'\202\323\344\223\002\034\"\027/insert/object/multiple:\001*'
  _globals['_FILTER'].methods_by_name['UpdateObject']._loaded_options = None
  _globals['_FILTER'].methods_by_name['UpdateObject']._serialized_options = b'\202\323\344\223\002\023\"\016/update/object:\001*'
  _globals['_FILTER'].methods_by_name['MultiUpdateObject']._loaded_options = None
  _globals['_FILTER'].methods_by_name['MultiUpdateObject']._serialized_options = b'\202\323\344\223\002\034\"\027/update/object/multiple:\001*'
  _globals['_FILTER'].methods_by_name['UpsertObject']._loaded_options = None
  _globals['_FILTER'].methods_by_name['UpsertObject']._serialized_options = b'\202\323\344\223\002\023\"\016/upsert/object:\001*'
  _globals['_FILTER'].methods_by_name['MultiUpsertObject']._loaded_options = None
  _globals['_FILTER'].methods_by_name['MultiUpsertObject']._serialized_options = b'\202\323\344\223\002\034\"\027/upsert/object/multiple:\001*'
  _globals['_FILTER']._serialized_start=100
  _globals['_FILTER']._serialized_end=1424
# @@protoc_insertion_point(module_scope)
