from typing import Protocol

from misc.input import Input


class IWire(Protocol):
    def send(self, input_: Input) -> str:
        pass
