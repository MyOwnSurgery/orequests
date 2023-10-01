import time


class ExponentialBackoff:
    def __init__(self, value: float, coeff: float):
        self.value = value
        self.coeff = coeff
        self.count = 1

    def sleep(self):
        time.sleep(self.count * self.coeff * self.value)
        self.count += 1  # TODO: get rid of immutability violation