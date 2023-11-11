import ssl
from select import select
from socket import socket, MSG_PEEK
from typing import Protocol


class ISocket(Protocol):
    def connect(self):
        pass

    def close(self):
        pass

    def send(self, input_: bytes):
        pass

    def recv(self, chunk) -> bytes:
        pass

    def has_some(self) -> bool:
        pass


class Socket:
    def __init__(self, addr: str, port: int, sock: socket = None):
        self.addr = addr
        self.port = port
        self.sock = sock if sock else socket()

    def connect(self):
        self.sock.connect((self.addr, self.port))

    def close(self):
        self.sock.close()

    def send(self, input_: bytes):
        self.sock.send(input_)

    def recv(self, *args) -> bytes:
        return self.sock.recv(*args)

    def has_some(self) -> bool:
        return bool(select([self.sock], [], [], 0)[0]) and self.recv(1, MSG_PEEK)


class SafeSocket:
    def __init__(
        self, addr: str, port: int, sock: socket = None, ssl_ctx: ssl.SSLContext = None
    ):
        self.origin = Socket(
            addr,
            port,
            (ssl_ctx or ssl.create_default_context()).wrap_socket(
                sock or socket(), server_hostname=addr
            ),
        )

    def connect(self):
        self.origin.connect()

    def close(self):
        self.origin.close()

    def send(self, input_: bytes):
        self.origin.send(input_=input_)

    def recv(self, *args) -> bytes:
        return self.origin.recv(*args)

    def has_some(self) -> bool:
        return self.origin.has_some()
