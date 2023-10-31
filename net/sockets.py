from socket import socket


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

    def recv(self, chunk) -> bytes:
        return self.sock.recv(chunk)