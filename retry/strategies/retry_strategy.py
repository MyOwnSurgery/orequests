from typing import Protocol, Callable


class RetryStrategy(Protocol):
    def retry(self, target: Callable):
        pass
