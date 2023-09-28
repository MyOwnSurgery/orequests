import multiprocessing.context
from multiprocessing.pool import ThreadPool

from wires.wire import Wire


class HtTimedWire:
    def __init__(self, origin: Wire, timeout: float):
        self.origin = origin
        self.timeout = timeout

    def send(self, input_: str) -> str:
        try:
            with ThreadPool(1) as pool:
                result = pool.apply_async(self.origin.send, args=(input_,))
                return result.get(timeout=self.timeout)
        except multiprocessing.context.TimeoutError as e:
            raise TimeoutError from e
