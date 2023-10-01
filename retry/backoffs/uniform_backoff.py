import time
from random import uniform


class UniformBackoff:
    def __init__(self, start: float = 1.0, end: float = 3.0):
        self.start = start
        self.end = end

    def sleep(self):
        time.sleep(uniform(a=self.start, b=self.end))
