# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/bigquery/storage/v1beta1/arrow.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/bigquery/storage/v1beta1/arrow.proto',
  package='google.cloud.bigquery.storage.v1beta1',
  syntax='proto3',
  serialized_options=_b('\n)com.google.cloud.bigquery.storage.v1beta1B\nArrowProtoZLgoogle.golang.org/genproto/googleapis/cloud/bigquery/storage/v1beta1;storage'),
  serialized_pb=_b('\n1google/cloud/bigquery/storage/v1beta1/arrow.proto\x12%google.cloud.bigquery.storage.v1beta1\"(\n\x0b\x41rrowSchema\x12\x19\n\x11serialized_schema\x18\x01 \x01(\x0c\"F\n\x10\x41rrowRecordBatch\x12\x1f\n\x17serialized_record_batch\x18\x01 \x01(\x0c\x12\x11\n\trow_count\x18\x02 \x01(\x03\x42\x85\x01\n)com.google.cloud.bigquery.storage.v1beta1B\nArrowProtoZLgoogle.golang.org/genproto/googleapis/cloud/bigquery/storage/v1beta1;storageb\x06proto3')
)




_ARROWSCHEMA = _descriptor.Descriptor(
  name='ArrowSchema',
  full_name='google.cloud.bigquery.storage.v1beta1.ArrowSchema',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='serialized_schema', full_name='google.cloud.bigquery.storage.v1beta1.ArrowSchema.serialized_schema', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=92,
  serialized_end=132,
)


_ARROWRECORDBATCH = _descriptor.Descriptor(
  name='ArrowRecordBatch',
  full_name='google.cloud.bigquery.storage.v1beta1.ArrowRecordBatch',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='serialized_record_batch', full_name='google.cloud.bigquery.storage.v1beta1.ArrowRecordBatch.serialized_record_batch', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='row_count', full_name='google.cloud.bigquery.storage.v1beta1.ArrowRecordBatch.row_count', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=134,
  serialized_end=204,
)

DESCRIPTOR.message_types_by_name['ArrowSchema'] = _ARROWSCHEMA
DESCRIPTOR.message_types_by_name['ArrowRecordBatch'] = _ARROWRECORDBATCH
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ArrowSchema = _reflection.GeneratedProtocolMessageType('ArrowSchema', (_message.Message,), {
  'DESCRIPTOR' : _ARROWSCHEMA,
  '__module__' : 'google.cloud.bigquery.storage.v1beta1.arrow_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.bigquery.storage.v1beta1.ArrowSchema)
  })
_sym_db.RegisterMessage(ArrowSchema)

ArrowRecordBatch = _reflection.GeneratedProtocolMessageType('ArrowRecordBatch', (_message.Message,), {
  'DESCRIPTOR' : _ARROWRECORDBATCH,
  '__module__' : 'google.cloud.bigquery.storage.v1beta1.arrow_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.bigquery.storage.v1beta1.ArrowRecordBatch)
  })
_sym_db.RegisterMessage(ArrowRecordBatch)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)