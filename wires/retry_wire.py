from functools import partial

from misc.input import Input
from retry.strategies.retry_strategy import RetryStrategy
from retry.strategies.std_retry import StdRetry
from wires.iwire import IWire


class RetryWire:
    def __init__(
        self,
        origin: IWire,
        strategy: RetryStrategy = StdRetry(),
    ):
        self.origin = origin
        self.strategy = strategy

    def send(self, input_: Input) -> str:
        return self.strategy.retry(partial(self.origin.send, input_))
