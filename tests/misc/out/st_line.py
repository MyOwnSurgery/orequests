import unittest

from misc.out.head import Head
from misc.out.st_line import StLine


class TestStLine(unittest.TestCase):
    def test_content(self):
        request = "GET / HTTP/1.1\r\nHost: www.google.com\r\nConnection: Close\r\n\r\n"
        self.assertEqual(
            StLine(Head(input_=request)).value(),
            "GET / HTTP/1.1",
        )
