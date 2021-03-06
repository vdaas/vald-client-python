# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vald/v1/vald/search.proto
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
  name='vald/v1/vald/search.proto',
  package='vald.v1',
  syntax='proto3',
  serialized_options=b'\n\032org.vdaas.vald.api.v1.valdB\nValdSearchP\001Z\'github.com/vdaas/vald/apis/grpc/v1/vald\310\342\036\001\320\342\036\001\340\342\036\001\300\343\036\001\310\343\036\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x19vald/v1/vald/search.proto\x12\x07vald.v1\x1a\x1dvald/v1/payload/payload.proto\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto2\xb0\x04\n\x06Search\x12U\n\x06Search\x12\x1a.payload.v1.Search.Request\x1a\x1b.payload.v1.Search.Response\"\x12\x82\xd3\xe4\x93\x02\x0c\"\x07/search:\x01*\x12^\n\nSearchByID\x12\x1c.payload.v1.Search.IDRequest\x1a\x1b.payload.v1.Search.Response\"\x15\x82\xd3\xe4\x93\x02\x0f\"\n/search/id:\x01*\x12S\n\x0cStreamSearch\x12\x1a.payload.v1.Search.Request\x1a!.payload.v1.Search.StreamResponse\"\x00(\x01\x30\x01\x12Y\n\x10StreamSearchByID\x12\x1c.payload.v1.Search.IDRequest\x1a!.payload.v1.Search.StreamResponse\"\x00(\x01\x30\x01\x12i\n\x0bMultiSearch\x12\x1f.payload.v1.Search.MultiRequest\x1a\x1c.payload.v1.Search.Responses\"\x1b\x82\xd3\xe4\x93\x02\x15\"\x10/search/multiple:\x01*\x12T\n\x0fMultiSearchByID\x12!.payload.v1.Search.MultiIDRequest\x1a\x1c.payload.v1.Search.Responses\"\x00\x42g\n\x1aorg.vdaas.vald.api.v1.valdB\nValdSearchP\x01Z\'github.com/vdaas/vald/apis/grpc/v1/vald\xc8\xe2\x1e\x01\xd0\xe2\x1e\x01\xe0\xe2\x1e\x01\xc0\xe3\x1e\x01\xc8\xe3\x1e\x01\x62\x06proto3'
  ,
  dependencies=[vald_dot_v1_dot_payload_dot_payload__pb2.DESCRIPTOR,gogoproto_dot_gogo__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None

_SEARCH = _descriptor.ServiceDescriptor(
  name='Search',
  full_name='vald.v1.Search',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=122,
  serialized_end=682,
  methods=[
  _descriptor.MethodDescriptor(
    name='Search',
    full_name='vald.v1.Search.Search',
    index=0,
    containing_service=None,
    input_type=vald_dot_v1_dot_payload_dot_payload__pb2._SEARCH_REQUEST,
    output_type=vald_dot_v1_dot_payload_dot_payload__pb2._SEARCH_RESPONSE,
    serialized_options=b'\202\323\344\223\002\014\"\007/search:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SearchByID',
    full_name='vald.v1.Search.SearchByID',
    index=1,
    containing_service=None,
    input_type=vald_dot_v1_dot_payload_dot_payload__pb2._SEARCH_IDREQUEST,
    output_type=vald_dot_v1_dot_payload_dot_payload__pb2._SEARCH_RESPONSE,
    serialized_options=b'\202\323\344\223\002\017\"\n/search/id:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='StreamSearch',
    full_name='vald.v1.Search.StreamSearch',
    index=2,
    containing_service=None,
    input_type=vald_dot_v1_dot_payload_dot_payload__pb2._SEARCH_REQUEST,
    output_type=vald_dot_v1_dot_payload_dot_payload__pb2._SEARCH_STREAMRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='StreamSearchByID',
    full_name='vald.v1.Search.StreamSearchByID',
    index=3,
    containing_service=None,
    input_type=vald_dot_v1_dot_payload_dot_payload__pb2._SEARCH_IDREQUEST,
    output_type=vald_dot_v1_dot_payload_dot_payload__pb2._SEARCH_STREAMRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='MultiSearch',
    full_name='vald.v1.Search.MultiSearch',
    index=4,
    containing_service=None,
    input_type=vald_dot_v1_dot_payload_dot_payload__pb2._SEARCH_MULTIREQUEST,
    output_type=vald_dot_v1_dot_payload_dot_payload__pb2._SEARCH_RESPONSES,
    serialized_options=b'\202\323\344\223\002\025\"\020/search/multiple:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='MultiSearchByID',
    full_name='vald.v1.Search.MultiSearchByID',
    index=5,
    containing_service=None,
    input_type=vald_dot_v1_dot_payload_dot_payload__pb2._SEARCH_MULTIIDREQUEST,
    output_type=vald_dot_v1_dot_payload_dot_payload__pb2._SEARCH_RESPONSES,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SEARCH)

DESCRIPTOR.services_by_name['Search'] = _SEARCH

# @@protoc_insertion_point(module_scope)
