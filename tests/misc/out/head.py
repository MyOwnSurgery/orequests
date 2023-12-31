import unittest

from misc.out.head import Head


class TestHead(unittest.TestCase):
    def test_head_content(self):
        response = (
            'HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n\r\n{"msg": "HELLO"}'
        )
        self.assertEqual(
            Head(input_=response).value(),
            "HTTP/1.1 200 OK\r\nContent-Type: application/json",
        )
