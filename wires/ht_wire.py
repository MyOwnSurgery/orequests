from multipledispatch import dispatch

from misc.input import Input
from misc.out.body import Body
from misc.out.head import Head
from misc.out.header import Header, NoSuchHeader
from net.connections import ShortConnection, Connection


class HtWire:
    @dispatch(str, int)
    def __init__(self, address: str, port: int):
        self.connection = ShortConnection(address, port)

    @dispatch(str)
    def __init__(self, address: str):
        self.connection = ShortConnection(address, 80)

    @dispatch(Connection)
    def __init__(self, connection: Connection):
        self.connection = connection

    def send(self, input_: Input) -> str:
        with self.connection as conn:
            conn.send(input_.bytes())

            response = ""

            while True:
                while conn.has_some():
                    chunk = conn.recv(4096)
                    response = response + chunk.decode()

                if self._check_body_len(response):
                    return response

                response = response + conn.recv(4096).decode()

    # @TODO: get rid of it immediately
    # @TODO: handle chunked first
    @staticmethod
    def _check_body_len(s: str) -> bool:
        head = Head(s)
        try:
            r_len = Header(head, "Content-Length").value()
        except NoSuchHeader:
            try:
                if (Header(head, "Transfer-Encoding").value() == 'chunked'
                        and s.endswith('\r\n0\r\n\r\n')):
                    return True
            except NoSuchHeader:
                return False
            return False

        body = Body(s).value().encode()
        if len(body) >= int(r_len):
            return True

        return False
