from socket import socket


class HtWire:
    def __init__(self, address, port=80):
        self.address = address
        self.port = port

    def send(self, input_: str) -> str:
        with socket() as sock:
            sock.connect((self.address, self.port))
            sock.send(input_.encode())

            response = ""
            chunks = sock.recv(4096)
            while chunks:
                response += chunks.decode()
                chunks = sock.recv(4096)

        return response
