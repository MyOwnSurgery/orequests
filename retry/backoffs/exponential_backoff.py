import time


class ExponentialBackoff:
    def __init__(self, value: float = 1.0, coeff: float = 2.0):
        self.value = value
        self.coeff = coeff
        self.count = 1

    def sleep(self):
        time.sleep(self.count * self.value)
        self.count *= self.coeff  # TODO: get rid of immutability violation
