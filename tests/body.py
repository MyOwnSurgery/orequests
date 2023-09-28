import unittest

from misc.body import Body


class TestBody(unittest.TestCase):
    def test_body_content(self):
        response = 'HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n\r\n{"msg": "HELLO"}'
        self.assertEqual(Body(response=response).as_json(), {"msg": "HELLO"})
