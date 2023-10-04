import unittest

from misc.response import Response


class TestResponse(unittest.TestCase):
    def test_timeout(self):
        res = Response("www.google.com").send()

        self.assertIn('google.com', res)
