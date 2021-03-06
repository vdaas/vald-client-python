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
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='vald/v1/vald/remove.proto',
  package='vald.v1',
  syntax='proto3',
  serialized_options=b'\n\032org.vdaas.vald.api.v1.valdB\nValdRemoveP\001Z\'github.com/vdaas/vald/apis/grpc/v1/vald\310\342\036\001\320\342\036\001\340\342\036\001\300\343\036\001\310\343\036\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x19vald/v1/vald/remove.proto\x12\x07vald.v1\x1a\x1dvald/v1/payload/payload.proto\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto2\x9f\x02\n\x06Remove\x12U\n\x06Remove\x12\x1a.payload.v1.Remove.Request\x1a\x1b.payload.v1.Object.Location\"\x12\x82\xd3\xe4\x93\x02\x0c\"\x07/remove:\x01*\x12S\n\x0cStreamRemove\x12\x1a.payload.v1.Remove.Request\x1a!.payload.v1.Object.StreamLocation\"\x00(\x01\x30\x01\x12i\n\x0bMultiRemove\x12\x1f.payload.v1.Remove.MultiRequest\x1a\x1c.payload.v1.Object.Locations\"\x1b\x82\xd3\xe4\x93\x02\x15\"\x10/remove/multiple:\x01*Bg\n\x1aorg.vdaas.vald.api.v1.valdB\nValdRemoveP\x01Z\'github.com/vdaas/vald/apis/grpc/v1/vald\xc8\xe2\x1e\x01\xd0\xe2\x1e\x01\xe0\xe2\x1e\x01\xc0\xe3\x1e\x01\xc8\xe3\x1e\x01\x62\x06proto3'
  ,
  dependencies=[vald_dot_v1_dot_payload_dot_payload__pb2.DESCRIPTOR,gogoproto_dot_gogo__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None

_REMOVE = _descriptor.ServiceDescriptor(
  name='Remove',
  full_name='vald.v1.Remove',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=122,
  serialized_end=409,
  methods=[
  _descriptor.MethodDescriptor(
    name='Remove',
    full_name='vald.v1.Remove.Remove',
    index=0,
    containing_service=None,
    input_type=vald_dot_v1_dot_payload_dot_payload__pb2._REMOVE_REQUEST,
    output_type=vald_dot_v1_dot_payload_dot_payload__pb2._OBJECT_LOCATION,
    serialized_options=b'\202\323\344\223\002\014\"\007/remove:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='StreamRemove',
    full_name='vald.v1.Remove.StreamRemove',
    index=1,
    containing_service=None,
    input_type=vald_dot_v1_dot_payload_dot_payload__pb2._REMOVE_REQUEST,
    output_type=vald_dot_v1_dot_payload_dot_payload__pb2._OBJECT_STREAMLOCATION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='MultiRemove',
    full_name='vald.v1.Remove.MultiRemove',
    index=2,
    containing_service=None,
    input_type=vald_dot_v1_dot_payload_dot_payload__pb2._REMOVE_MULTIREQUEST,
    output_type=vald_dot_v1_dot_payload_dot_payload__pb2._OBJECT_LOCATIONS,
    serialized_options=b'\202\323\344\223\002\025\"\020/remove/multiple:\001*',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_REMOVE)

DESCRIPTOR.services_by_name['Remove'] = _REMOVE

# @@protoc_insertion_point(module_scope)
