import json
import unittest

from misc.in_.body import RawBody, JsonBody
from misc.request import (
    Request,
    GetRequest,
    PostRequest,
)


class TestRequest(unittest.TestCase):
    def test_request_with_no_body(self):
        self.assertEqual(
            Request(
                st_line="GET / HTTP/1.1",
                headers={"Connection": "Close", "Host": "www.example.com"},
            ).value(),
            "GET / HTTP/1.1\r\nConnection: Close\r\nHost: www.example.com\r\n\r\n",
        )

    def test_request_with_raw_body(self):
        input_ = '{"msg": "Hello, World!"}'
        self.assertEqual(
            Request(
                st_line="GET / HTTP/1.1",
                headers={"Connection": "Close", "Host": "www.example.com"},
                body=RawBody(input_=input_),
            ).value(),
            f"GET / HTTP/1.1\r\nConnection: Close\r\nHost: www.example.com\r\n"
            f"Content-Length: {len(input_.encode())}\r\nContent-Type: text/plain\r\n\r\n"
            '{"msg": "Hello, World!"}\r\n\r\n',
        )

    def test_request_with_json_body(self):
        input_ = {"msg": "Hello, World!"}
        self.assertEqual(
            Request(
                st_line="GET / HTTP/1.1",
                headers={"Connection": "Close", "Host": "www.example.com"},
                body=JsonBody(input_=input_),
            ).value(),
            f"GET / HTTP/1.1\r\nConnection: Close\r\nHost: www.example.com\r\n"
            f"Content-Length: {len(json.dumps(input_).encode())}\r\nContent-Type: application/json\r\n\r\n"
            '{"msg": "Hello, World!"}\r\n\r\n',
        )

    def test_get_request(self):
        self.assertEqual(
            GetRequest(
                uri="/example",
                params={"val1": 1, "val2": 2},
                headers={"Connection": "Close", "Host": "www.example.com"},
            ).value(),
            "GET /example?val1=1&val2=2 HTTP/1.1\r\nConnection: Close\r\nHost: www.example.com\r\n\r\n",
        )

    def test_post_request(self):
        input_ = {"msg": "Hello, World!"}
        self.assertEqual(
            PostRequest(
                uri="/example",
                headers={"Connection": "Close", "Host": "www.example.com"},
                body=JsonBody(input_=input_),
            ).value(),
            f"POST /example HTTP/1.1\r\nConnection: Close\r\nHost: www.example.com\r\n"
            f"Content-Length: {len(json.dumps(input_).encode())}\r\nContent-Type: application/json\r\n\r\n"
            '{"msg": "Hello, World!"}\r\n\r\n',
        )
