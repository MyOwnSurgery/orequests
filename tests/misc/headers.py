import unittest

from misc.out.head import Head
from misc.out.headers import Headers


class TestHeaders(unittest.TestCase):
    def test_headers(self):
        response = (
            'HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n\r\n{"msg": "HELLO"}'
        )
        self.assertEqual(
            Headers(Head(input_=response)).value(),
            {"Content-Type": "application/json"},
        )
