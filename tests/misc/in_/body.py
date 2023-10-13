import json
import unittest

from misc.in_.body import RawBody, JsonBody, CachedBody


class FkBody:
    def __init__(self):
        self.call_count = 0

    def value(self) -> str:
        self.call_count += 1
        return ""

    def bytes(self) -> bytes:
        return self.value().encode()

    def content_type(self) -> str:
        return ""

    def content_length(self) -> int:
        return 0


class TestBody(unittest.TestCase):
    def test_raw_body(self):
        input_ = '{"msg": "Hello, World!"}'
        body = RawBody(input_=input_)
        self.assertEqual(body.value(), '{"msg": "Hello, World!"}')
        self.assertEqual(body.content_type(), "text/plain")
        self.assertEqual(body.content_length(), len(input_.encode()))

    def test_json_body(self):
        input_ = {"msg": "Hello, World!"}
        body = JsonBody(input_=input_)
        self.assertEqual(body.value(), '{"msg": "Hello, World!"}')
        self.assertEqual(body.content_type(), "application/json")
        self.assertEqual(body.content_length(), len(json.dumps(input_).encode()))

    def test_cached_body(self):
        cached_body = CachedBody(FkBody())
        cached_body.value()
        cached_body.bytes()
        cached_body.content_length()
        self.assertEqual(cached_body.origin.call_count, 1)
