import unittest

from misc.response import Response


class TestResponse(unittest.TestCase):
    def test_timeout(self):
        res = Response("www.google.com").value()

        self.assertIn('google.com', res)
