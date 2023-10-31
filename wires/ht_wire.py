from multipledispatch import dispatch

from misc.input import Input
from misc.out.body import Body
from misc.out.head import Head
from misc.out.header import Header, NoSuchHeader
from net.connections import ShortConnection, Connection


class HtWire:
    @dispatch(str, int)
    def __init__(self, address, port):
        self.connection = ShortConnection(address, port)

    @dispatch(str)
    def __init__(self, address):
        self.connection = ShortConnection(address, 80)

    @dispatch(Connection)
    def __init__(self, connection: Connection):
        self.connection = connection

    def send(self, input_: Input) -> str:
        with self.connection as conn:
            conn.send(input_.bytes())

            response = ""
            chunks = conn.recv(4096)

            while not self._check_body_len(response := response + chunks.decode()):
                chunks = conn.recv(4096)

        return response

    # @TODO: get rid of it immediately
    @staticmethod
    def _check_body_len(s: str) -> bool:
        try:
            r_len = Header(Head(s), "Content-Length").value()
        except NoSuchHeader:
            return False

        body = Body(s).value().encode()

        if len(body) == int(r_len):
            return True

        return False
