from typing import Protocol

from misc.input import Input


class Wire(Protocol):
    def send(self, input_: Input) -> str:
        pass
