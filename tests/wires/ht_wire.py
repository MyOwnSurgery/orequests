import unittest

from misc.str_input import StrInput
from wires.ht_wire import HtWire


class FkConnection:
    def __init__(self, response):
        self.response = response

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def send(self, input_: bytes):
        pass

    def recv(self, chunk) -> bytes:
        return self.response


class TestHtWire(unittest.TestCase):
    def test_response_simple(self):
        response = (
            "HTTP/1.1 200 OK\r\nContent-Type: application/json"
            '\r\nContent-Length: 16\r\n\r\n{"msg": "HELLO"}'
        )
        with FkConnection(response.encode()) as conn:
            res = HtWire(conn).send(StrInput(""))

        self.assertEqual(res, response)

    def test_response_end_newline(self):
        response = (
            "HTTP/1.1 200 OK\r\nContent-Type: application/json"
            '\r\nContent-Length: 17\r\n\r\n{"msg": "HELLO"}\n'
        )
        with FkConnection(response.encode()) as conn:
            res = HtWire(conn).send(StrInput(""))

        self.assertEqual(res, response)

    def test_response_start_newline(self):
        response = (
            "HTTP/1.1 200 OK\r\nContent-Type: application/json"
            '\r\nContent-Length: 18\r\n\r\n\n{"msg": "HELLO"}\n'
        )
        with FkConnection(response.encode()) as conn:
            res = HtWire(conn).send(StrInput(""))

        self.assertEqual(res, response)

    def test_response_empty_body(self):
        response = (
            "HTTP/1.1 200 OK\r\nContent-Type: application/json"
            "\r\nContent-Length: 0\r\n\r\n"
        )
        with FkConnection(response.encode()) as conn:
            res = HtWire(conn).send(StrInput(""))

        self.assertEqual(res, response)
