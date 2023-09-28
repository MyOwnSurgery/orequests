from typing import Protocol


class Wire(Protocol):
    def send(self, input_: str) -> str:
        pass
