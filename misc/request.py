import functools
from io import StringIO
from functools import reduce
from typing import Optional

from misc.in_.body import Body, CachedBody


class Request:
    def __init__(
        self,
        st_line: str,
        params: Optional[dict] = None,
        headers: Optional[dict] = None,
        body: Optional[Body] = None,
    ):
        self.st_line = st_line
        self.params = params
        self.headers = headers.copy() if headers else {}
        self.body = body

    def bytes(self) -> bytes:
        return self.value().encode()

    def value(self) -> str:
        if self.params:
            splat_st_line = self.st_line.split(" ")
            splat_st_line[1] += "?" + "&".join(
                [f"{k}={v}" for k, v in self.params.items()]
            )
            st_line = " ".join(splat_st_line)
        else:
            st_line = self.st_line

        body = CachedBody(self.body) if self.body else None
        if body:
            self.headers["Content-Length"] = body.content_length()
            self.headers["Content-Type"] = body.content_type()

        with StringIO() as stream:
            stream.write(f"{st_line}\r\n")

            for h_name, h_val in self.headers.items():
                stream.write(f"{h_name}: {h_val}\r\n")
            stream.write("\r\n")

            if body:
                stream.write(body.value())
                stream.write("\r\n\r\n")

            input_ = stream.getvalue()

        return input_


class GetRequest:
    def __init__(
        self,
        uri: str = "/",
        params: Optional[dict] = None,
        headers: Optional[dict] = None,
    ):
        self.origin = Request(
            st_line=f"GET {uri} HTTP/1.1", params=params, headers=headers
        )

    def bytes(self) -> bytes:
        return self.origin.bytes()

    def value(self) -> str:
        return self.origin.value()


class PostRequest:
    def __init__(
        self,
        uri: str = "/",
        headers: Optional[dict] = None,
        body: Optional[Body] = None,
    ):
        self.origin = Request(
            st_line=f"POST {uri} HTTP/1.1", headers=headers, body=body
        )

    def bytes(self) -> bytes:
        return self.origin.bytes()

    def value(self) -> str:
        return self.origin.value()


class PutRequest:
    def __init__(
        self,
        uri: str = "/",
        headers: Optional[dict] = None,
        body: Optional[Body] = None,
    ):
        self.origin = Request(st_line=f"PUT {uri} HTTP/1.1", headers=headers, body=body)

    def bytes(self) -> bytes:
        return self.origin.bytes()

    def value(self) -> str:
        return self.origin.value()


class PatchRequest:
    def __init__(
        self,
        uri: str = "/",
        headers: Optional[dict] = None,
        body: Optional[Body] = None,
    ):
        self.origin = Request(
            st_line=f"PATCH {uri} HTTP/1.1", headers=headers, body=body
        )

    def bytes(self) -> bytes:
        return self.origin.bytes()

    def value(self) -> str:
        return self.origin.value()


class DeleteRequest:
    def __init__(self, uri: str = "/", headers: Optional[dict] = None):
        self.origin = Request(st_line=f"DELETE {uri} HTTP/1.1", headers=headers)

    def bytes(self) -> bytes:
        return self.origin.bytes()

    def value(self) -> str:
        return self.origin.value()


class CompoundRequest:
    def __init__(self, requests: list[Request]):
        self.requests = requests

    def bytes(self) -> bytes:
        return functools.reduce(lambda a, b: a + b, (req.bytes() for req in self.requests))

    def value(self) -> str:
        return functools.reduce(lambda a, b: a + b, (req.value() for req in self.requests))
