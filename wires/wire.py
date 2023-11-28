from multipledispatch import dispatch

from misc.input import Input
from misc.out.body import Body
from misc.out.head import Head
from misc.out.header import Header, NoSuchHeader
from misc.out.headers import Headers
from net.sessions import ShortSession, ISession


class Wire:
    @dispatch(str, int)
    def __init__(self, address: str, port: int):
        self.session = ShortSession(address, port)

    @dispatch(str)
    def __init__(self, address: str):
        self.session = ShortSession(address, 80)

    @dispatch(ISession)
    def __init__(self, session: ISession):
        self.session = session

    def send(self, input_: Input) -> str:
        with self.session as conn:
            conn.send(input_.bytes())

            response = ""

            while True:
                while conn.has_some():
                    chunk = conn.recv(4096)
                    response = response + chunk.decode()

                if self._check_body_len(response):
                    return response

                response = response + conn.recv(4096).decode()

    # @TODO: refactor in more oop style
    @staticmethod
    def _check_body_len(s: str) -> bool:
        head = Head(s)

        try:
            headers = Headers(head).value()
        except (IndexError, ValueError):
            return False

        if headers.get("Transfer-Encoding", None) == "chunked" and s.endswith(
            "\r\n0\r\n\r\n"
        ):
            return True

        ct_len = headers.get("Content-Length", None)
        if ct_len and int(ct_len) == len(Body(s).value().encode()):
            return True

        return False
