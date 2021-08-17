import unittest
import json
import time

import grpc
from vald.v1.agent.core import agent_pb2_grpc
from vald.v1.vald import insert_pb2_grpc
from vald.v1.vald import search_pb2_grpc
from vald.v1.vald import update_pb2_grpc
from vald.v1.vald import upsert_pb2_grpc
from vald.v1.vald import remove_pb2_grpc
from vald.v1.vald import object_pb2_grpc
from vald.v1.payload import payload_pb2


class TestValdE2E(unittest.TestCase):
    """e2e test for vald-client-python
    """

    def __init__(self, *args, **kwargs):
        super(TestValdE2E, self).__init__(*args, **kwargs)
        self.data = json.load(open("wordvecs1000.json", "r"))

    def setUp(self):
        options = [("grpc.keepalive_time_ms", 10000),
                   ("grpc.keepalive_timeout_ms", 5000),
                   ("grpc.client_channel_backup_poll_interval_ms", 100)]
        self.channel = grpc.insecure_channel(
            target="localhost:8081", options=options)

    def tearDown(self):
        self.channel.close()

    def test_insert(self):
        stub = insert_pb2_grpc.InsertStub(self.channel)
        vec = payload_pb2.Object.Vector(
            id=self.data[0]["id"], vector=self.data[0]["vector"])
        cfg = payload_pb2.Insert.Config(skip_strict_exist_check=True)
        result = stub.Insert(
            payload_pb2.Insert.Request(vector=vec, config=cfg))
        self.assertIsInstance(result, payload_pb2.Object.Location)

    def test_multi_insert(self):
        stub = insert_pb2_grpc.InsertStub(self.channel)
        cfg = payload_pb2.Insert.Config(skip_strict_exist_check=True)
        requests = []
        for i in range(1, 10):
            vec = payload_pb2.Object.Vector(
                id=self.data[i]["id"], vector=self.data[i]["vector"])
            requests.append(payload_pb2.Insert.Request(
                vector=vec, config=cfg))
        results = stub.MultiInsert(
            payload_pb2.Insert.MultiRequest(requests=requests))
        self.assertIsInstance(results, payload_pb2.Object.Locations)

    def test_stream_insert(self):
        stub = insert_pb2_grpc.InsertStub(self.channel)
        cfg = payload_pb2.Insert.Config(skip_strict_exist_check=True)
        requests = []
        for i in range(11, 100):
            vec = payload_pb2.Object.Vector(
                id=self.data[i]["id"], vector=self.data[i]["vector"])
            requests.append(payload_pb2.Insert.Request(
                vector=vec, config=cfg))
        results = stub.StreamInsert(iter(requests))
        for result in results:
            self.assertIsInstance(result, payload_pb2.Object.StreamLocation)
            self.assertEqual(result.status.code, 0)

    def test_create_index(self):
        stub = agent_pb2_grpc.AgentStub(self.channel)
        result = stub.CreateIndex(
            payload_pb2.Control.CreateIndexRequest(pool_size=10000))
        self.assertIsInstance(result, payload_pb2.Empty)

    def test_save_index(self):
        stub = agent_pb2_grpc.AgentStub(self.channel)
        result = stub.SaveIndex(payload_pb2.Empty())
        self.assertIsInstance(result, payload_pb2.Empty)

    def test_index_info(self):
        stub = agent_pb2_grpc.AgentStub(self.channel)
        result = stub.IndexInfo(payload_pb2.Empty())
        self.assertIsInstance(result, payload_pb2.Info.Index.Count)
        self.assertEqual(result.stored, 99)
        self.assertEqual(result.uncommitted, 0)

    def test_exists(self):
        stub = object_pb2_grpc.ObjectStub(self.channel)
        result = stub.Exists(
            payload_pb2.Object.ID(id=self.data[0]["id"]))
        self.assertIsInstance(result, payload_pb2.Object.ID)

    def test_get_object(self):
        stub = object_pb2_grpc.ObjectStub(self.channel)
        req = payload_pb2.Object.VectorRequest(
            id=payload_pb2.Object.ID(id=self.data[0]["id"]))
        result = stub.GetObject(req)
        self.assertIsInstance(result, payload_pb2.Object.Vector)
        self.assertEqual(result.id, self.data[0]["id"])

    def test_stream_get_object(self):
        stub = object_pb2_grpc.ObjectStub(self.channel)
        requests = []
        for i in range(0, 10):
            requests.append(payload_pb2.Object.VectorRequest(
                id=payload_pb2.Object.ID(id=self.data[i]["id"])))
        results = stub.StreamGetObject(iter(requests))
        for result in results:
            self.assertIsInstance(result, payload_pb2.Object.StreamVector)

    def test_search(self):
        stub = search_pb2_grpc.SearchStub(self.channel)
        cfg = payload_pb2.Search.Config(
            num=3, radius=-1.0, epsilon=0.1, timeout=3000000000)
        result = stub.Search(payload_pb2.Search.Request(
            vector=self.data[0]["vector"], config=cfg))
        self.assertIsInstance(result, payload_pb2.Search.Response)
        self.assertEqual(len(result.results), 3)

    def test_multi_search(self):
        stub = search_pb2_grpc.SearchStub(self.channel)
        cfg = payload_pb2.Search.Config(
            num=3, radius=-1.0, epsilon=0.1, timeout=3000000000)
        requests = []
        for i in range(1, 10):
            requests.append(payload_pb2.Search.Request(
                vector=self.data[i]["vector"], config=cfg))
        results = stub.MultiSearch(
            payload_pb2.Search.MultiRequest(requests=requests))
        self.assertIsInstance(results, payload_pb2.Search.Responses)
        for response in results.responses:
            self.assertIsInstance(response, payload_pb2.Search.Response)
            self.assertEqual(len(response.results), 3)

    def test_stream_search(self):
        stub = search_pb2_grpc.SearchStub(self.channel)
        cfg = payload_pb2.Search.Config(
            num=3, radius=-1.0, epsilon=0.1, timeout=3000000000)
        requests = []
        for i in range(11, 20):
            requests.append(payload_pb2.Search.Request(
                vector=self.data[i]["vector"], config=cfg))
        results = stub.StreamSearch(iter(requests))
        for result in results:
            self.assertIsInstance(result, payload_pb2.Search.StreamResponse)
            self.assertIsNotNone(result.response)

    def test_search_id(self):
        stub = search_pb2_grpc.SearchStub(self.channel)
        cfg = payload_pb2.Search.Config(
            num=3, radius=-1.0, epsilon=0.1, timeout=3000000000)
        result = stub.SearchByID(payload_pb2.Search.IDRequest(
            id=self.data[0]["id"], config=cfg))
        self.assertIsInstance(result, payload_pb2.Search.Response)
        self.assertEqual(len(result.results), 3)

    def test_multi_search_id(self):
        stub = search_pb2_grpc.SearchStub(self.channel)
        cfg = payload_pb2.Search.Config(
            num=3, radius=-1.0, epsilon=0.1, timeout=3000000000)
        requests = []
        for i in range(1, 10):
            requests.append(payload_pb2.Search.IDRequest(
                id=self.data[i]["id"], config=cfg))
        results = stub.MultiSearchByID(
            payload_pb2.Search.MultiIDRequest(requests=requests))
        self.assertIsInstance(results, payload_pb2.Search.Responses)
        for response in results.responses:
            self.assertIsInstance(response, payload_pb2.Search.Response)
            self.assertEqual(len(response.results), 3)

    def test_stream_search_id(self):
        stub = search_pb2_grpc.SearchStub(self.channel)
        cfg = payload_pb2.Search.Config(
            num=3, radius=-1.0, epsilon=0.1, timeout=3000000000)
        requests = []
        for i in range(11, 20):
            requests.append(payload_pb2.Search.IDRequest(
                id=self.data[i]["id"], config=cfg))
        results = stub.StreamSearchByID(iter(requests))
        for result in results:
            self.assertIsInstance(result, payload_pb2.Search.StreamResponse)
            self.assertIsNotNone(result.response)

    def test_update(self):
        stub = update_pb2_grpc.UpdateStub(self.channel)
        vec = payload_pb2.Object.Vector(
            id=self.data[0]["id"], vector=self.data[1]["vector"])
        cfg = payload_pb2.Update.Config(skip_strict_exist_check=True)
        result = stub.Update(
            payload_pb2.Update.Request(vector=vec, config=cfg))
        self.assertIsInstance(result, payload_pb2.Object.Location)

    def test_multi_update(self):
        stub = update_pb2_grpc.UpdateStub(self.channel)
        cfg = payload_pb2.Update.Config(skip_strict_exist_check=True)
        requests = []
        for i in range(1, 10):
            vec = payload_pb2.Object.Vector(
                id=self.data[i]["id"], vector=self.data[i+1]["vector"])
            requests.append(payload_pb2.Update.Request(
                vector=vec, config=cfg))
        results = stub.MultiUpdate(
            payload_pb2.Update.MultiRequest(requests=requests))
        self.assertIsInstance(results, payload_pb2.Object.Locations)

    def test_stream_update(self):
        stub = update_pb2_grpc.UpdateStub(self.channel)
        cfg = payload_pb2.Update.Config(skip_strict_exist_check=True)
        requests = []
        for i in range(11, 20):
            vec = payload_pb2.Object.Vector(
                id=self.data[i]["id"], vector=self.data[i+1]["vector"])
            requests.append(payload_pb2.Update.Request(
                vector=vec, config=cfg))
        results = stub.StreamUpdate(iter(requests))
        for result in results:
            self.assertIsInstance(result, payload_pb2.Object.StreamLocation)
            self.assertEqual(result.status.code, 0)

    def test_upsert(self):
        stub = upsert_pb2_grpc.UpsertStub(self.channel)
        vec = payload_pb2.Object.Vector(
            id=self.data[0]["id"], vector=self.data[0]["vector"])
        cfg = payload_pb2.Upsert.Config(skip_strict_exist_check=True)
        result = stub.Upsert(
            payload_pb2.Upsert.Request(vector=vec, config=cfg))
        self.assertIsInstance(result, payload_pb2.Object.Location)

    def test_multi_upsert(self):
        stub = upsert_pb2_grpc.UpsertStub(self.channel)
        cfg = payload_pb2.Upsert.Config(skip_strict_exist_check=True)
        requests = []
        for i in range(1, 10):
            vec = payload_pb2.Object.Vector(
                id=self.data[i]["id"], vector=self.data[i]["vector"])
            requests.append(payload_pb2.Upsert.Request(
                vector=vec, config=cfg))
        results = stub.MultiUpsert(
            payload_pb2.Upsert.MultiRequest(requests=requests))
        self.assertIsInstance(results, payload_pb2.Object.Locations)

    def test_stream_upsert(self):
        stub = upsert_pb2_grpc.UpsertStub(self.channel)
        cfg = payload_pb2.Upsert.Config(skip_strict_exist_check=True)
        requests = []
        for i in range(11, 20):
            vec = payload_pb2.Object.Vector(
                id=self.data[i]["id"], vector=self.data[i]["vector"])
            requests.append(payload_pb2.Upsert.Request(
                vector=vec, config=cfg))
        results = stub.StreamUpsert(iter(requests))
        for result in results:
            self.assertIsInstance(result, payload_pb2.Object.StreamLocation)
            self.assertEqual(result.status.code, 0)

    def test_remove(self):
        stub = remove_pb2_grpc.RemoveStub(self.channel)
        cfg = payload_pb2.Remove.Config(skip_strict_exist_check=True)
        result = stub.Remove(
            payload_pb2.Remove.Request(
                id=payload_pb2.Object.ID(id=self.data[0]["id"]), config=cfg))
        self.assertIsInstance(result, payload_pb2.Object.Location)

    def test_multi_remove(self):
        stub = remove_pb2_grpc.RemoveStub(self.channel)
        cfg = payload_pb2.Remove.Config(skip_strict_exist_check=True)
        requests = []
        for i in range(1, 10):
            requests.append(payload_pb2.Remove.Request(
                id=payload_pb2.Object.ID(id=self.data[i]["id"]), config=cfg))
        results = stub.MultiRemove(
            payload_pb2.Remove.MultiRequest(requests=requests))
        self.assertIsInstance(results, payload_pb2.Object.Locations)

    def test_stream_remove(self):
        stub = remove_pb2_grpc.RemoveStub(self.channel)
        cfg = payload_pb2.Remove.Config(skip_strict_exist_check=True)
        requests = []
        for i in range(11, 20):
            requests.append(payload_pb2.Remove.Request(
                id=payload_pb2.Object.ID(id=self.data[i]["id"]), config=cfg))
        results = stub.StreamRemove(iter(requests))
        for result in results:
            self.assertIsInstance(result, payload_pb2.Object.StreamLocation)
            self.assertEqual(result.status.code, 0)
