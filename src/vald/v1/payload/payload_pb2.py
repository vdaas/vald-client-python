# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: vald/v1/payload/payload.proto
# Protobuf Python Version: 6.31.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    6,
    31,
    1,
    '',
    'vald/v1/payload/payload.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from buf.validate import validate_pb2 as buf_dot_validate_dot_validate__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dvald/v1/payload/payload.proto\x12\npayload.v1\x1a\x1b\x62uf/validate/validate.proto\x1a\x19google/protobuf/any.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x17google/rpc/status.proto\"\xb8\x0b\n\x06Search\x1a^\n\x07Request\x12 \n\x06vector\x18\x01 \x03(\x02\x42\x08\xbaH\x05\x92\x01\x02\x08\x02R\x06vector\x12\x31\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x19.payload.v1.Search.ConfigR\x06\x63onfig\x1a\x46\n\x0cMultiRequest\x12\x36\n\x08requests\x18\x01 \x03(\x0b\x32\x1a.payload.v1.Search.RequestR\x08requests\x1aN\n\tIDRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x31\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x19.payload.v1.Search.ConfigR\x06\x63onfig\x1aJ\n\x0eMultiIDRequest\x12\x38\n\x08requests\x18\x01 \x03(\x0b\x32\x1c.payload.v1.Search.IDRequestR\x08requests\x1a\x95\x01\n\rObjectRequest\x12\x16\n\x06object\x18\x01 \x01(\x0cR\x06object\x12\x31\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x19.payload.v1.Search.ConfigR\x06\x63onfig\x12\x39\n\nvectorizer\x18\x03 \x01(\x0b\x32\x19.payload.v1.Filter.TargetR\nvectorizer\x1aR\n\x12MultiObjectRequest\x12<\n\x08requests\x18\x01 \x03(\x0b\x32 .payload.v1.Search.ObjectRequestR\x08requests\x1a\xdf\x03\n\x06\x43onfig\x12\x1d\n\nrequest_id\x18\x01 \x01(\tR\trequestId\x12\x19\n\x03num\x18\x02 \x01(\rB\x07\xbaH\x04*\x02(\x01R\x03num\x12\x16\n\x06radius\x18\x03 \x01(\x02R\x06radius\x12\x18\n\x07\x65psilon\x18\x04 \x01(\x02R\x07\x65psilon\x12\x18\n\x07timeout\x18\x05 \x01(\x03R\x07timeout\x12\x42\n\x0fingress_filters\x18\x06 \x01(\x0b\x32\x19.payload.v1.Filter.ConfigR\x0eingressFilters\x12@\n\x0e\x65gress_filters\x18\x07 \x01(\x0b\x32\x19.payload.v1.Filter.ConfigR\regressFilters\x12 \n\x07min_num\x18\x08 \x01(\rB\x07\xbaH\x04*\x02(\x00R\x06minNum\x12\\\n\x15\x61ggregation_algorithm\x18\t \x01(\x0e\x32\'.payload.v1.Search.AggregationAlgorithmR\x14\x61ggregationAlgorithm\x12\x31\n\x05ratio\x18\n \x01(\x0b\x32\x1b.google.protobuf.FloatValueR\x05ratio\x12\x16\n\x06nprobe\x18\x0b \x01(\rR\x06nprobe\x1a`\n\x08Response\x12\x1d\n\nrequest_id\x18\x01 \x01(\tR\trequestId\x12\x35\n\x07results\x18\x02 \x03(\x0b\x32\x1b.payload.v1.Object.DistanceR\x07results\x1a\x46\n\tResponses\x12\x39\n\tresponses\x18\x01 \x03(\x0b\x32\x1b.payload.v1.Search.ResponseR\tresponses\x1a\x84\x01\n\x0eStreamResponse\x12\x39\n\x08response\x18\x01 \x01(\x0b\x32\x1b.payload.v1.Search.ResponseH\x00R\x08response\x12,\n\x06status\x18\x02 \x01(\x0b\x32\x12.google.rpc.StatusH\x00R\x06statusB\t\n\x07payload\"k\n\x14\x41ggregationAlgorithm\x12\x0b\n\x07Unknown\x10\x00\x12\x13\n\x0f\x43oncurrentQueue\x10\x01\x12\r\n\tSortSlice\x10\x02\x12\x11\n\rSortPoolSlice\x10\x03\x12\x0f\n\x0bPairingHeap\x10\x04\"y\n\x06\x46ilter\x1a\x30\n\x06Target\x12\x12\n\x04host\x18\x01 \x01(\tR\x04host\x12\x12\n\x04port\x18\x02 \x01(\rR\x04port\x1a=\n\x06\x43onfig\x12\x33\n\x07targets\x18\x01 \x03(\x0b\x32\x19.payload.v1.Filter.TargetR\x07targets\"\xe5\x04\n\x06Insert\x1ay\n\x07Request\x12;\n\x06vector\x18\x01 \x01(\x0b\x32\x19.payload.v1.Object.VectorB\x08\xbaH\x05\x92\x01\x02\x08\x02R\x06vector\x12\x31\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x19.payload.v1.Insert.ConfigR\x06\x63onfig\x1a\x46\n\x0cMultiRequest\x12\x36\n\x08requests\x18\x01 \x03(\x0b\x32\x1a.payload.v1.Insert.RequestR\x08requests\x1a\xae\x01\n\rObjectRequest\x12/\n\x06object\x18\x01 \x01(\x0b\x32\x17.payload.v1.Object.BlobR\x06object\x12\x31\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x19.payload.v1.Insert.ConfigR\x06\x63onfig\x12\x39\n\nvectorizer\x18\x03 \x01(\x0b\x32\x19.payload.v1.Filter.TargetR\nvectorizer\x1aR\n\x12MultiObjectRequest\x12<\n\x08requests\x18\x01 \x03(\x0b\x32 .payload.v1.Insert.ObjectRequestR\x08requests\x1a\x92\x01\n\x06\x43onfig\x12\x35\n\x17skip_strict_exist_check\x18\x01 \x01(\x08R\x14skipStrictExistCheck\x12\x33\n\x07\x66ilters\x18\x02 \x01(\x0b\x32\x19.payload.v1.Filter.ConfigR\x07\x66ilters\x12\x1c\n\ttimestamp\x18\x03 \x01(\x03R\ttimestamp\"\xfe\x05\n\x06Update\x1ay\n\x07Request\x12;\n\x06vector\x18\x01 \x01(\x0b\x32\x19.payload.v1.Object.VectorB\x08\xbaH\x05\x92\x01\x02\x08\x02R\x06vector\x12\x31\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x19.payload.v1.Update.ConfigR\x06\x63onfig\x1a\x46\n\x0cMultiRequest\x12\x36\n\x08requests\x18\x01 \x03(\x0b\x32\x1a.payload.v1.Update.RequestR\x08requests\x1a\xae\x01\n\rObjectRequest\x12/\n\x06object\x18\x01 \x01(\x0b\x32\x17.payload.v1.Object.BlobR\x06object\x12\x31\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x19.payload.v1.Update.ConfigR\x06\x63onfig\x12\x39\n\nvectorizer\x18\x03 \x01(\x0b\x32\x19.payload.v1.Filter.TargetR\nvectorizer\x1aR\n\x12MultiObjectRequest\x12<\n\x08requests\x18\x01 \x03(\x0b\x32 .payload.v1.Update.ObjectRequestR\x08requests\x1a_\n\x10TimestampRequest\x12\x17\n\x02id\x18\x01 \x01(\tB\x07\xbaH\x04r\x02\x10\x01R\x02id\x12\x1c\n\ttimestamp\x18\x02 \x01(\x03R\ttimestamp\x12\x14\n\x05\x66orce\x18\x03 \x01(\x08R\x05\x66orce\x1a\xca\x01\n\x06\x43onfig\x12\x35\n\x17skip_strict_exist_check\x18\x01 \x01(\x08R\x14skipStrictExistCheck\x12\x33\n\x07\x66ilters\x18\x02 \x01(\x0b\x32\x19.payload.v1.Filter.ConfigR\x07\x66ilters\x12\x1c\n\ttimestamp\x18\x03 \x01(\x03R\ttimestamp\x12\x36\n\x17\x64isable_balanced_update\x18\x04 \x01(\x08R\x15\x64isableBalancedUpdate\"\x9d\x05\n\x06Upsert\x1ay\n\x07Request\x12;\n\x06vector\x18\x01 \x01(\x0b\x32\x19.payload.v1.Object.VectorB\x08\xbaH\x05\x92\x01\x02\x08\x02R\x06vector\x12\x31\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x19.payload.v1.Upsert.ConfigR\x06\x63onfig\x1a\x46\n\x0cMultiRequest\x12\x36\n\x08requests\x18\x01 \x03(\x0b\x32\x1a.payload.v1.Upsert.RequestR\x08requests\x1a\xae\x01\n\rObjectRequest\x12/\n\x06object\x18\x01 \x01(\x0b\x32\x17.payload.v1.Object.BlobR\x06object\x12\x31\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x19.payload.v1.Upsert.ConfigR\x06\x63onfig\x12\x39\n\nvectorizer\x18\x03 \x01(\x0b\x32\x19.payload.v1.Filter.TargetR\nvectorizer\x1aR\n\x12MultiObjectRequest\x12<\n\x08requests\x18\x01 \x03(\x0b\x32 .payload.v1.Upsert.ObjectRequestR\x08requests\x1a\xca\x01\n\x06\x43onfig\x12\x35\n\x17skip_strict_exist_check\x18\x01 \x01(\x08R\x14skipStrictExistCheck\x12\x33\n\x07\x66ilters\x18\x02 \x01(\x0b\x32\x19.payload.v1.Filter.ConfigR\x07\x66ilters\x12\x1c\n\ttimestamp\x18\x03 \x01(\x03R\ttimestamp\x12\x36\n\x17\x64isable_balanced_update\x18\x04 \x01(\x08R\x15\x64isableBalancedUpdate\"\x91\x04\n\x06Remove\x1a\x63\n\x07Request\x12%\n\x02id\x18\x01 \x01(\x0b\x32\x15.payload.v1.Object.IDR\x02id\x12\x31\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x19.payload.v1.Remove.ConfigR\x06\x63onfig\x1a\x46\n\x0cMultiRequest\x12\x36\n\x08requests\x18\x01 \x03(\x0b\x32\x1a.payload.v1.Remove.RequestR\x08requests\x1aP\n\x10TimestampRequest\x12<\n\ntimestamps\x18\x01 \x03(\x0b\x32\x1c.payload.v1.Remove.TimestampR\ntimestamps\x1a\xa8\x01\n\tTimestamp\x12\x1c\n\ttimestamp\x18\x01 \x01(\x03R\ttimestamp\x12\x41\n\x08operator\x18\x02 \x01(\x0e\x32%.payload.v1.Remove.Timestamp.OperatorR\x08operator\":\n\x08Operator\x12\x06\n\x02\x45q\x10\x00\x12\x06\n\x02Ne\x10\x01\x12\x06\n\x02Ge\x10\x02\x12\x06\n\x02Gt\x10\x03\x12\x06\n\x02Le\x10\x04\x12\x06\n\x02Lt\x10\x05\x1a]\n\x06\x43onfig\x12\x35\n\x17skip_strict_exist_check\x18\x01 \x01(\x08R\x14skipStrictExistCheck\x12\x1c\n\ttimestamp\x18\x03 \x01(\x03R\ttimestamp\"\x12\n\x05\x46lush\x1a\t\n\x07Request\"\xb1\x0b\n\x06Object\x1au\n\rVectorRequest\x12/\n\x02id\x18\x01 \x01(\x0b\x32\x15.payload.v1.Object.IDB\x08\xbaH\x05\x92\x01\x02\x08\x02R\x02id\x12\x33\n\x07\x66ilters\x18\x02 \x01(\x0b\x32\x19.payload.v1.Filter.ConfigR\x07\x66ilters\x1a\x36\n\x08\x44istance\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x1a\n\x08\x64istance\x18\x02 \x01(\x02R\x08\x64istance\x1a\x84\x01\n\x0eStreamDistance\x12\x39\n\x08\x64istance\x18\x01 \x01(\x0b\x32\x1b.payload.v1.Object.DistanceH\x00R\x08\x64istance\x12,\n\x06status\x18\x02 \x01(\x0b\x32\x12.google.rpc.StatusH\x00R\x06statusB\t\n\x07payload\x1a\x1d\n\x02ID\x12\x17\n\x02id\x18\x01 \x01(\tB\x07\xbaH\x04r\x02\x10\x01R\x02id\x1a\x17\n\x03IDs\x12\x10\n\x03ids\x18\x01 \x03(\tR\x03ids\x1a\x61\n\x06Vector\x12\x17\n\x02id\x18\x01 \x01(\tB\x07\xbaH\x04r\x02\x10\x01R\x02id\x12 \n\x06vector\x18\x02 \x03(\x02\x42\x08\xbaH\x05\x92\x01\x02\x08\x02R\x06vector\x12\x1c\n\ttimestamp\x18\x03 \x01(\x03R\ttimestamp\x1a\x43\n\x10TimestampRequest\x12/\n\x02id\x18\x01 \x01(\x0b\x32\x15.payload.v1.Object.IDB\x08\xbaH\x05\x92\x01\x02\x08\x02R\x02id\x1a\x42\n\tTimestamp\x12\x17\n\x02id\x18\x01 \x01(\tB\x07\xbaH\x04r\x02\x10\x01R\x02id\x12\x1c\n\ttimestamp\x18\x02 \x01(\x03R\ttimestamp\x1a>\n\x07Vectors\x12\x33\n\x07vectors\x18\x01 \x03(\x0b\x32\x19.payload.v1.Object.VectorR\x07vectors\x1a|\n\x0cStreamVector\x12\x33\n\x06vector\x18\x01 \x01(\x0b\x32\x19.payload.v1.Object.VectorH\x00R\x06vector\x12,\n\x06status\x18\x02 \x01(\x0b\x32\x12.google.rpc.StatusH\x00R\x06statusB\t\n\x07payload\x1a=\n\rReshapeVector\x12\x16\n\x06object\x18\x01 \x01(\x0cR\x06object\x12\x14\n\x05shape\x18\x02 \x03(\x05R\x05shape\x1a\x37\n\x04\x42lob\x12\x17\n\x02id\x18\x01 \x01(\tB\x07\xbaH\x04r\x02\x10\x01R\x02id\x12\x16\n\x06object\x18\x02 \x01(\x0cR\x06object\x1at\n\nStreamBlob\x12-\n\x04\x62lob\x18\x01 \x01(\x0b\x32\x17.payload.v1.Object.BlobH\x00R\x04\x62lob\x12,\n\x06status\x18\x02 \x01(\x0b\x32\x12.google.rpc.StatusH\x00R\x06statusB\t\n\x07payload\x1a\x44\n\x08Location\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x12\n\x04uuid\x18\x02 \x01(\tR\x04uuid\x12\x10\n\x03ips\x18\x03 \x03(\tR\x03ips\x1a\x84\x01\n\x0eStreamLocation\x12\x39\n\x08location\x18\x01 \x01(\x0b\x32\x1b.payload.v1.Object.LocationH\x00R\x08location\x12,\n\x06status\x18\x02 \x01(\x0b\x32\x12.google.rpc.StatusH\x00R\x06statusB\t\n\x07payload\x1a\x46\n\tLocations\x12\x39\n\tlocations\x18\x01 \x03(\x0b\x32\x1b.payload.v1.Object.LocationR\tlocations\x1a\x8b\x01\n\x04List\x1a\t\n\x07Request\x1ax\n\x08Response\x12\x33\n\x06vector\x18\x01 \x01(\x0b\x32\x19.payload.v1.Object.VectorH\x00R\x06vector\x12,\n\x06status\x18\x02 \x01(\x0b\x32\x12.google.rpc.StatusH\x00R\x06statusB\t\n\x07payload\"E\n\x07\x43ontrol\x1a:\n\x12\x43reateIndexRequest\x12$\n\tpool_size\x18\x01 \x01(\rB\x07\xbaH\x04*\x02(\x00R\x08poolSize\"f\n\nDiscoverer\x1aX\n\x07Request\x12\x1b\n\x04name\x18\x01 \x01(\tB\x07\xbaH\x04r\x02\x10\x01R\x04name\x12\x1c\n\tnamespace\x18\x02 \x01(\tR\tnamespace\x12\x12\n\x04node\x18\x03 \x01(\tR\x04node\"\xc2+\n\x04Info\x1a\x80 \n\x05Index\x1au\n\x05\x43ount\x12\x16\n\x06stored\x18\x01 \x01(\rR\x06stored\x12 \n\x0buncommitted\x18\x02 \x01(\rR\x0buncommitted\x12\x1a\n\x08indexing\x18\x03 \x01(\x08R\x08indexing\x12\x16\n\x06saving\x18\x04 \x01(\x08R\x06saving\x1a\xdf\x01\n\x06\x44\x65tail\x12\x41\n\x06\x63ounts\x18\x01 \x03(\x0b\x32).payload.v1.Info.Index.Detail.CountsEntryR\x06\x63ounts\x12\x18\n\x07replica\x18\x02 \x01(\rR\x07replica\x12\x1f\n\x0blive_agents\x18\x03 \x01(\rR\nliveAgents\x1aW\n\x0b\x43ountsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x32\n\x05value\x18\x02 \x01(\x0b\x32\x1c.payload.v1.Info.Index.CountR\x05value:\x02\x38\x01\x1aJ\n\x04UUID\x1a\x1f\n\tCommitted\x12\x12\n\x04uuid\x18\x01 \x01(\tR\x04uuid\x1a!\n\x0bUncommitted\x12\x12\n\x04uuid\x18\x01 \x01(\tR\x04uuid\x1a\x9d\r\n\nStatistics\x12\x14\n\x05valid\x18\x01 \x01(\x08R\x05valid\x12\'\n\x0fmedian_indegree\x18\x02 \x01(\x05R\x0emedianIndegree\x12)\n\x10median_outdegree\x18\x03 \x01(\x05R\x0fmedianOutdegree\x12\x33\n\x16max_number_of_indegree\x18\x04 \x01(\x04R\x13maxNumberOfIndegree\x12\x35\n\x17max_number_of_outdegree\x18\x05 \x01(\x04R\x14maxNumberOfOutdegree\x12\x33\n\x16min_number_of_indegree\x18\x06 \x01(\x04R\x13minNumberOfIndegree\x12\x35\n\x17min_number_of_outdegree\x18\x07 \x01(\x04R\x14minNumberOfOutdegree\x12#\n\rmode_indegree\x18\x08 \x01(\x04R\x0cmodeIndegree\x12%\n\x0emode_outdegree\x18\t \x01(\x04R\rmodeOutdegree\x12:\n\x1anodes_skipped_for_10_edges\x18\n \x01(\x04R\x16nodesSkippedFor10Edges\x12L\n#nodes_skipped_for_indegree_distance\x18\x0b \x01(\x04R\x1fnodesSkippedForIndegreeDistance\x12&\n\x0fnumber_of_edges\x18\x0c \x01(\x04R\rnumberOfEdges\x12\x39\n\x19number_of_indexed_objects\x18\r \x01(\x04R\x16numberOfIndexedObjects\x12&\n\x0fnumber_of_nodes\x18\x0e \x01(\x04R\rnumberOfNodes\x12@\n\x1dnumber_of_nodes_without_edges\x18\x0f \x01(\x04R\x19numberOfNodesWithoutEdges\x12\x46\n number_of_nodes_without_indegree\x18\x10 \x01(\x04R\x1cnumberOfNodesWithoutIndegree\x12*\n\x11number_of_objects\x18\x11 \x01(\x04R\x0fnumberOfObjects\x12\x39\n\x19number_of_removed_objects\x18\x12 \x01(\x04R\x16numberOfRemovedObjects\x12\x39\n\x19size_of_object_repository\x18\x13 \x01(\x04R\x16sizeOfObjectRepository\x12N\n$size_of_refinement_object_repository\x18\x14 \x01(\x04R sizeOfRefinementObjectRepository\x12\x30\n\x14variance_of_indegree\x18\x15 \x01(\x01R\x12varianceOfIndegree\x12\x32\n\x15variance_of_outdegree\x18\x16 \x01(\x01R\x13varianceOfOutdegree\x12(\n\x10mean_edge_length\x18\x17 \x01(\x01R\x0emeanEdgeLength\x12?\n\x1dmean_edge_length_for_10_edges\x18\x18 \x01(\x01R\x18meanEdgeLengthFor10Edges\x12K\n#mean_indegree_distance_for_10_edges\x18\x19 \x01(\x01R\x1emeanIndegreeDistanceFor10Edges\x12?\n\x1dmean_number_of_edges_per_node\x18\x1a \x01(\x01R\x18meanNumberOfEdgesPerNode\x12\x1f\n\x0b\x63\x31_indegree\x18\x1b \x01(\x01R\nc1Indegree\x12\x1f\n\x0b\x63\x35_indegree\x18\x1c \x01(\x01R\nc5Indegree\x12#\n\rc95_outdegree\x18\x1d \x01(\x01R\x0c\x63\x39\x35Outdegree\x12#\n\rc99_outdegree\x18\x1e \x01(\x01R\x0c\x63\x39\x39Outdegree\x12%\n\x0eindegree_count\x18\x1f \x03(\x03R\rindegreeCount\x12/\n\x13outdegree_histogram\x18  \x03(\x04R\x12outdegreeHistogram\x12-\n\x12indegree_histogram\x18! \x03(\x04R\x11indegreeHistogram\x1a\xc1\x01\n\x10StatisticsDetail\x12N\n\x07\x64\x65tails\x18\x01 \x03(\x0b\x32\x34.payload.v1.Info.Index.StatisticsDetail.DetailsEntryR\x07\x64\x65tails\x1a]\n\x0c\x44\x65tailsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x37\n\x05value\x18\x02 \x01(\x0b\x32!.payload.v1.Info.Index.StatisticsR\x05value:\x02\x38\x01\x1a\xaf\x0c\n\x08Property\x12\x1c\n\tdimension\x18\x01 \x01(\x05R\tdimension\x12(\n\x10thread_pool_size\x18\x02 \x01(\x05R\x0ethreadPoolSize\x12\x1f\n\x0bobject_type\x18\x03 \x01(\tR\nobjectType\x12#\n\rdistance_type\x18\x04 \x01(\tR\x0c\x64istanceType\x12\x1d\n\nindex_type\x18\x05 \x01(\tR\tindexType\x12#\n\rdatabase_type\x18\x06 \x01(\tR\x0c\x64\x61tabaseType\x12)\n\x10object_alignment\x18\x07 \x01(\tR\x0fobjectAlignment\x12\x38\n\x18path_adjustment_interval\x18\x08 \x01(\x05R\x16pathAdjustmentInterval\x12\x37\n\x18graph_shared_memory_size\x18\t \x01(\x05R\x15graphSharedMemorySize\x12\x35\n\x17tree_shared_memory_size\x18\n \x01(\x05R\x14treeSharedMemorySize\x12\x39\n\x19object_shared_memory_size\x18\x0b \x01(\x05R\x16objectSharedMemorySize\x12\'\n\x0fprefetch_offset\x18\x0c \x01(\x05R\x0eprefetchOffset\x12#\n\rprefetch_size\x18\r \x01(\x05R\x0cprefetchSize\x12%\n\x0e\x61\x63\x63uracy_table\x18\x0e \x01(\tR\raccuracyTable\x12\x1f\n\x0bsearch_type\x18\x0f \x01(\tR\nsearchType\x12#\n\rmax_magnitude\x18\x10 \x01(\x02R\x0cmaxMagnitude\x12I\n\"n_of_neighbors_for_insertion_order\x18\x11 \x01(\x05R\x1dnOfNeighborsForInsertionOrder\x12=\n\x1b\x65psilon_for_insertion_order\x18\x12 \x01(\x02R\x18\x65psilonForInsertionOrder\x12\x34\n\x16refinement_object_type\x18\x13 \x01(\tR\x14refinementObjectType\x12\x31\n\x14truncation_threshold\x18\x14 \x01(\x05R\x13truncationThreshold\x12\x33\n\x16\x65\x64ge_size_for_creation\x18\x15 \x01(\x05R\x13\x65\x64geSizeForCreation\x12/\n\x14\x65\x64ge_size_for_search\x18\x16 \x01(\x05R\x11\x65\x64geSizeForSearch\x12>\n\x1c\x65\x64ge_size_limit_for_creation\x18\x17 \x01(\x05R\x18\x65\x64geSizeLimitForCreation\x12@\n\x1cinsertion_radius_coefficient\x18\x18 \x01(\x01R\x1ainsertionRadiusCoefficient\x12\x1b\n\tseed_size\x18\x19 \x01(\x05R\x08seedSize\x12\x1b\n\tseed_type\x18\x1a \x01(\tR\x08seedType\x12=\n\x1btruncation_thread_pool_size\x18\x1b \x01(\x05R\x18truncationThreadPoolSize\x12\x35\n\x17\x62\x61tch_size_for_creation\x18\x1c \x01(\x05R\x14\x62\x61tchSizeForCreation\x12\x1d\n\ngraph_type\x18\x1d \x01(\tR\tgraphType\x12\x33\n\x16\x64ynamic_edge_size_base\x18\x1e \x01(\x05R\x13\x64ynamicEdgeSizeBase\x12\x33\n\x16\x64ynamic_edge_size_rate\x18\x1f \x01(\x05R\x13\x64ynamicEdgeSizeRate\x12(\n\x10\x62uild_time_limit\x18  \x01(\x02R\x0e\x62uildTimeLimit\x12#\n\routgoing_edge\x18! \x01(\x05R\x0coutgoingEdge\x12#\n\rincoming_edge\x18\" \x01(\x05R\x0cincomingEdge\x1a\xbb\x01\n\x0ePropertyDetail\x12L\n\x07\x64\x65tails\x18\x01 \x03(\x0b\x32\x32.payload.v1.Info.Index.PropertyDetail.DetailsEntryR\x07\x64\x65tails\x1a[\n\x0c\x44\x65tailsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x35\n\x05value\x18\x02 \x01(\x0b\x32\x1f.payload.v1.Info.Index.PropertyR\x05value:\x02\x38\x01\x1a\xef\x01\n\x03Pod\x12\x19\n\x08\x61pp_name\x18\x01 \x01(\tR\x07\x61ppName\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12\x1c\n\tnamespace\x18\x03 \x01(\tR\tnamespace\x12\x17\n\x02ip\x18\x04 \x01(\tB\x07\xbaH\x04r\x02x\x01R\x02ip\x12&\n\x03\x63pu\x18\x05 \x01(\x0b\x32\x14.payload.v1.Info.CPUR\x03\x63pu\x12/\n\x06memory\x18\x06 \x01(\x0b\x32\x17.payload.v1.Info.MemoryR\x06memory\x12)\n\x04node\x18\x07 \x01(\x0b\x32\x15.payload.v1.Info.NodeR\x04node\x1a\xe8\x01\n\x04Node\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12#\n\rinternal_addr\x18\x02 \x01(\tR\x0cinternalAddr\x12#\n\rexternal_addr\x18\x03 \x01(\tR\x0c\x65xternalAddr\x12&\n\x03\x63pu\x18\x04 \x01(\x0b\x32\x14.payload.v1.Info.CPUR\x03\x63pu\x12/\n\x06memory\x18\x05 \x01(\x0b\x32\x17.payload.v1.Info.MemoryR\x06memory\x12)\n\x04Pods\x18\x06 \x01(\x0b\x32\x15.payload.v1.Info.PodsR\x04Pods\x1a\x82\x02\n\x07Service\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1d\n\ncluster_ip\x18\x02 \x01(\tR\tclusterIp\x12\x1f\n\x0b\x63luster_ips\x18\x03 \x03(\tR\nclusterIps\x12\x32\n\x05ports\x18\x04 \x03(\x0b\x32\x1c.payload.v1.Info.ServicePortR\x05ports\x12/\n\x06labels\x18\x05 \x01(\x0b\x32\x17.payload.v1.Info.LabelsR\x06labels\x12>\n\x0b\x61nnotations\x18\x06 \x01(\x0b\x32\x1c.payload.v1.Info.AnnotationsR\x0b\x61nnotations\x1a\x35\n\x0bServicePort\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x12\n\x04port\x18\x02 \x01(\x05R\x04port\x1a\x80\x01\n\x06Labels\x12;\n\x06labels\x18\x01 \x03(\x0b\x32#.payload.v1.Info.Labels.LabelsEntryR\x06labels\x1a\x39\n\x0bLabelsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\x1a\x9e\x01\n\x0b\x41nnotations\x12O\n\x0b\x61nnotations\x18\x01 \x03(\x0b\x32-.payload.v1.Info.Annotations.AnnotationsEntryR\x0b\x61nnotations\x1a>\n\x10\x41nnotationsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\x1aK\n\x03\x43PU\x12\x14\n\x05limit\x18\x01 \x01(\x01R\x05limit\x12\x18\n\x07request\x18\x02 \x01(\x01R\x07request\x12\x14\n\x05usage\x18\x03 \x01(\x01R\x05usage\x1aN\n\x06Memory\x12\x14\n\x05limit\x18\x01 \x01(\x01R\x05limit\x12\x18\n\x07request\x18\x02 \x01(\x01R\x07request\x12\x14\n\x05usage\x18\x03 \x01(\x01R\x05usage\x1a:\n\x04Pods\x12\x32\n\x04pods\x18\x01 \x03(\x0b\x32\x14.payload.v1.Info.PodB\x08\xbaH\x05\x92\x01\x02\x08\x01R\x04pods\x1a>\n\x05Nodes\x12\x35\n\x05nodes\x18\x01 \x03(\x0b\x32\x15.payload.v1.Info.NodeB\x08\xbaH\x05\x92\x01\x02\x08\x01R\x05nodes\x1aJ\n\x08Services\x12>\n\x08services\x18\x01 \x03(\x0b\x32\x18.payload.v1.Info.ServiceB\x08\xbaH\x05\x92\x01\x02\x08\x01R\x08services\x1a\x15\n\x03IPs\x12\x0e\n\x02ip\x18\x01 \x03(\tR\x02ip\"z\n\x06Mirror\x1a\x30\n\x06Target\x12\x12\n\x04host\x18\x01 \x01(\tR\x04host\x12\x12\n\x04port\x18\x02 \x01(\rR\x04port\x1a>\n\x07Targets\x12\x33\n\x07targets\x18\x01 \x03(\x0b\x32\x19.payload.v1.Mirror.TargetR\x07targets\"\xb6\x01\n\x04Meta\x1a\x17\n\x03Key\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x1a\x33\n\x05Value\x12*\n\x05value\x18\x01 \x01(\x0b\x32\x14.google.protobuf.AnyR\x05value\x1a`\n\x08KeyValue\x12&\n\x03key\x18\x01 \x01(\x0b\x32\x14.payload.v1.Meta.KeyR\x03key\x12,\n\x05value\x18\x02 \x01(\x0b\x32\x16.payload.v1.Meta.ValueR\x05value\"\x07\n\x05\x45mptyBd\n\x1dorg.vdaas.vald.api.v1.payloadB\x0bValdPayloadP\x01Z*github.com/vdaas/vald/apis/grpc/v1/payload\xa2\x02\x07Payloadb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'vald.v1.payload.payload_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\035org.vdaas.vald.api.v1.payloadB\013ValdPayloadP\001Z*github.com/vdaas/vald/apis/grpc/v1/payload\242\002\007Payload'
  _globals['_SEARCH_REQUEST'].fields_by_name['vector']._loaded_options = None
  _globals['_SEARCH_REQUEST'].fields_by_name['vector']._serialized_options = b'\272H\005\222\001\002\010\002'
  _globals['_SEARCH_CONFIG'].fields_by_name['num']._loaded_options = None
  _globals['_SEARCH_CONFIG'].fields_by_name['num']._serialized_options = b'\272H\004*\002(\001'
  _globals['_SEARCH_CONFIG'].fields_by_name['min_num']._loaded_options = None
  _globals['_SEARCH_CONFIG'].fields_by_name['min_num']._serialized_options = b'\272H\004*\002(\000'
  _globals['_INSERT_REQUEST'].fields_by_name['vector']._loaded_options = None
  _globals['_INSERT_REQUEST'].fields_by_name['vector']._serialized_options = b'\272H\005\222\001\002\010\002'
  _globals['_UPDATE_REQUEST'].fields_by_name['vector']._loaded_options = None
  _globals['_UPDATE_REQUEST'].fields_by_name['vector']._serialized_options = b'\272H\005\222\001\002\010\002'
  _globals['_UPDATE_TIMESTAMPREQUEST'].fields_by_name['id']._loaded_options = None
  _globals['_UPDATE_TIMESTAMPREQUEST'].fields_by_name['id']._serialized_options = b'\272H\004r\002\020\001'
  _globals['_UPSERT_REQUEST'].fields_by_name['vector']._loaded_options = None
  _globals['_UPSERT_REQUEST'].fields_by_name['vector']._serialized_options = b'\272H\005\222\001\002\010\002'
  _globals['_OBJECT_VECTORREQUEST'].fields_by_name['id']._loaded_options = None
  _globals['_OBJECT_VECTORREQUEST'].fields_by_name['id']._serialized_options = b'\272H\005\222\001\002\010\002'
  _globals['_OBJECT_ID'].fields_by_name['id']._loaded_options = None
  _globals['_OBJECT_ID'].fields_by_name['id']._serialized_options = b'\272H\004r\002\020\001'
  _globals['_OBJECT_VECTOR'].fields_by_name['id']._loaded_options = None
  _globals['_OBJECT_VECTOR'].fields_by_name['id']._serialized_options = b'\272H\004r\002\020\001'
  _globals['_OBJECT_VECTOR'].fields_by_name['vector']._loaded_options = None
  _globals['_OBJECT_VECTOR'].fields_by_name['vector']._serialized_options = b'\272H\005\222\001\002\010\002'
  _globals['_OBJECT_TIMESTAMPREQUEST'].fields_by_name['id']._loaded_options = None
  _globals['_OBJECT_TIMESTAMPREQUEST'].fields_by_name['id']._serialized_options = b'\272H\005\222\001\002\010\002'
  _globals['_OBJECT_TIMESTAMP'].fields_by_name['id']._loaded_options = None
  _globals['_OBJECT_TIMESTAMP'].fields_by_name['id']._serialized_options = b'\272H\004r\002\020\001'
  _globals['_OBJECT_BLOB'].fields_by_name['id']._loaded_options = None
  _globals['_OBJECT_BLOB'].fields_by_name['id']._serialized_options = b'\272H\004r\002\020\001'
  _globals['_CONTROL_CREATEINDEXREQUEST'].fields_by_name['pool_size']._loaded_options = None
  _globals['_CONTROL_CREATEINDEXREQUEST'].fields_by_name['pool_size']._serialized_options = b'\272H\004*\002(\000'
  _globals['_DISCOVERER_REQUEST'].fields_by_name['name']._loaded_options = None
  _globals['_DISCOVERER_REQUEST'].fields_by_name['name']._serialized_options = b'\272H\004r\002\020\001'
  _globals['_INFO_INDEX_DETAIL_COUNTSENTRY']._loaded_options = None
  _globals['_INFO_INDEX_DETAIL_COUNTSENTRY']._serialized_options = b'8\001'
  _globals['_INFO_INDEX_STATISTICSDETAIL_DETAILSENTRY']._loaded_options = None
  _globals['_INFO_INDEX_STATISTICSDETAIL_DETAILSENTRY']._serialized_options = b'8\001'
  _globals['_INFO_INDEX_PROPERTYDETAIL_DETAILSENTRY']._loaded_options = None
  _globals['_INFO_INDEX_PROPERTYDETAIL_DETAILSENTRY']._serialized_options = b'8\001'
  _globals['_INFO_POD'].fields_by_name['ip']._loaded_options = None
  _globals['_INFO_POD'].fields_by_name['ip']._serialized_options = b'\272H\004r\002x\001'
  _globals['_INFO_LABELS_LABELSENTRY']._loaded_options = None
  _globals['_INFO_LABELS_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_INFO_ANNOTATIONS_ANNOTATIONSENTRY']._loaded_options = None
  _globals['_INFO_ANNOTATIONS_ANNOTATIONSENTRY']._serialized_options = b'8\001'
  _globals['_INFO_PODS'].fields_by_name['pods']._loaded_options = None
  _globals['_INFO_PODS'].fields_by_name['pods']._serialized_options = b'\272H\005\222\001\002\010\001'
  _globals['_INFO_NODES'].fields_by_name['nodes']._loaded_options = None
  _globals['_INFO_NODES'].fields_by_name['nodes']._serialized_options = b'\272H\005\222\001\002\010\001'
  _globals['_INFO_SERVICES'].fields_by_name['services']._loaded_options = None
  _globals['_INFO_SERVICES'].fields_by_name['services']._serialized_options = b'\272H\005\222\001\002\010\001'
  _globals['_SEARCH']._serialized_start=159
  _globals['_SEARCH']._serialized_end=1623
  _globals['_SEARCH_REQUEST']._serialized_start=169
  _globals['_SEARCH_REQUEST']._serialized_end=263
  _globals['_SEARCH_MULTIREQUEST']._serialized_start=265
  _globals['_SEARCH_MULTIREQUEST']._serialized_end=335
  _globals['_SEARCH_IDREQUEST']._serialized_start=337
  _globals['_SEARCH_IDREQUEST']._serialized_end=415
  _globals['_SEARCH_MULTIIDREQUEST']._serialized_start=417
  _globals['_SEARCH_MULTIIDREQUEST']._serialized_end=491
  _globals['_SEARCH_OBJECTREQUEST']._serialized_start=494
  _globals['_SEARCH_OBJECTREQUEST']._serialized_end=643
  _globals['_SEARCH_MULTIOBJECTREQUEST']._serialized_start=645
  _globals['_SEARCH_MULTIOBJECTREQUEST']._serialized_end=727
  _globals['_SEARCH_CONFIG']._serialized_start=730
  _globals['_SEARCH_CONFIG']._serialized_end=1209
  _globals['_SEARCH_RESPONSE']._serialized_start=1211
  _globals['_SEARCH_RESPONSE']._serialized_end=1307
  _globals['_SEARCH_RESPONSES']._serialized_start=1309
  _globals['_SEARCH_RESPONSES']._serialized_end=1379
  _globals['_SEARCH_STREAMRESPONSE']._serialized_start=1382
  _globals['_SEARCH_STREAMRESPONSE']._serialized_end=1514
  _globals['_SEARCH_AGGREGATIONALGORITHM']._serialized_start=1516
  _globals['_SEARCH_AGGREGATIONALGORITHM']._serialized_end=1623
  _globals['_FILTER']._serialized_start=1625
  _globals['_FILTER']._serialized_end=1746
  _globals['_FILTER_TARGET']._serialized_start=1635
  _globals['_FILTER_TARGET']._serialized_end=1683
  _globals['_FILTER_CONFIG']._serialized_start=1685
  _globals['_FILTER_CONFIG']._serialized_end=1746
  _globals['_INSERT']._serialized_start=1749
  _globals['_INSERT']._serialized_end=2362
  _globals['_INSERT_REQUEST']._serialized_start=1759
  _globals['_INSERT_REQUEST']._serialized_end=1880
  _globals['_INSERT_MULTIREQUEST']._serialized_start=1882
  _globals['_INSERT_MULTIREQUEST']._serialized_end=1952
  _globals['_INSERT_OBJECTREQUEST']._serialized_start=1955
  _globals['_INSERT_OBJECTREQUEST']._serialized_end=2129
  _globals['_INSERT_MULTIOBJECTREQUEST']._serialized_start=2131
  _globals['_INSERT_MULTIOBJECTREQUEST']._serialized_end=2213
  _globals['_INSERT_CONFIG']._serialized_start=2216
  _globals['_INSERT_CONFIG']._serialized_end=2362
  _globals['_UPDATE']._serialized_start=2365
  _globals['_UPDATE']._serialized_end=3131
  _globals['_UPDATE_REQUEST']._serialized_start=2375
  _globals['_UPDATE_REQUEST']._serialized_end=2496
  _globals['_UPDATE_MULTIREQUEST']._serialized_start=2498
  _globals['_UPDATE_MULTIREQUEST']._serialized_end=2568
  _globals['_UPDATE_OBJECTREQUEST']._serialized_start=2571
  _globals['_UPDATE_OBJECTREQUEST']._serialized_end=2745
  _globals['_UPDATE_MULTIOBJECTREQUEST']._serialized_start=2747
  _globals['_UPDATE_MULTIOBJECTREQUEST']._serialized_end=2829
  _globals['_UPDATE_TIMESTAMPREQUEST']._serialized_start=2831
  _globals['_UPDATE_TIMESTAMPREQUEST']._serialized_end=2926
  _globals['_UPDATE_CONFIG']._serialized_start=2929
  _globals['_UPDATE_CONFIG']._serialized_end=3131
  _globals['_UPSERT']._serialized_start=3134
  _globals['_UPSERT']._serialized_end=3803
  _globals['_UPSERT_REQUEST']._serialized_start=3144
  _globals['_UPSERT_REQUEST']._serialized_end=3265
  _globals['_UPSERT_MULTIREQUEST']._serialized_start=3267
  _globals['_UPSERT_MULTIREQUEST']._serialized_end=3337
  _globals['_UPSERT_OBJECTREQUEST']._serialized_start=3340
  _globals['_UPSERT_OBJECTREQUEST']._serialized_end=3514
  _globals['_UPSERT_MULTIOBJECTREQUEST']._serialized_start=3516
  _globals['_UPSERT_MULTIOBJECTREQUEST']._serialized_end=3598
  _globals['_UPSERT_CONFIG']._serialized_start=2929
  _globals['_UPSERT_CONFIG']._serialized_end=3131
  _globals['_REMOVE']._serialized_start=3806
  _globals['_REMOVE']._serialized_end=4335
  _globals['_REMOVE_REQUEST']._serialized_start=3816
  _globals['_REMOVE_REQUEST']._serialized_end=3915
  _globals['_REMOVE_MULTIREQUEST']._serialized_start=3917
  _globals['_REMOVE_MULTIREQUEST']._serialized_end=3987
  _globals['_REMOVE_TIMESTAMPREQUEST']._serialized_start=3989
  _globals['_REMOVE_TIMESTAMPREQUEST']._serialized_end=4069
  _globals['_REMOVE_TIMESTAMP']._serialized_start=4072
  _globals['_REMOVE_TIMESTAMP']._serialized_end=4240
  _globals['_REMOVE_TIMESTAMP_OPERATOR']._serialized_start=4182
  _globals['_REMOVE_TIMESTAMP_OPERATOR']._serialized_end=4240
  _globals['_REMOVE_CONFIG']._serialized_start=4242
  _globals['_REMOVE_CONFIG']._serialized_end=4335
  _globals['_FLUSH']._serialized_start=4337
  _globals['_FLUSH']._serialized_end=4355
  _globals['_FLUSH_REQUEST']._serialized_start=169
  _globals['_FLUSH_REQUEST']._serialized_end=178
  _globals['_OBJECT']._serialized_start=4358
  _globals['_OBJECT']._serialized_end=5815
  _globals['_OBJECT_VECTORREQUEST']._serialized_start=4368
  _globals['_OBJECT_VECTORREQUEST']._serialized_end=4485
  _globals['_OBJECT_DISTANCE']._serialized_start=4487
  _globals['_OBJECT_DISTANCE']._serialized_end=4541
  _globals['_OBJECT_STREAMDISTANCE']._serialized_start=4544
  _globals['_OBJECT_STREAMDISTANCE']._serialized_end=4676
  _globals['_OBJECT_ID']._serialized_start=4678
  _globals['_OBJECT_ID']._serialized_end=4707
  _globals['_OBJECT_IDS']._serialized_start=4709
  _globals['_OBJECT_IDS']._serialized_end=4732
  _globals['_OBJECT_VECTOR']._serialized_start=4734
  _globals['_OBJECT_VECTOR']._serialized_end=4831
  _globals['_OBJECT_TIMESTAMPREQUEST']._serialized_start=4833
  _globals['_OBJECT_TIMESTAMPREQUEST']._serialized_end=4900
  _globals['_OBJECT_TIMESTAMP']._serialized_start=4902
  _globals['_OBJECT_TIMESTAMP']._serialized_end=4968
  _globals['_OBJECT_VECTORS']._serialized_start=4970
  _globals['_OBJECT_VECTORS']._serialized_end=5032
  _globals['_OBJECT_STREAMVECTOR']._serialized_start=5034
  _globals['_OBJECT_STREAMVECTOR']._serialized_end=5158
  _globals['_OBJECT_RESHAPEVECTOR']._serialized_start=5160
  _globals['_OBJECT_RESHAPEVECTOR']._serialized_end=5221
  _globals['_OBJECT_BLOB']._serialized_start=5223
  _globals['_OBJECT_BLOB']._serialized_end=5278
  _globals['_OBJECT_STREAMBLOB']._serialized_start=5280
  _globals['_OBJECT_STREAMBLOB']._serialized_end=5396
  _globals['_OBJECT_LOCATION']._serialized_start=5398
  _globals['_OBJECT_LOCATION']._serialized_end=5466
  _globals['_OBJECT_STREAMLOCATION']._serialized_start=5469
  _globals['_OBJECT_STREAMLOCATION']._serialized_end=5601
  _globals['_OBJECT_LOCATIONS']._serialized_start=5603
  _globals['_OBJECT_LOCATIONS']._serialized_end=5673
  _globals['_OBJECT_LIST']._serialized_start=5676
  _globals['_OBJECT_LIST']._serialized_end=5815
  _globals['_OBJECT_LIST_REQUEST']._serialized_start=169
  _globals['_OBJECT_LIST_REQUEST']._serialized_end=178
  _globals['_OBJECT_LIST_RESPONSE']._serialized_start=5695
  _globals['_OBJECT_LIST_RESPONSE']._serialized_end=5815
  _globals['_CONTROL']._serialized_start=5817
  _globals['_CONTROL']._serialized_end=5886
  _globals['_CONTROL_CREATEINDEXREQUEST']._serialized_start=5828
  _globals['_CONTROL_CREATEINDEXREQUEST']._serialized_end=5886
  _globals['_DISCOVERER']._serialized_start=5888
  _globals['_DISCOVERER']._serialized_end=5990
  _globals['_DISCOVERER_REQUEST']._serialized_start=5902
  _globals['_DISCOVERER_REQUEST']._serialized_end=5990
  _globals['_INFO']._serialized_start=5993
  _globals['_INFO']._serialized_end=11563
  _globals['_INFO_INDEX']._serialized_start=6002
  _globals['_INFO_INDEX']._serialized_end=10098
  _globals['_INFO_INDEX_COUNT']._serialized_start=6011
  _globals['_INFO_INDEX_COUNT']._serialized_end=6128
  _globals['_INFO_INDEX_DETAIL']._serialized_start=6131
  _globals['_INFO_INDEX_DETAIL']._serialized_end=6354
  _globals['_INFO_INDEX_DETAIL_COUNTSENTRY']._serialized_start=6267
  _globals['_INFO_INDEX_DETAIL_COUNTSENTRY']._serialized_end=6354
  _globals['_INFO_INDEX_UUID']._serialized_start=6356
  _globals['_INFO_INDEX_UUID']._serialized_end=6430
  _globals['_INFO_INDEX_UUID_COMMITTED']._serialized_start=6364
  _globals['_INFO_INDEX_UUID_COMMITTED']._serialized_end=6395
  _globals['_INFO_INDEX_UUID_UNCOMMITTED']._serialized_start=6397
  _globals['_INFO_INDEX_UUID_UNCOMMITTED']._serialized_end=6430
  _globals['_INFO_INDEX_STATISTICS']._serialized_start=6433
  _globals['_INFO_INDEX_STATISTICS']._serialized_end=8126
  _globals['_INFO_INDEX_STATISTICSDETAIL']._serialized_start=8129
  _globals['_INFO_INDEX_STATISTICSDETAIL']._serialized_end=8322
  _globals['_INFO_INDEX_STATISTICSDETAIL_DETAILSENTRY']._serialized_start=8229
  _globals['_INFO_INDEX_STATISTICSDETAIL_DETAILSENTRY']._serialized_end=8322
  _globals['_INFO_INDEX_PROPERTY']._serialized_start=8325
  _globals['_INFO_INDEX_PROPERTY']._serialized_end=9908
  _globals['_INFO_INDEX_PROPERTYDETAIL']._serialized_start=9911
  _globals['_INFO_INDEX_PROPERTYDETAIL']._serialized_end=10098
  _globals['_INFO_INDEX_PROPERTYDETAIL_DETAILSENTRY']._serialized_start=10007
  _globals['_INFO_INDEX_PROPERTYDETAIL_DETAILSENTRY']._serialized_end=10098
  _globals['_INFO_POD']._serialized_start=10101
  _globals['_INFO_POD']._serialized_end=10340
  _globals['_INFO_NODE']._serialized_start=10343
  _globals['_INFO_NODE']._serialized_end=10575
  _globals['_INFO_SERVICE']._serialized_start=10578
  _globals['_INFO_SERVICE']._serialized_end=10836
  _globals['_INFO_SERVICEPORT']._serialized_start=10838
  _globals['_INFO_SERVICEPORT']._serialized_end=10891
  _globals['_INFO_LABELS']._serialized_start=10894
  _globals['_INFO_LABELS']._serialized_end=11022
  _globals['_INFO_LABELS_LABELSENTRY']._serialized_start=10965
  _globals['_INFO_LABELS_LABELSENTRY']._serialized_end=11022
  _globals['_INFO_ANNOTATIONS']._serialized_start=11025
  _globals['_INFO_ANNOTATIONS']._serialized_end=11183
  _globals['_INFO_ANNOTATIONS_ANNOTATIONSENTRY']._serialized_start=11121
  _globals['_INFO_ANNOTATIONS_ANNOTATIONSENTRY']._serialized_end=11183
  _globals['_INFO_CPU']._serialized_start=11185
  _globals['_INFO_CPU']._serialized_end=11260
  _globals['_INFO_MEMORY']._serialized_start=11262
  _globals['_INFO_MEMORY']._serialized_end=11340
  _globals['_INFO_PODS']._serialized_start=11342
  _globals['_INFO_PODS']._serialized_end=11400
  _globals['_INFO_NODES']._serialized_start=11402
  _globals['_INFO_NODES']._serialized_end=11464
  _globals['_INFO_SERVICES']._serialized_start=11466
  _globals['_INFO_SERVICES']._serialized_end=11540
  _globals['_INFO_IPS']._serialized_start=11542
  _globals['_INFO_IPS']._serialized_end=11563
  _globals['_MIRROR']._serialized_start=11565
  _globals['_MIRROR']._serialized_end=11687
  _globals['_MIRROR_TARGET']._serialized_start=1635
  _globals['_MIRROR_TARGET']._serialized_end=1683
  _globals['_MIRROR_TARGETS']._serialized_start=11625
  _globals['_MIRROR_TARGETS']._serialized_end=11687
  _globals['_META']._serialized_start=11690
  _globals['_META']._serialized_end=11872
  _globals['_META_KEY']._serialized_start=11698
  _globals['_META_KEY']._serialized_end=11721
  _globals['_META_VALUE']._serialized_start=11723
  _globals['_META_VALUE']._serialized_end=11774
  _globals['_META_KEYVALUE']._serialized_start=11776
  _globals['_META_KEYVALUE']._serialized_end=11872
  _globals['_EMPTY']._serialized_start=11874
  _globals['_EMPTY']._serialized_end=11881
# @@protoc_insertion_point(module_scope)
