# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vald/v1/vald/update.proto
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
  name='vald/v1/vald/update.proto',
  package='vald',
  syntax='proto3',
  serialized_options=b'\n\032org.vdaas.vald.api.v1.valdB\nValdUpdateP\001Z\'github.com/vdaas/vald/apis/grpc/v1/vald',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x19vald/v1/vald/update.proto\x12\x04vald\x1a\x1dvald/v1/payload/payload.proto\x1a\x1cgoogle/api/annotations.proto2\xec\x01\n\x06Update\x12O\n\x06Update\x12\x17.payload.Update.Request\x1a\x18.payload.Object.Location\"\x12\x82\xd3\xe4\x93\x02\x0c\"\x07/update:\x01*\x12G\n\x0cStreamUpdate\x12\x17.payload.Update.Request\x1a\x18.payload.Object.Location\"\x00(\x01\x30\x01\x12H\n\x0bMultiUpdate\x12\x1c.payload.Update.MultiRequest\x1a\x19.payload.Object.Locations\"\x00\x42S\n\x1aorg.vdaas.vald.api.v1.valdB\nValdUpdateP\x01Z\'github.com/vdaas/vald/apis/grpc/v1/valdb\x06proto3'
  ,
  dependencies=[vald_dot_v1_dot_payload_dot_payload__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None

_UPDATE = _descriptor.ServiceDescriptor(
  name='Update',
  full_name='vald.Update',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=97,
  serialized_end=333,
  methods=[
  _descriptor.MethodDescriptor(
    name='Update',
    full_name='vald.Update.Update',
    index=0,
    containing_service=None,
    input_type=vald_dot_v1_dot_payload_dot_payload__pb2._UPDATE_REQUEST,
    output_type=vald_dot_v1_dot_payload_dot_payload__pb2._OBJECT_LOCATION,
    serialized_options=b'\202\323\344\223\002\014\"\007/update:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='StreamUpdate',
    full_name='vald.Update.StreamUpdate',
    index=1,
    containing_service=None,
    input_type=vald_dot_v1_dot_payload_dot_payload__pb2._UPDATE_REQUEST,
    output_type=vald_dot_v1_dot_payload_dot_payload__pb2._OBJECT_LOCATION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='MultiUpdate',
    full_name='vald.Update.MultiUpdate',
    index=2,
    containing_service=None,
    input_type=vald_dot_v1_dot_payload_dot_payload__pb2._UPDATE_MULTIREQUEST,
    output_type=vald_dot_v1_dot_payload_dot_payload__pb2._OBJECT_LOCATIONS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_UPDATE)

DESCRIPTOR.services_by_name['Update'] = _UPDATE

# @@protoc_insertion_point(module_scope)
