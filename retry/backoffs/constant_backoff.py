import time


class ConstantBackoff:
    def __init__(self, value: float = 1.0):
        self.value = value

    def sleep(self):
        time.sleep(self.value)
