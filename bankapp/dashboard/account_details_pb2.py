# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: account_details.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x61\x63\x63ount_details.proto\"a\n\x07\x41\x63\x63ount\x12\x16\n\x0e\x61\x63\x63ount_number\x18\x01 \x01(\t\x12\x1b\n\x13\x61\x63\x63ount_holder_name\x18\x02 \x01(\t\x12\x0f\n\x07\x62\x61lance\x18\x03 \x01(\x01\x12\x10\n\x08\x63urrency\x18\x04 \x01(\t\"2\n\x18GetAccountDetailsRequest\x12\x16\n\x0e\x61\x63\x63ount_number\x18\x01 \x01(\t\"6\n\x19GetAccountDetailsResponse\x12\x19\n\x07\x61\x63\x63ount\x18\x01 \x01(\x0b\x32\x08.Account2c\n\x15\x41\x63\x63ountDetailsService\x12J\n\x11GetAccountDetails\x12\x19.GetAccountDetailsRequest\x1a\x1a.GetAccountDetailsResponseb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'account_details_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ACCOUNT._serialized_start=25
  _ACCOUNT._serialized_end=122
  _GETACCOUNTDETAILSREQUEST._serialized_start=124
  _GETACCOUNTDETAILSREQUEST._serialized_end=174
  _GETACCOUNTDETAILSRESPONSE._serialized_start=176
  _GETACCOUNTDETAILSRESPONSE._serialized_end=230
  _ACCOUNTDETAILSSERVICE._serialized_start=232
  _ACCOUNTDETAILSSERVICE._serialized_end=331
# @@protoc_insertion_point(module_scope)
