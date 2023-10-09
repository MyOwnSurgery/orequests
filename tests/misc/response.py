import unittest

from misc.out.head import Head
from misc.response import Response
from misc.out.status import Status


class TestResponse(unittest.TestCase):
    def test_response(self):
        res = Response("www.google.com").value()

        self.assertEqual(Status(Head(input_=res)).int_value(), 200)
        self.assertIn("google.com", res)

    def test_uri(self):
        res = Response("www.google.com/doodles").value()

        self.assertEqual(Status(Head(input_=res)).int_value(), 200)
        self.assertIn("google.com", res)
