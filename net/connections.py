from typing import Protocol, runtime_checkable

from multipledispatch import dispatch

from net.sockets import Socket


@runtime_checkable
class Connection(Protocol):
    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def send(self, input_: bytes):
        pass

    def recv(self, chunk) -> bytes:
        pass


class LongConnection:
    class _FkConnection:
        def __init__(self, sock: Socket):
            self.sock = sock

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            pass

        def send(self, input_: bytes):
            self.sock.send(input_)

        def recv(self, chunk) -> bytes:
            return self.sock.recv(chunk)

    @dispatch(str, int)
    def __init__(self, address: str, port: int):
        self.__init__(Socket(addr=address, port=port))

    @dispatch(str)
    def __init__(self, address: str):
        self.__init__(Socket(addr=address, port=80))

    @dispatch(Socket)
    def __init__(self, socket: Socket):
        self.socket = socket

    def __enter__(self):
        self.socket.connect()
        return self._FkConnection(self.socket)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.socket.close()

    def send(self, input_: bytes):
        self.socket.send(input_)

    def recv(self, chunk) -> bytes:
        return self.socket.recv(chunk)


class ShortConnection:
    @dispatch(str, int)
    def __init__(self, address: str, port: int):
        self.__init__(Socket(addr=address, port=port))

    @dispatch(str)
    def __init__(self, address: str):
        self.__init__(Socket(addr=address, port=80))

    @dispatch(Socket)
    def __init__(self, socket: Socket):
        self.socket = socket

    def __enter__(self):
        self.socket.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.socket.close()

    def send(self, input_: bytes):
        self.socket.send(input_)

    def recv(self, chunk) -> bytes:
        return self.socket.recv(chunk)
