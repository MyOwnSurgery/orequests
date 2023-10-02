import unittest
from timeit import default_timer as timer
from retry.backoffs.uniform_backoff import UniformBackoff


class TestUniformBackoff(unittest.TestCase):
    def test_backoff_time(self):
        start_from = 1.0
        end_from = 3.0
        backoff = UniformBackoff(start=start_from, end=end_from)

        start = timer()
        backoff.sleep()
        end = timer()

        self.assertGreaterEqual(end-start, start_from)
