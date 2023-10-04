from wires.ht_wire import HtWire


class Response:
    def __init__(self, address, port: int = 80):
        self.address = address
        self.port = port

    def value(self) -> str:
        return HtWire(address=self.address, port=self.port).send("\r\n".join(["GET / HTTP/1.1",
                                                                              f"Host: {self.address}",
                                                                              "Connection: Close\r\n\r\n"]))
