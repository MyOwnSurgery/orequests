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
        self.assertEqual(
            Request(
                st_line="GET / HTTP/1.1",
                headers={"Connection": "Close", "Host": "www.example.com"},
                body=RawBody(input_='{"msg": "Hello, World!"}'),
            ).value(),
            "GET / HTTP/1.1\r\nConnection: Close\r\nHost: www.example.com\r\n\r\n"
            '{"msg": "Hello, World!"}\r\n\r\n',
        )

    def test_request_with_json_body(self):
        self.assertEqual(
            Request(
                st_line="GET / HTTP/1.1",
                headers={"Connection": "Close", "Host": "www.example.com"},
                body=JsonBody(input_={"msg": "Hello, World!"}),
            ).value(),
            "GET / HTTP/1.1\r\nConnection: Close\r\nHost: www.example.com\r\n\r\n"
            '{"msg": "Hello, World!"}\r\n\r\n',
        )

    def test_get_request(self):
        self.assertEqual(
            GetRequest(
                uri="/example",
                headers={"Connection": "Close", "Host": "www.example.com"},
            ).value(),
            "GET /example HTTP/1.1\r\nConnection: Close\r\nHost: www.example.com\r\n\r\n",
        )

    def test_post_request(self):
        self.assertEqual(
            PostRequest(
                uri="/example",
                headers={"Connection": "Close", "Host": "www.example.com"},
                body=JsonBody(input_={"msg": "Hello, World!"}),
            ).value(),
            "POST /example HTTP/1.1\r\nConnection: Close\r\nHost: www.example.com\r\n\r\n"
            '{"msg": "Hello, World!"}\r\n\r\n',
        )
