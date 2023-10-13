import unittest

from misc.in_.body import RawBody, JsonBody, CachedBody


class FkBody:
    def __init__(self):
        self.call_count = 0

    def value(self) -> str:
        self.call_count += 1
        return ''

    def bytes(self) -> bytes:
        return self.value().encode()

    def content_type(self) -> str:
        return ''

    def content_length(self) -> int:
        return 0


class TestBody(unittest.TestCase):
    def test_raw_body_content(self):
        input_ = '{"msg": "Hello, World!"}'
        self.assertEqual(RawBody(input_=input_).value(), '{"msg": "Hello, World!"}')

    def test_json_body_content(self):
        input_ = {"msg": "Hello, World!"}
        self.assertEqual(JsonBody(input_=input_).value(), '{"msg": "Hello, World!"}')

    def test_cached_body(self):
        cached_body = CachedBody(FkBody())
        cached_body.value()
        cached_body.bytes()
        cached_body.content_length()
        self.assertEqual(cached_body.origin.call_count, 1)
