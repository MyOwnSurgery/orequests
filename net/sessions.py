from typing import Protocol, runtime_checkable

from multipledispatch import dispatch

from net.sockets import Socket, SafeSocket, ISocket


@runtime_checkable
class ISession(Protocol):
    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def send(self, input_: bytes):
        pass

    def recv(self, *args) -> bytes:
        pass

    def has_some(self) -> bool:
        pass


class _FkSession:
    def __init__(self, sock: ISocket):
        self.sock = sock

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def send(self, input_: bytes):
        self.sock.send(input_)

    def recv(self, *args) -> bytes:
        return self.sock.recv(*args)

    def has_some(self) -> bool:
        return self.sock.has_some()


class Session:
    @dispatch(str, int)
    def __init__(self, address: str, port: int):
        self.__init__(Socket(addr=address, port=port))

    @dispatch(str)
    def __init__(self, address: str):
        self.__init__(Socket(addr=address, port=80))

    @dispatch(Socket)
    def __init__(self, socket: ISocket):
        self.socket = socket

    def __enter__(self):
        self.socket.connect()
        return _FkSession(self.socket)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.socket.close()

    def send(self, input_: bytes):
        self.socket.send(input_)

    def recv(self, *args) -> bytes:
        return self.socket.recv(*args)

    def has_some(self) -> bool:
        return self.socket.has_some()


class SafeSession:
    @dispatch(str, int)
    def __init__(self, address: str, port: int):
        self.socket = SafeSocket(addr=address, port=port)

    @dispatch(str)
    def __init__(self, address: str):
        self.socket = SafeSocket(addr=address, port=80)

    def __enter__(self):
        self.socket.connect()
        return _FkSession(self.socket)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.socket.close()

    def send(self, input_: bytes):
        self.socket.send(input_)

    def recv(self, *args) -> bytes:
        return self.socket.recv(*args)

    def has_some(self) -> bool:
        return self.socket.has_some()


class ShortSession:
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

    def recv(self, *args) -> bytes:
        return self.socket.recv(*args)

    def has_some(self) -> bool:
        return self.socket.has_some()
