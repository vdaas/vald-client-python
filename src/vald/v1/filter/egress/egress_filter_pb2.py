# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: vald/v1/filter/egress/egress_filter.proto
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
    'vald/v1/filter/egress/egress_filter.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from vald.v1.payload import payload_pb2 as vald_dot_v1_dot_payload_dot_payload__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)vald/v1/filter/egress/egress_filter.proto\x12\x10\x66ilter.egress.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1dvald/v1/payload/payload.proto2\xe0\x01\n\x06\x46ilter\x12n\n\x0e\x46ilterDistance\x12\x1b.payload.v1.Object.Distance\x1a\x1b.payload.v1.Object.Distance\"\"\x82\xd3\xe4\x93\x02\x1c\"\x17/filter/egress/distance:\x01*\x12\x66\n\x0c\x46ilterVector\x12\x19.payload.v1.Object.Vector\x1a\x19.payload.v1.Object.Vector\" \x82\xd3\xe4\x93\x02\x1a\"\x15/filter/egress/vector:\x01*Bk\n#org.vdaas.vald.api.v1.filter.egressB\x10ValdEgressFilterP\x01Z0github.com/vdaas/vald/apis/grpc/v1/filter/egressb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'vald.v1.filter.egress.egress_filter_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n#org.vdaas.vald.api.v1.filter.egressB\020ValdEgressFilterP\001Z0github.com/vdaas/vald/apis/grpc/v1/filter/egress'
  _globals['_FILTER'].methods_by_name['FilterDistance']._loaded_options = None
  _globals['_FILTER'].methods_by_name['FilterDistance']._serialized_options = b'\202\323\344\223\002\034\"\027/filter/egress/distance:\001*'
  _globals['_FILTER'].methods_by_name['FilterVector']._loaded_options = None
  _globals['_FILTER'].methods_by_name['FilterVector']._serialized_options = b'\202\323\344\223\002\032\"\025/filter/egress/vector:\001*'
  _globals['_FILTER']._serialized_start=125
  _globals['_FILTER']._serialized_end=349
# @@protoc_insertion_point(module_scope)
