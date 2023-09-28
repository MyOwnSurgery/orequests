from socket import socket


class HtWire:
    def __init__(self, address, port=80):
        self.address = address
        self.port = port

    def send(self, input_: str) -> str:
        with socket() as sock:
            sock.connect((self.address, self.port))
            sock.send(input_.encode())

            response = ''
            chunks = sock.recv(4096)
            while chunks:
                response += chunks.decode()
                chunks = sock.recv(4096)

        return response


if __name__ == "__main__":
    print(HtWire("demo4529285.mockable.io").send("\r\n".join([
            "GET /aboba HTTP/1.1", "Host: demo4529285.mockable.io",
            "Connection: Close\r\n\r\n"
        ])))
