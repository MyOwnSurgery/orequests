import json
from typing import Protocol


class Body(Protocol):
    def value(self) -> str:
        pass

    def bytes(self) -> bytes:
        pass


class RawBody:
    def __init__(self, input_: str):
        self.input_ = input_

    def value(self) -> str:
        return self.input_

    def bytes(self) -> bytes:
        return self.value().encode()


class JsonBody:
    def __init__(self, input_: dict):
        self.input_ = input_

    def value(self) -> str:
        return json.dumps(self.input_)

    def bytes(self) -> bytes:
        return self.value().encode()
