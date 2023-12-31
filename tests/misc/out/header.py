import unittest

from misc.out.head import Head
from misc.out.header import Header


class TestHeader(unittest.TestCase):
    def test_header_content(self):
        response = (
            'HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n\r\n{"msg": "HELLO"}'
        )
        self.assertEqual(
            Header(Head(input_=response), "Content-Type").value(), "application/json"
        )
