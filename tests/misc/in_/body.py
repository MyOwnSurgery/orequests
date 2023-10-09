import unittest

from misc.in_.body import RawBody, JsonBody


class TestBody(unittest.TestCase):
    def test_raw_body_content(self):
        input_ = '{"msg": "Hello, World!"}'
        self.assertEqual(RawBody(input_=input_).value(), '{"msg": "Hello, World!"}')

    def test_json_body_content(self):
        input_ = {"msg": "Hello, World!"}
        self.assertEqual(JsonBody(input_=input_).value(), '{"msg": "Hello, World!"}')
