# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: serv.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='serv.proto',
  package='serv',
  syntax='proto3',
  serialized_options=b'\n\007ex.grpc',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\nserv.proto\x12\x04serv\"\"\n\x07\x63onInfo\x12\x0b\n\x03\x61\x64r\x18\x01 \x01(\t\x12\n\n\x02ID\x18\x02 \x01(\t\"\x1a\n\x06\x63onRes\x12\x10\n\x08response\x18\x01 \x01(\t\"B\n\x07pubInfo\x12\x0b\n\x03\x61\x64r\x18\x01 \x01(\t\x12\r\n\x05topic\x18\x02 \x01(\t\x12\x0f\n\x07message\x18\x03 \x01(\t\x12\n\n\x02ID\x18\x04 \x01(\t\"\x15\n\x06pubRes\x12\x0b\n\x03res\x18\x01 \x01(\t\"\"\n\x07\x64isInfo\x12\x0b\n\x03\x61\x64r\x18\x01 \x01(\t\x12\n\n\x02ID\x18\x02 \x01(\t\"\x15\n\x06\x64isRes\x12\x0b\n\x03res\x18\x01 \x01(\t\"1\n\x07subInfo\x12\x0b\n\x03\x61\x64r\x18\x01 \x01(\t\x12\r\n\x05topic\x18\x02 \x01(\t\x12\n\n\x02ID\x18\x03 \x01(\t\"\x15\n\x06subRes\x12\x0b\n\x03res\x18\x01 \x01(\t2\xbb\x01\n\x0cMqttservices\x12(\n\x07\x63onnect\x12\r.serv.conInfo\x1a\x0c.serv.conRes\"\x00\x12(\n\x07publish\x12\r.serv.pubInfo\x1a\x0c.serv.pubRes\"\x00\x12+\n\ndisconnect\x12\r.serv.disInfo\x1a\x0c.serv.disRes\"\x00\x12*\n\tsubscribe\x12\r.serv.subInfo\x1a\x0c.serv.subRes\"\x00\x42\t\n\x07\x65x.grpcb\x06proto3'
)




_CONINFO = _descriptor.Descriptor(
  name='conInfo',
  full_name='serv.conInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='adr', full_name='serv.conInfo.adr', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ID', full_name='serv.conInfo.ID', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=20,
  serialized_end=54,
)


_CONRES = _descriptor.Descriptor(
  name='conRes',
  full_name='serv.conRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='response', full_name='serv.conRes.response', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=56,
  serialized_end=82,
)


_PUBINFO = _descriptor.Descriptor(
  name='pubInfo',
  full_name='serv.pubInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='adr', full_name='serv.pubInfo.adr', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='topic', full_name='serv.pubInfo.topic', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='serv.pubInfo.message', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ID', full_name='serv.pubInfo.ID', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=84,
  serialized_end=150,
)


_PUBRES = _descriptor.Descriptor(
  name='pubRes',
  full_name='serv.pubRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='res', full_name='serv.pubRes.res', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=152,
  serialized_end=173,
)


_DISINFO = _descriptor.Descriptor(
  name='disInfo',
  full_name='serv.disInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='adr', full_name='serv.disInfo.adr', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ID', full_name='serv.disInfo.ID', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=175,
  serialized_end=209,
)


_DISRES = _descriptor.Descriptor(
  name='disRes',
  full_name='serv.disRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='res', full_name='serv.disRes.res', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=211,
  serialized_end=232,
)


_SUBINFO = _descriptor.Descriptor(
  name='subInfo',
  full_name='serv.subInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='adr', full_name='serv.subInfo.adr', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='topic', full_name='serv.subInfo.topic', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ID', full_name='serv.subInfo.ID', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=234,
  serialized_end=283,
)


_SUBRES = _descriptor.Descriptor(
  name='subRes',
  full_name='serv.subRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='res', full_name='serv.subRes.res', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=285,
  serialized_end=306,
)

DESCRIPTOR.message_types_by_name['conInfo'] = _CONINFO
DESCRIPTOR.message_types_by_name['conRes'] = _CONRES
DESCRIPTOR.message_types_by_name['pubInfo'] = _PUBINFO
DESCRIPTOR.message_types_by_name['pubRes'] = _PUBRES
DESCRIPTOR.message_types_by_name['disInfo'] = _DISINFO
DESCRIPTOR.message_types_by_name['disRes'] = _DISRES
DESCRIPTOR.message_types_by_name['subInfo'] = _SUBINFO
DESCRIPTOR.message_types_by_name['subRes'] = _SUBRES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

conInfo = _reflection.GeneratedProtocolMessageType('conInfo', (_message.Message,), {
  'DESCRIPTOR' : _CONINFO,
  '__module__' : 'serv_pb2'
  # @@protoc_insertion_point(class_scope:serv.conInfo)
  })
_sym_db.RegisterMessage(conInfo)

conRes = _reflection.GeneratedProtocolMessageType('conRes', (_message.Message,), {
  'DESCRIPTOR' : _CONRES,
  '__module__' : 'serv_pb2'
  # @@protoc_insertion_point(class_scope:serv.conRes)
  })
_sym_db.RegisterMessage(conRes)

pubInfo = _reflection.GeneratedProtocolMessageType('pubInfo', (_message.Message,), {
  'DESCRIPTOR' : _PUBINFO,
  '__module__' : 'serv_pb2'
  # @@protoc_insertion_point(class_scope:serv.pubInfo)
  })
_sym_db.RegisterMessage(pubInfo)

pubRes = _reflection.GeneratedProtocolMessageType('pubRes', (_message.Message,), {
  'DESCRIPTOR' : _PUBRES,
  '__module__' : 'serv_pb2'
  # @@protoc_insertion_point(class_scope:serv.pubRes)
  })
_sym_db.RegisterMessage(pubRes)

disInfo = _reflection.GeneratedProtocolMessageType('disInfo', (_message.Message,), {
  'DESCRIPTOR' : _DISINFO,
  '__module__' : 'serv_pb2'
  # @@protoc_insertion_point(class_scope:serv.disInfo)
  })
_sym_db.RegisterMessage(disInfo)

disRes = _reflection.GeneratedProtocolMessageType('disRes', (_message.Message,), {
  'DESCRIPTOR' : _DISRES,
  '__module__' : 'serv_pb2'
  # @@protoc_insertion_point(class_scope:serv.disRes)
  })
_sym_db.RegisterMessage(disRes)

subInfo = _reflection.GeneratedProtocolMessageType('subInfo', (_message.Message,), {
  'DESCRIPTOR' : _SUBINFO,
  '__module__' : 'serv_pb2'
  # @@protoc_insertion_point(class_scope:serv.subInfo)
  })
_sym_db.RegisterMessage(subInfo)

subRes = _reflection.GeneratedProtocolMessageType('subRes', (_message.Message,), {
  'DESCRIPTOR' : _SUBRES,
  '__module__' : 'serv_pb2'
  # @@protoc_insertion_point(class_scope:serv.subRes)
  })
_sym_db.RegisterMessage(subRes)


DESCRIPTOR._options = None

_MQTTSERVICES = _descriptor.ServiceDescriptor(
  name='Mqttservices',
  full_name='serv.Mqttservices',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=309,
  serialized_end=496,
  methods=[
  _descriptor.MethodDescriptor(
    name='connect',
    full_name='serv.Mqttservices.connect',
    index=0,
    containing_service=None,
    input_type=_CONINFO,
    output_type=_CONRES,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='publish',
    full_name='serv.Mqttservices.publish',
    index=1,
    containing_service=None,
    input_type=_PUBINFO,
    output_type=_PUBRES,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='disconnect',
    full_name='serv.Mqttservices.disconnect',
    index=2,
    containing_service=None,
    input_type=_DISINFO,
    output_type=_DISRES,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='subscribe',
    full_name='serv.Mqttservices.subscribe',
    index=3,
    containing_service=None,
    input_type=_SUBINFO,
    output_type=_SUBRES,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MQTTSERVICES)

DESCRIPTOR.services_by_name['Mqttservices'] = _MQTTSERVICES

# @@protoc_insertion_point(module_scope)
