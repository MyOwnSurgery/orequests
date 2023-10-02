import unittest

from retry.strategies.std_retry import StdRetry
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
            HtRetryWire(ExceptionWire()).send(
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
            retry_strategy = StdRetry(retry_statuses=[500])
            HtRetryWire(Status500Wire(), strategy=retry_strategy).send(
                "\r\n".join(
                    [
                        "GET / HTTP/1.1",
                        "Host: www.google.com",
                        "Connection: Close\r\n\r\n",
                    ]
                )
            )
