from typing import Protocol


class BackOff(Protocol):
    def sleep(self):
        pass
