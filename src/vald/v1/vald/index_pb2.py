# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: vald/v1/vald/index.proto
# Protobuf Python Version: 6.30.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    6,
    30,
    0,
    '',
    'vald/v1/vald/index.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from vald.v1.payload import payload_pb2 as vald_dot_v1_dot_payload_dot_payload__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18vald/v1/vald/index.proto\x12\x07vald.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1dvald/v1/payload/payload.proto2\xf1\x03\n\x05Index\x12Q\n\tIndexInfo\x12\x11.payload.v1.Empty\x1a\x1c.payload.v1.Info.Index.Count\"\x13\x82\xd3\xe4\x93\x02\r\x12\x0b/index/info\x12V\n\x0bIndexDetail\x12\x11.payload.v1.Empty\x1a\x1d.payload.v1.Info.Index.Detail\"\x15\x82\xd3\xe4\x93\x02\x0f\x12\r/index/detail\x12\x62\n\x0fIndexStatistics\x12\x11.payload.v1.Empty\x1a!.payload.v1.Info.Index.Statistics\"\x19\x82\xd3\xe4\x93\x02\x13\x12\x11/index/statistics\x12u\n\x15IndexStatisticsDetail\x12\x11.payload.v1.Empty\x1a\'.payload.v1.Info.Index.StatisticsDetail\" \x82\xd3\xe4\x93\x02\x1a\x12\x18/index/statistics/detail\x12\x62\n\rIndexProperty\x12\x11.payload.v1.Empty\x1a%.payload.v1.Info.Index.PropertyDetail\"\x17\x82\xd3\xe4\x93\x02\x11\x12\x0f/index/propertyBR\n\x1aorg.vdaas.vald.api.v1.valdB\tValdIndexP\x01Z\'github.com/vdaas/vald/apis/grpc/v1/valdb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'vald.v1.vald.index_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\032org.vdaas.vald.api.v1.valdB\tValdIndexP\001Z\'github.com/vdaas/vald/apis/grpc/v1/vald'
  _globals['_INDEX'].methods_by_name['IndexInfo']._loaded_options = None
  _globals['_INDEX'].methods_by_name['IndexInfo']._serialized_options = b'\202\323\344\223\002\r\022\013/index/info'
  _globals['_INDEX'].methods_by_name['IndexDetail']._loaded_options = None
  _globals['_INDEX'].methods_by_name['IndexDetail']._serialized_options = b'\202\323\344\223\002\017\022\r/index/detail'
  _globals['_INDEX'].methods_by_name['IndexStatistics']._loaded_options = None
  _globals['_INDEX'].methods_by_name['IndexStatistics']._serialized_options = b'\202\323\344\223\002\023\022\021/index/statistics'
  _globals['_INDEX'].methods_by_name['IndexStatisticsDetail']._loaded_options = None
  _globals['_INDEX'].methods_by_name['IndexStatisticsDetail']._serialized_options = b'\202\323\344\223\002\032\022\030/index/statistics/detail'
  _globals['_INDEX'].methods_by_name['IndexProperty']._loaded_options = None
  _globals['_INDEX'].methods_by_name['IndexProperty']._serialized_options = b'\202\323\344\223\002\021\022\017/index/property'
  _globals['_INDEX']._serialized_start=99
  _globals['_INDEX']._serialized_end=596
# @@protoc_insertion_point(module_scope)
