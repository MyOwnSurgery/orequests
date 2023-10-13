import json
from copy import copy
from functools import cache
from typing import Protocol


class Body(Protocol):
    def value(self) -> str:
        pass

    def bytes(self) -> bytes:
        pass

    def content_type(self) -> str:
        pass

    def content_length(self) -> int:
        pass


class RawBody:
    def __init__(self, input_: str, ct_type: str = "text/plain"):
        self.input_ = input_
        self.ct_type = ct_type

    def value(self) -> str:
        return self.input_

    def bytes(self) -> bytes:
        return self.value().encode()

    def content_length(self) -> int:
        return len(self.bytes())

    def content_type(self) -> str:
        return self.ct_type


class JsonBody:
    def __init__(self, input_: dict):
        self.input_ = input_

    def value(self) -> str:
        return json.dumps(self.input_)

    def content_length(self) -> int:
        return len(self.bytes())

    def bytes(self) -> bytes:
        return self.value().encode()

    def content_type(self) -> str:
        return "application/json"


class CachedBody:
    # @TODO: find a less brutal way to cache
    def __init__(self, origin: Body):
        self.origin = copy(origin)
        self.origin.value = cache(self.origin.value)

    def value(self):
        return self.origin.value()

    def bytes(self):
        return self.origin.bytes()

    def content_length(self):
        return self.origin.content_length()

    def content_type(self):
        return self.origin.content_type()
