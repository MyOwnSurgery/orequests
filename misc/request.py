from io import StringIO
from typing import Optional


class Request:
    def __init__(
        self, st_line: str, headers: Optional[dict] = None, body: Optional[str] = None
    ):
        self.st_line = st_line
        self.headers = headers if headers else {}
        self.body = body

    def bytes(self) -> bytes:
        return self.value().encode()

    def value(self) -> str:
        with StringIO() as stream:
            stream.write(f"{self.st_line}\r\n")

            for h_name, h_val in self.headers.items():
                stream.write(f"{h_name}: {h_val}\r\n")
            stream.write("\r\n")

            if self.body:
                stream.write(self.body)
                stream.write("\r\n\r\n")

            input_ = stream.getvalue()

        return input_
