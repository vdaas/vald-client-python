# vald-client-python

[![PyPI version](https://badge.fury.io/py/vald-client-python.svg)](https://badge.fury.io/py/vald-client-python)

A Python gRPC client library for [Vald](https://github.com/vdaas/vald).

## Install

Using pip,

```sh
pip install vald-client-python
```

## Usage

To use v1 APIs,

```python
import grpc
from vald.v1.vald import insert_pb2_grpc
from vald.v1.vald import search_pb2_grpc
from vald.v1.vald import update_pb2_grpc
from vald.v1.vald import remove_pb2_grpc
from vald.v1.payload import payload_pb2

## create a channel by passing "{host}:{port}"
channel = grpc.insecure_channel("gateway.vald.vdaas.org:80")

## create stubs for calling RPCs
istub = insert_pb2_grpc.InsertStub(channel)
sstub = search_pb2_grpc.SearchStub(channel)
ustub = update_pb2_grpc.UpdateStub(channel)
rstub = remove_pb2_grpc.RemoveStub(channel)

## call RPCs: Insert
vec = payload_pb2.Object.Vector(id='vector_id_1', vector=[0.1, 0.2, 0.3])
icfg = payload_pb2.Insert.Config(skip_strict_exist_check=True)
istub.Insert(payload_pb2.Insert.Request(vector=vec, config=icfg))


## call RPCs: Search
### num: number of results
### timeout: 3 seconds
scfg = payload_pb2.Search.Config(num=10, radius=-1.0, epsilon=0.01, timeout=3000000000)
res = sstub.Search(payload_pb2.Search.Request(vector=[0.1, 0.2, 0.3], config=scfg))


## call RPCs: Update
uvec = payload_pb2.Object.Vector(id='vector_id_1', vector=[0.1, 0.2, 0.3])
ucfg = payload_pb2.Update.Config(skip_strict_exist_check=True)
ustub.Update(payload_pb2.Update.Request(vector=vec, config=ucfg))


## call RPCs: Remove
rcfg = payload_pb2.Remove.Config(skip_strict_exist_check=True)
rid = payload_pb2.Object.ID(id='vector_id_1')
rstub.Remove(payload_pb2.Remove.Request(id=rid, config=rcfg))

## close channel
channel.close()
```
