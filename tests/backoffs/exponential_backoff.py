import unittest
from timeit import default_timer as timer
from retry.backoffs.exponential_backoff import ExponentialBackoff


class TestExponentialBackoff(unittest.TestCase):
    def test_backoff_time(self):
        sleep_for = 1.0
        coeff = 2.0
        backoff = ExponentialBackoff(value=sleep_for, coeff=coeff)

        for i in [1, 2, 4, 8, 16]:
            start = timer()
            backoff.sleep()
            end = timer()

            self.assertGreaterEqual(end - start, i)
