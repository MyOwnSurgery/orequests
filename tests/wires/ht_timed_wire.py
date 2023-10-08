import time
import unittest

from misc.input import Input
from misc.str_input import StrInput
from wires.ht_timed_wire import HtTimedWire


class SleepWire:
    def __init__(self, sleep_for: int = 5):
        self.sleep_for = sleep_for

    def send(self, input_: Input) -> str:
        time.sleep(self.sleep_for)
        return "HTTP/1.1 200 OK\r\n\r\n"


class TestTimedWire(unittest.TestCase):
    def test_timeout(self):
        with self.assertRaises(TimeoutError):
            HtTimedWire(SleepWire(sleep_for=10), 3).send(
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
