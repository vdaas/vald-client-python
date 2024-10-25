# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: vald/v1/rpc/errdetails/error_details.proto
# Protobuf Python Version: 5.28.3
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
    3,
    '',
    'vald/v1/rpc/errdetails/error_details.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*vald/v1/rpc/errdetails/error_details.proto\x12\x06rpc.v1\x1a\x1egoogle/protobuf/duration.proto\"\xb5\x01\n\tErrorInfo\x12\x16\n\x06reason\x18\x01 \x01(\tR\x06reason\x12\x16\n\x06\x64omain\x18\x02 \x01(\tR\x06\x64omain\x12;\n\x08metadata\x18\x03 \x03(\x0b\x32\x1f.rpc.v1.ErrorInfo.MetadataEntryR\x08metadata\x1a;\n\rMetadataEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"G\n\tRetryInfo\x12:\n\x0bretry_delay\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationR\nretryDelay\"H\n\tDebugInfo\x12#\n\rstack_entries\x18\x01 \x03(\tR\x0cstackEntries\x12\x16\n\x06\x64\x65tail\x18\x02 \x01(\tR\x06\x64\x65tail\"\x97\x01\n\x0cQuotaFailure\x12>\n\nviolations\x18\x01 \x03(\x0b\x32\x1e.rpc.v1.QuotaFailure.ViolationR\nviolations\x1aG\n\tViolation\x12\x18\n\x07subject\x18\x01 \x01(\tR\x07subject\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\"\xb9\x01\n\x13PreconditionFailure\x12\x45\n\nviolations\x18\x01 \x03(\x0b\x32%.rpc.v1.PreconditionFailure.ViolationR\nviolations\x1a[\n\tViolation\x12\x12\n\x04type\x18\x01 \x01(\tR\x04type\x12\x18\n\x07subject\x18\x02 \x01(\tR\x07subject\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\"\xa4\x01\n\nBadRequest\x12L\n\x10\x66ield_violations\x18\x01 \x03(\x0b\x32!.rpc.v1.BadRequest.FieldViolationR\x0f\x66ieldViolations\x1aH\n\x0e\x46ieldViolation\x12\x14\n\x05\x66ield\x18\x01 \x01(\tR\x05\x66ield\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\"O\n\x0bRequestInfo\x12\x1d\n\nrequest_id\x18\x01 \x01(\tR\trequestId\x12!\n\x0cserving_data\x18\x02 \x01(\tR\x0bservingData\"\x90\x01\n\x0cResourceInfo\x12#\n\rresource_type\x18\x01 \x01(\tR\x0cresourceType\x12#\n\rresource_name\x18\x02 \x01(\tR\x0cresourceName\x12\x14\n\x05owner\x18\x03 \x01(\tR\x05owner\x12 \n\x0b\x64\x65scription\x18\x04 \x01(\tR\x0b\x64\x65scription\"k\n\x04Help\x12\'\n\x05links\x18\x01 \x03(\x0b\x32\x11.rpc.v1.Help.LinkR\x05links\x1a:\n\x04Link\x12 \n\x0b\x64\x65scription\x18\x01 \x01(\tR\x0b\x64\x65scription\x12\x10\n\x03url\x18\x02 \x01(\tR\x03url\"D\n\x10LocalizedMessage\x12\x16\n\x06locale\x18\x01 \x01(\tR\x06locale\x12\x18\n\x07message\x18\x02 \x01(\tR\x07messageBi\n\x19org.vdaas.vald.api.v1.rpcB\x11\x45rrorDetailsProtoP\x01Z1github.com/vdaas/vald/apis/grpc/v1/rpc/errdetails\xa2\x02\x03RPCb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'vald.v1.rpc.errdetails.error_details_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031org.vdaas.vald.api.v1.rpcB\021ErrorDetailsProtoP\001Z1github.com/vdaas/vald/apis/grpc/v1/rpc/errdetails\242\002\003RPC'
  _globals['_ERRORINFO_METADATAENTRY']._loaded_options = None
  _globals['_ERRORINFO_METADATAENTRY']._serialized_options = b'8\001'
  _globals['_ERRORINFO']._serialized_start=87
  _globals['_ERRORINFO']._serialized_end=268
  _globals['_ERRORINFO_METADATAENTRY']._serialized_start=209
  _globals['_ERRORINFO_METADATAENTRY']._serialized_end=268
  _globals['_RETRYINFO']._serialized_start=270
  _globals['_RETRYINFO']._serialized_end=341
  _globals['_DEBUGINFO']._serialized_start=343
  _globals['_DEBUGINFO']._serialized_end=415
  _globals['_QUOTAFAILURE']._serialized_start=418
  _globals['_QUOTAFAILURE']._serialized_end=569
  _globals['_QUOTAFAILURE_VIOLATION']._serialized_start=498
  _globals['_QUOTAFAILURE_VIOLATION']._serialized_end=569
  _globals['_PRECONDITIONFAILURE']._serialized_start=572
  _globals['_PRECONDITIONFAILURE']._serialized_end=757
  _globals['_PRECONDITIONFAILURE_VIOLATION']._serialized_start=666
  _globals['_PRECONDITIONFAILURE_VIOLATION']._serialized_end=757
  _globals['_BADREQUEST']._serialized_start=760
  _globals['_BADREQUEST']._serialized_end=924
  _globals['_BADREQUEST_FIELDVIOLATION']._serialized_start=852
  _globals['_BADREQUEST_FIELDVIOLATION']._serialized_end=924
  _globals['_REQUESTINFO']._serialized_start=926
  _globals['_REQUESTINFO']._serialized_end=1005
  _globals['_RESOURCEINFO']._serialized_start=1008
  _globals['_RESOURCEINFO']._serialized_end=1152
  _globals['_HELP']._serialized_start=1154
  _globals['_HELP']._serialized_end=1261
  _globals['_HELP_LINK']._serialized_start=1203
  _globals['_HELP_LINK']._serialized_end=1261
  _globals['_LOCALIZEDMESSAGE']._serialized_start=1263
  _globals['_LOCALIZEDMESSAGE']._serialized_end=1331
# @@protoc_insertion_point(module_scope)
