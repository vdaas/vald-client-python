# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vald/v1/vald/filter.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from vald.v1.payload import payload_pb2 as vald_dot_v1_dot_payload_dot_payload__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='vald/v1/vald/filter.proto',
  package='filter',
  syntax='proto3',
  serialized_options=b'\n\032org.vdaas.vald.api.v1.valdB\nValdFilterP\001Z\'github.com/vdaas/vald/apis/grpc/v1/vald',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x19vald/v1/vald/filter.proto\x12\x06\x66ilter\x1a\x1dvald/v1/payload/payload.proto\x1a\x1cgoogle/api/annotations.proto2\x8e\x07\n\x06\x46ilter\x12\x62\n\x0cSearchObject\x12\x1d.payload.Search.ObjectRequest\x1a\x18.payload.Search.Response\"\x19\x82\xd3\xe4\x93\x02\x13\"\x0e/search/object:\x01*\x12S\n\x12StreamSearchObject\x12\x1d.payload.Search.ObjectRequest\x1a\x18.payload.Search.Response\"\x00(\x01\x30\x01\x12Y\n\x0cInsertObject\x12\x14.payload.Object.Blob\x1a\x18.payload.Object.Location\"\x19\x82\xd3\xe4\x93\x02\x13\"\x0e/insert/object:\x01*\x12J\n\x12StreamInsertObject\x12\x14.payload.Object.Blob\x1a\x18.payload.Object.Location\"\x00(\x01\x30\x01\x12\x46\n\x11MultiInsertObject\x12\x14.payload.Object.Blob\x1a\x19.payload.Object.Locations\"\x00\x12Y\n\x0cUpdateObject\x12\x14.payload.Object.Blob\x1a\x18.payload.Object.Location\"\x19\x82\xd3\xe4\x93\x02\x13\"\x0e/update/object:\x01*\x12J\n\x12StreamUpdateObject\x12\x14.payload.Object.Blob\x1a\x18.payload.Object.Location\"\x00(\x01\x30\x01\x12\x46\n\x11MultiUpdateObject\x12\x14.payload.Object.Blob\x1a\x19.payload.Object.Locations\"\x00\x12Y\n\x0cUpsertObject\x12\x14.payload.Object.Blob\x1a\x18.payload.Object.Location\"\x19\x82\xd3\xe4\x93\x02\x13\"\x0e/upsert/object:\x01*\x12J\n\x12StreamUpsertObject\x12\x14.payload.Object.Blob\x1a\x18.payload.Object.Location\"\x00(\x01\x30\x01\x12\x46\n\x11MultiUpsertObject\x12\x14.payload.Object.Blob\x1a\x19.payload.Object.Locations\"\x00\x42S\n\x1aorg.vdaas.vald.api.v1.valdB\nValdFilterP\x01Z\'github.com/vdaas/vald/apis/grpc/v1/valdb\x06proto3'
  ,
  dependencies=[vald_dot_v1_dot_payload_dot_payload__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None

_FILTER = _descriptor.ServiceDescriptor(
  name='Filter',
  full_name='filter.Filter',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=99,
  serialized_end=1009,
  methods=[
  _descriptor.MethodDescriptor(
    name='SearchObject',
    full_name='filter.Filter.SearchObject',
    index=0,
    containing_service=None,
    input_type=vald_dot_v1_dot_payload_dot_payload__pb2._SEARCH_OBJECTREQUEST,
    output_type=vald_dot_v1_dot_payload_dot_payload__pb2._SEARCH_RESPONSE,
    serialized_options=b'\202\323\344\223\002\023\"\016/search/object:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='StreamSearchObject',
    full_name='filter.Filter.StreamSearchObject',
    index=1,
    containing_service=None,
    input_type=vald_dot_v1_dot_payload_dot_payload__pb2._SEARCH_OBJECTREQUEST,
    output_type=vald_dot_v1_dot_payload_dot_payload__pb2._SEARCH_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='InsertObject',
    full_name='filter.Filter.InsertObject',
    index=2,
    containing_service=None,
    input_type=vald_dot_v1_dot_payload_dot_payload__pb2._OBJECT_BLOB,
    output_type=vald_dot_v1_dot_payload_dot_payload__pb2._OBJECT_LOCATION,
    serialized_options=b'\202\323\344\223\002\023\"\016/insert/object:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='StreamInsertObject',
    full_name='filter.Filter.StreamInsertObject',
    index=3,
    containing_service=None,
    input_type=vald_dot_v1_dot_payload_dot_payload__pb2._OBJECT_BLOB,
    output_type=vald_dot_v1_dot_payload_dot_payload__pb2._OBJECT_LOCATION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='MultiInsertObject',
    full_name='filter.Filter.MultiInsertObject',
    index=4,
    containing_service=None,
    input_type=vald_dot_v1_dot_payload_dot_payload__pb2._OBJECT_BLOB,
    output_type=vald_dot_v1_dot_payload_dot_payload__pb2._OBJECT_LOCATIONS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateObject',
    full_name='filter.Filter.UpdateObject',
    index=5,
    containing_service=None,
    input_type=vald_dot_v1_dot_payload_dot_payload__pb2._OBJECT_BLOB,
    output_type=vald_dot_v1_dot_payload_dot_payload__pb2._OBJECT_LOCATION,
    serialized_options=b'\202\323\344\223\002\023\"\016/update/object:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='StreamUpdateObject',
    full_name='filter.Filter.StreamUpdateObject',
    index=6,
    containing_service=None,
    input_type=vald_dot_v1_dot_payload_dot_payload__pb2._OBJECT_BLOB,
    output_type=vald_dot_v1_dot_payload_dot_payload__pb2._OBJECT_LOCATION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='MultiUpdateObject',
    full_name='filter.Filter.MultiUpdateObject',
    index=7,
    containing_service=None,
    input_type=vald_dot_v1_dot_payload_dot_payload__pb2._OBJECT_BLOB,
    output_type=vald_dot_v1_dot_payload_dot_payload__pb2._OBJECT_LOCATIONS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UpsertObject',
    full_name='filter.Filter.UpsertObject',
    index=8,
    containing_service=None,
    input_type=vald_dot_v1_dot_payload_dot_payload__pb2._OBJECT_BLOB,
    output_type=vald_dot_v1_dot_payload_dot_payload__pb2._OBJECT_LOCATION,
    serialized_options=b'\202\323\344\223\002\023\"\016/upsert/object:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='StreamUpsertObject',
    full_name='filter.Filter.StreamUpsertObject',
    index=9,
    containing_service=None,
    input_type=vald_dot_v1_dot_payload_dot_payload__pb2._OBJECT_BLOB,
    output_type=vald_dot_v1_dot_payload_dot_payload__pb2._OBJECT_LOCATION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='MultiUpsertObject',
    full_name='filter.Filter.MultiUpsertObject',
    index=10,
    containing_service=None,
    input_type=vald_dot_v1_dot_payload_dot_payload__pb2._OBJECT_BLOB,
    output_type=vald_dot_v1_dot_payload_dot_payload__pb2._OBJECT_LOCATIONS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_FILTER)

DESCRIPTOR.services_by_name['Filter'] = _FILTER

# @@protoc_insertion_point(module_scope)