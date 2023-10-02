import unittest
from timeit import default_timer as timer
from retry.backoffs.exponential_backoff import ExponentialBackoff


class TestExponentialBackoff(unittest.TestCase):
    def test_backoff_time(self):
        sleep_for = 1.0
        coeff = 2.0
        backoff = ExponentialBackoff(value=sleep_for, coeff=coeff)

        for i in range(0, 5):
            start = timer()
            backoff.sleep()
            end = timer()

            self.assertGreaterEqual(end-start, sleep_for*coeff*i if i else sleep_for)
