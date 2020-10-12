# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vald/v1/vald/remove.proto
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
  name='vald/v1/vald/remove.proto',
  package='vald',
  syntax='proto3',
  serialized_options=b'\n\032org.vdaas.vald.api.v1.valdB\nValdRemoveP\001Z\'github.com/vdaas/vald/apis/grpc/v1/vald',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x19vald/v1/vald/remove.proto\x12\x04vald\x1a\x1dvald/v1/payload/payload.proto\x1a\x1cgoogle/api/annotations.proto2\xda\x01\n\x06Remove\x12=\n\x06Remove\x12\x17.payload.Remove.Request\x1a\x18.payload.Object.Location\"\x00\x12G\n\x0cStreamRemove\x12\x17.payload.Remove.Request\x1a\x18.payload.Object.Location\"\x00(\x01\x30\x01\x12H\n\x0bMultiRemove\x12\x1c.payload.Remove.MultiRequest\x1a\x19.payload.Object.Locations\"\x00\x42S\n\x1aorg.vdaas.vald.api.v1.valdB\nValdRemoveP\x01Z\'github.com/vdaas/vald/apis/grpc/v1/valdb\x06proto3'
  ,
  dependencies=[vald_dot_v1_dot_payload_dot_payload__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None

_REMOVE = _descriptor.ServiceDescriptor(
  name='Remove',
  full_name='vald.Remove',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=97,
  serialized_end=315,
  methods=[
  _descriptor.MethodDescriptor(
    name='Remove',
    full_name='vald.Remove.Remove',
    index=0,
    containing_service=None,
    input_type=vald_dot_v1_dot_payload_dot_payload__pb2._REMOVE_REQUEST,
    output_type=vald_dot_v1_dot_payload_dot_payload__pb2._OBJECT_LOCATION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='StreamRemove',
    full_name='vald.Remove.StreamRemove',
    index=1,
    containing_service=None,
    input_type=vald_dot_v1_dot_payload_dot_payload__pb2._REMOVE_REQUEST,
    output_type=vald_dot_v1_dot_payload_dot_payload__pb2._OBJECT_LOCATION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='MultiRemove',
    full_name='vald.Remove.MultiRemove',
    index=2,
    containing_service=None,
    input_type=vald_dot_v1_dot_payload_dot_payload__pb2._REMOVE_MULTIREQUEST,
    output_type=vald_dot_v1_dot_payload_dot_payload__pb2._OBJECT_LOCATIONS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_REMOVE)

DESCRIPTOR.services_by_name['Remove'] = _REMOVE

# @@protoc_insertion_point(module_scope)
