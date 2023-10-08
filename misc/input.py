from typing import Protocol


class Input(Protocol):
    def value(self) -> str:
        pass

    def bytes(self) -> bytes:
        pass
