from misc.head import Head
from misc.header import Header
from wires.ht_wire import HtWire
from misc.status import Status
from wires.wire import Wire

import urllib.parse


class AutoRedirect:
    def __init__(self, origin: Wire):
        self.origin = origin

    def send(self, input_: str) -> str:
        res = self.origin.send(input_)
        head = Head(res)
        while 300 <= Status(head).int_value() <= 308:
            new_addr = urllib.parse.urlparse(Header(head, 'Location').value())
            host, port = new_addr.hostname, new_addr.port
            if not port:
                port = 443 if host.startswith('https') else 80

            res = HtWire(host, port).send(input_)
            head = Head(res)

        return res
