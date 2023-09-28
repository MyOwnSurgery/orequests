import unittest

from wires.ht_retry_wire import HtRetryWire


class ExceptionWire:
    def send(self, input_: str) -> str:
        raise Exception


class Status500Wire:
    def send(self, input_: str) -> str:
        return "HTTP/1.1 500 Internal Server Error\r\n\r\n"


class TestRetryWire(unittest.TestCase):
    def test_exceptions(self):
        with self.assertRaises(ExceptionGroup):
            HtRetryWire(ExceptionWire(), attempts=3).send(
                "\r\n".join(
                    [
                        "GET / HTTP/1.1",
                        "Host: www.google.com",
                        "Connection: Close\r\n\r\n",
                    ]
                )
            )

    def test_statuses(self):
        with self.assertRaises(ExceptionGroup):
            HtRetryWire(Status500Wire(), attempts=3, retry_statuses=[500]).send(
                "\r\n".join(
                    [
                        "GET / HTTP/1.1",
                        "Host: www.google.com",
                        "Connection: Close\r\n\r\n",
                    ]
                )
            )
