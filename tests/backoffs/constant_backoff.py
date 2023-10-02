import unittest
from timeit import default_timer as timer
from retry.backoffs.constant_backoff import ConstantBackoff


class TestConstantBackoff(unittest.TestCase):
    def test_backoff_time(self):
        sleep_for = 1.0
        backoff = ConstantBackoff(value=sleep_for)
        start = timer()
        backoff.sleep()
        end = timer()

        self.assertGreaterEqual(end - start, sleep_for)
