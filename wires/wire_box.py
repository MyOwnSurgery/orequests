# @TODO: reconsider
from wires.iwire import IWire
from wires.safe_wire import SafeWire
from wires.wire import Wire


class WireBox:
    def __init__(self, host: str, port: int, scheme: str):
        self.host = host
        self.port = port
        self.scheme = scheme

    def wire(self) -> IWire:
        is_safe = self.scheme == "https"
        port = self.port
        if not port:
            port = 443 if is_safe else 80
        return SafeWire(self.host, port) if is_safe else Wire(self.host, port)
