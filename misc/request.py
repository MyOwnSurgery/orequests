from io import StringIO
from typing import Optional

from misc.in_.body import Body
from misc.req_to_str import ReqToStr


class Request:
    def __init__(
        self, st_line: str, headers: Optional[dict] = None, body: Optional[Body] = None
    ):
        self.st_line = st_line
        self.headers = headers
        self.body = body

    def bytes(self) -> bytes:
        return self.value().encode()

    def value(self) -> str:
        return ReqToStr(self.st_line, self.headers, self.body).value()


class GetRequest:
    def __init__(self, uri: str = "", headers: Optional[dict] = None):
        self.uri = uri if uri else "/"
        self.headers = headers

    def bytes(self) -> bytes:
        return self.value().encode()

    def value(self) -> str:
        return ReqToStr(
            st_line=f"GET {self.uri} HTTP/1.1", headers=self.headers
        ).value()


class PostRequest:
    def __init__(
        self, uri: str = "", headers: Optional[dict] = None, body: Optional[Body] = None
    ):
        self.uri = uri if uri else "/"
        self.headers = headers
        self.body = body

    def bytes(self) -> bytes:
        return self.value().encode()

    def value(self) -> str:
        return ReqToStr(
            st_line=f"POST {self.uri} HTTP/1.1", headers=self.headers, body=self.body
        ).value()


class PutRequest:
    def __init__(
        self, uri: str = "", headers: Optional[dict] = None, body: Optional[Body] = None
    ):
        self.uri = uri if uri else "/"
        self.headers = headers
        self.body = body

    def bytes(self) -> bytes:
        return self.value().encode()

    def value(self) -> str:
        return ReqToStr(
            st_line=f"PUT {self.uri} HTTP/1.1", headers=self.headers, body=self.body
        ).value()


class PatchRequest:
    def __init__(
        self, uri: str = "", headers: Optional[dict] = None, body: Optional[Body] = None
    ):
        self.uri = uri if uri else "/"
        self.headers = headers
        self.body = body

    def bytes(self) -> bytes:
        return self.value().encode()

    def value(self) -> str:
        return ReqToStr(
            st_line=f"PATCH {self.uri} HTTP/1.1", headers=self.headers, body=self.body
        ).value()


class DeleteRequest:
    def __init__(self, uri: str = "", headers: Optional[dict] = None):
        self.uri = uri
        self.headers = headers

    def bytes(self) -> bytes:
        return self.value().encode()

    def value(self) -> str:
        return ReqToStr(
            st_line=f"DELETE {self.uri} HTTP/1.1", headers=self.headers
        ).value()
