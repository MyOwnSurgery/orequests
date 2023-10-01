import time


class ConstantBackoff:
    def __init__(self, value: float = 1.0):
        self.value = value

    def sleep(self):
        return time.sleep(self.value)
