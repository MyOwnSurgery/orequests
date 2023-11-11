import unittest

from misc.out.head import Head
from misc.input import Input
from misc.out.status import Status
from misc.str_input import StrInput
from wires.autoredirect import AutoRedirect
from wires.wire import Wire


class RedirectWire:
    def send(self, input_: Input) -> str:
        return "HTTP/1.1 301 Moved Permanently\r\nLocation: https://www.google.com/\r\n\r\n"


class TestAutoRedirect(unittest.TestCase):
    def test_redirect(self):
        res_head = Head(
            AutoRedirect(RedirectWire()).send(
                StrInput(
                    "\r\n".join(
                        [
                            "GET / HTTP/1.1",
                            "Host: www.google.com",
                            "Connection: Close\r\n\r\n",
                        ]
                    )
                )
            )
        )
        self.assertEqual(Status(res_head).int_value(), 200)
        self.assertIn("google.com", res_head.value())

    def test_real_redirect(self):
        """Test a read redirect from google.com to www.google.com"""
        res_head = Head(
            AutoRedirect(Wire("google.com")).send(
                StrInput(
                    "\r\n".join(
                        [
                            "GET / HTTP/1.1",
                            "Host: google.com",
                            "Connection: Close\r\n\r\n",
                        ]
                    )
                )
            )
        )
        self.assertEqual(Status(res_head).int_value(), 200)
        self.assertIn("google.com", res_head.value())
