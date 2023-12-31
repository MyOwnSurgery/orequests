import multiprocessing.context
from multiprocessing.pool import ThreadPool

from misc.input import Input
from wires.iwire import IWire


class TimedWire:
    def __init__(self, origin: IWire, timeout: float):
        self.origin = origin
        self.timeout = timeout

    def send(self, input_: Input) -> str:
        try:
            with ThreadPool(1) as pool:
                result = pool.apply_async(self.origin.send, args=(input_,))
                return result.get(timeout=self.timeout)
        except multiprocessing.context.TimeoutError as e:
            raise TimeoutError from e
