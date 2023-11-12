from misc.input import Input
from net.sessions import ShortSession
from net.sockets import SafeSocket
from wires.wire import Wire


class SafeWire:
    def __init__(self, host: str, port: int = 443):
        self.origin = Wire(ShortSession(SafeSocket(addr=host, port=port)))

    def send(self, input_: Input) -> str:
        return self.origin.send(input_=input_)
