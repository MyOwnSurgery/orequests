import unittest

from misc.head import Head
from misc.start_line import StartLine


class TestStartLine(unittest.TestCase):
    def test_content(self):
        request = "GET / HTTP/1.1\r\nHost: www.google.com\r\nConnection: Close\r\n\r\n"
        self.assertEqual(
            StartLine(Head(input_=request)).value(),
            "GET / HTTP/1.1",
        )
