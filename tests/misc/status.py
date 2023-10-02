import unittest

from misc.head import Head
from misc.status import Status


class TestStatus(unittest.TestCase):
    def test_content(self):
        response = "HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n\r\n{'msg': 'HELLO'}"
        self.assertEqual(
            Status(Head(input_=response)).value(),
            "HTTP/1.1 200 OK",
        )
        self.assertEqual(
            Status(Head(input_=response)).int_value(),
            200
        )
