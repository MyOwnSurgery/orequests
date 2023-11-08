from select import select
from socket import socket
from typing import Protocol


class _Socket(Protocol):
    def connect(self):
        pass

    def close(self):
        pass

    def send(self, input_: bytes):
        pass

    def recv(self, chunk) -> bytes:
        pass


class Socket:
    def __init__(self, addr: str, port: int):
        self.addr = addr
        self.port = port
        self.sock = socket()

    def connect(self):
        self.sock.connect((self.addr, self.port))

    def close(self):
        self.sock.close()

    def send(self, input_: bytes):
        self.sock.send(input_)

    def recv(self, *args) -> bytes:
        return self.sock.recv(*args)

    def has_some(self) -> bool:
        return bool(select([self.sock], [], [], 0)[0])
