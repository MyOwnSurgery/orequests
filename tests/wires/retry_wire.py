import unittest

from misc.input import Input
from misc.str_input import StrInput
from retry.strategies.std_retry import StdRetry
from wires.retry_wire import RetryWire


class ExceptionWire:
    def send(self, input_: Input) -> str:
        raise Exception


class Status500Wire:
    def send(self, input_: Input) -> str:
        return "HTTP/1.1 500 Internal Server Error\r\n\r\n"


class TestRetryWire(unittest.TestCase):
    def test_exceptions(self):
        with self.assertRaises(ExceptionGroup):
            RetryWire(ExceptionWire()).send(
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

    def test_statuses(self):
        with self.assertRaises(ExceptionGroup):
            retry_strategy = StdRetry(retry_statuses=[500])
            RetryWire(Status500Wire(), strategy=retry_strategy).send(
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
