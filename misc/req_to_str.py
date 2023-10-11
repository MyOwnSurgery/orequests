from io import StringIO
from typing import Optional

from misc.in_.body import Body


class ReqToStr:
    def __init__(
        self, st_line: str, headers: Optional[dict] = None, body: Optional[Body] = None
    ):
        self.st_line = st_line
        self.headers = headers if headers else {}
        self.body = body

    def value(self):
        with StringIO() as stream:
            stream.write(f"{self.st_line}\r\n")

            for h_name, h_val in self.headers.items():
                stream.write(f"{h_name}: {h_val}\r\n")
            stream.write("\r\n")

            if self.body:
                stream.write(self.body.value())
                stream.write("\r\n\r\n")

            input_ = stream.getvalue()

        return input_
