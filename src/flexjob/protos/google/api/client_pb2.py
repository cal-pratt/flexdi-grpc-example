# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/api/client.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2

from flexjob.protos.google.api import (
    launch_stage_pb2 as google_dot_api_dot_launch__stage__pb2,
)

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x17google/api/client.proto\x12\ngoogle.api\x1a\x1dgoogle/api/launch_stage.proto\x1a google/protobuf/descriptor.proto\x1a\x1egoogle/protobuf/duration.proto"t\n\x16\x43ommonLanguageSettings\x12\x1e\n\x12reference_docs_uri\x18\x01 \x01(\tB\x02\x18\x01\x12:\n\x0c\x64\x65stinations\x18\x02 \x03(\x0e\x32$.google.api.ClientLibraryDestination"\xfb\x03\n\x15\x43lientLibrarySettings\x12\x0f\n\x07version\x18\x01 \x01(\t\x12-\n\x0claunch_stage\x18\x02 \x01(\x0e\x32\x17.google.api.LaunchStage\x12\x1a\n\x12rest_numeric_enums\x18\x03 \x01(\x08\x12/\n\rjava_settings\x18\x15 \x01(\x0b\x32\x18.google.api.JavaSettings\x12-\n\x0c\x63pp_settings\x18\x16 \x01(\x0b\x32\x17.google.api.CppSettings\x12-\n\x0cphp_settings\x18\x17 \x01(\x0b\x32\x17.google.api.PhpSettings\x12\x33\n\x0fpython_settings\x18\x18 \x01(\x0b\x32\x1a.google.api.PythonSettings\x12/\n\rnode_settings\x18\x19 \x01(\x0b\x32\x18.google.api.NodeSettings\x12\x33\n\x0f\x64otnet_settings\x18\x1a \x01(\x0b\x32\x1a.google.api.DotnetSettings\x12/\n\rruby_settings\x18\x1b \x01(\x0b\x32\x18.google.api.RubySettings\x12+\n\x0bgo_settings\x18\x1c \x01(\x0b\x32\x16.google.api.GoSettings"\xfe\x02\n\nPublishing\x12\x33\n\x0fmethod_settings\x18\x02 \x03(\x0b\x32\x1a.google.api.MethodSettings\x12\x15\n\rnew_issue_uri\x18\x65 \x01(\t\x12\x19\n\x11\x64ocumentation_uri\x18\x66 \x01(\t\x12\x16\n\x0e\x61pi_short_name\x18g \x01(\t\x12\x14\n\x0cgithub_label\x18h \x01(\t\x12\x1e\n\x16\x63odeowner_github_teams\x18i \x03(\t\x12\x16\n\x0e\x64oc_tag_prefix\x18j \x01(\t\x12;\n\x0corganization\x18k \x01(\x0e\x32%.google.api.ClientLibraryOrganization\x12;\n\x10library_settings\x18m \x03(\x0b\x32!.google.api.ClientLibrarySettings\x12)\n!proto_reference_documentation_uri\x18n \x01(\t"\xe3\x01\n\x0cJavaSettings\x12\x17\n\x0flibrary_package\x18\x01 \x01(\t\x12L\n\x13service_class_names\x18\x02 \x03(\x0b\x32/.google.api.JavaSettings.ServiceClassNamesEntry\x12\x32\n\x06\x63ommon\x18\x03 \x01(\x0b\x32".google.api.CommonLanguageSettings\x1a\x38\n\x16ServiceClassNamesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"A\n\x0b\x43ppSettings\x12\x32\n\x06\x63ommon\x18\x01 \x01(\x0b\x32".google.api.CommonLanguageSettings"A\n\x0bPhpSettings\x12\x32\n\x06\x63ommon\x18\x01 \x01(\x0b\x32".google.api.CommonLanguageSettings"D\n\x0ePythonSettings\x12\x32\n\x06\x63ommon\x18\x01 \x01(\x0b\x32".google.api.CommonLanguageSettings"B\n\x0cNodeSettings\x12\x32\n\x06\x63ommon\x18\x01 \x01(\x0b\x32".google.api.CommonLanguageSettings"\xaa\x03\n\x0e\x44otnetSettings\x12\x32\n\x06\x63ommon\x18\x01 \x01(\x0b\x32".google.api.CommonLanguageSettings\x12I\n\x10renamed_services\x18\x02 \x03(\x0b\x32/.google.api.DotnetSettings.RenamedServicesEntry\x12K\n\x11renamed_resources\x18\x03 \x03(\x0b\x32\x30.google.api.DotnetSettings.RenamedResourcesEntry\x12\x19\n\x11ignored_resources\x18\x04 \x03(\t\x12 \n\x18\x66orced_namespace_aliases\x18\x05 \x03(\t\x12\x1e\n\x16handwritten_signatures\x18\x06 \x03(\t\x1a\x36\n\x14RenamedServicesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x37\n\x15RenamedResourcesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"B\n\x0cRubySettings\x12\x32\n\x06\x63ommon\x18\x01 \x01(\x0b\x32".google.api.CommonLanguageSettings"@\n\nGoSettings\x12\x32\n\x06\x63ommon\x18\x01 \x01(\x0b\x32".google.api.CommonLanguageSettings"\xb0\x02\n\x0eMethodSettings\x12\x10\n\x08selector\x18\x01 \x01(\t\x12<\n\x0clong_running\x18\x02 \x01(\x0b\x32&.google.api.MethodSettings.LongRunning\x1a\xcd\x01\n\x0bLongRunning\x12\x35\n\x12initial_poll_delay\x18\x01 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x1d\n\x15poll_delay_multiplier\x18\x02 \x01(\x02\x12\x31\n\x0emax_poll_delay\x18\x03 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x35\n\x12total_poll_timeout\x18\x04 \x01(\x0b\x32\x19.google.protobuf.Duration*y\n\x19\x43lientLibraryOrganization\x12+\n\'CLIENT_LIBRARY_ORGANIZATION_UNSPECIFIED\x10\x00\x12\t\n\x05\x43LOUD\x10\x01\x12\x07\n\x03\x41\x44S\x10\x02\x12\n\n\x06PHOTOS\x10\x03\x12\x0f\n\x0bSTREET_VIEW\x10\x04*g\n\x18\x43lientLibraryDestination\x12*\n&CLIENT_LIBRARY_DESTINATION_UNSPECIFIED\x10\x00\x12\n\n\x06GITHUB\x10\n\x12\x13\n\x0fPACKAGE_MANAGER\x10\x14:9\n\x10method_signature\x12\x1e.google.protobuf.MethodOptions\x18\x9b\x08 \x03(\t:6\n\x0c\x64\x65\x66\x61ult_host\x12\x1f.google.protobuf.ServiceOptions\x18\x99\x08 \x01(\t:6\n\x0coauth_scopes\x12\x1f.google.protobuf.ServiceOptions\x18\x9a\x08 \x01(\tBi\n\x0e\x63om.google.apiB\x0b\x43lientProtoP\x01ZAgoogle.golang.org/genproto/googleapis/api/annotations;annotations\xa2\x02\x04GAPIb\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "google.api.client_pb2", globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    google_dot_protobuf_dot_descriptor__pb2.MethodOptions.RegisterExtension(
        method_signature
    )
    google_dot_protobuf_dot_descriptor__pb2.ServiceOptions.RegisterExtension(
        default_host
    )
    google_dot_protobuf_dot_descriptor__pb2.ServiceOptions.RegisterExtension(
        oauth_scopes
    )

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"\n\016com.google.apiB\013ClientProtoP\001ZAgoogle.golang.org/genproto/googleapis/api/annotations;annotations\242\002\004GAPI"
    _COMMONLANGUAGESETTINGS.fields_by_name["reference_docs_uri"]._options = None
    _COMMONLANGUAGESETTINGS.fields_by_name[
        "reference_docs_uri"
    ]._serialized_options = b"\030\001"
    _JAVASETTINGS_SERVICECLASSNAMESENTRY._options = None
    _JAVASETTINGS_SERVICECLASSNAMESENTRY._serialized_options = b"8\001"
    _DOTNETSETTINGS_RENAMEDSERVICESENTRY._options = None
    _DOTNETSETTINGS_RENAMEDSERVICESENTRY._serialized_options = b"8\001"
    _DOTNETSETTINGS_RENAMEDRESOURCESENTRY._options = None
    _DOTNETSETTINGS_RENAMEDRESOURCESENTRY._serialized_options = b"8\001"
    _CLIENTLIBRARYORGANIZATION._serialized_start = 2521
    _CLIENTLIBRARYORGANIZATION._serialized_end = 2642
    _CLIENTLIBRARYDESTINATION._serialized_start = 2644
    _CLIENTLIBRARYDESTINATION._serialized_end = 2747
    _COMMONLANGUAGESETTINGS._serialized_start = 136
    _COMMONLANGUAGESETTINGS._serialized_end = 252
    _CLIENTLIBRARYSETTINGS._serialized_start = 255
    _CLIENTLIBRARYSETTINGS._serialized_end = 762
    _PUBLISHING._serialized_start = 765
    _PUBLISHING._serialized_end = 1147
    _JAVASETTINGS._serialized_start = 1150
    _JAVASETTINGS._serialized_end = 1377
    _JAVASETTINGS_SERVICECLASSNAMESENTRY._serialized_start = 1321
    _JAVASETTINGS_SERVICECLASSNAMESENTRY._serialized_end = 1377
    _CPPSETTINGS._serialized_start = 1379
    _CPPSETTINGS._serialized_end = 1444
    _PHPSETTINGS._serialized_start = 1446
    _PHPSETTINGS._serialized_end = 1511
    _PYTHONSETTINGS._serialized_start = 1513
    _PYTHONSETTINGS._serialized_end = 1581
    _NODESETTINGS._serialized_start = 1583
    _NODESETTINGS._serialized_end = 1649
    _DOTNETSETTINGS._serialized_start = 1652
    _DOTNETSETTINGS._serialized_end = 2078
    _DOTNETSETTINGS_RENAMEDSERVICESENTRY._serialized_start = 1967
    _DOTNETSETTINGS_RENAMEDSERVICESENTRY._serialized_end = 2021
    _DOTNETSETTINGS_RENAMEDRESOURCESENTRY._serialized_start = 2023
    _DOTNETSETTINGS_RENAMEDRESOURCESENTRY._serialized_end = 2078
    _RUBYSETTINGS._serialized_start = 2080
    _RUBYSETTINGS._serialized_end = 2146
    _GOSETTINGS._serialized_start = 2148
    _GOSETTINGS._serialized_end = 2212
    _METHODSETTINGS._serialized_start = 2215
    _METHODSETTINGS._serialized_end = 2519
    _METHODSETTINGS_LONGRUNNING._serialized_start = 2314
    _METHODSETTINGS_LONGRUNNING._serialized_end = 2519
# @@protoc_insertion_point(module_scope)
