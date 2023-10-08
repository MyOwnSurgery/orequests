from functools import partial

from misc.input import Input
from retry.strategies.retry_strategy import RetryStrategy
from retry.strategies.std_retry import StdRetry
from wires.wire import Wire


class HtRetryWire:
    def __init__(
        self,
        origin: Wire,
        strategy: RetryStrategy = StdRetry(),
    ):
        self.origin = origin
        self.strategy = strategy

    def send(self, input_: Input) -> str:
        return self.strategy.retry(partial(self.origin.send, input_))
