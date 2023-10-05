from misc.body import Body
from misc.head import Head
from misc.header import Header
from misc.headers import Headers
from misc.st_line import StLine
from wires.ht_wire import HtWire
from misc.status import Status
from wires.wire import Wire

import io
import urllib.parse


class AutoRedirect:
    def __init__(self, origin: Wire):
        self.origin = origin

    def send(self, input_: str) -> str:
        res = self.origin.send(input_)
        head = Head(res)
        while 300 <= Status(head).int_value() <= 308:
            new_addr = urllib.parse.urlparse(Header(head, "Location").value())
            host, port = new_addr.hostname, new_addr.port

            input_head, input_body = Head(input_), Body(input_)
            start_line = StLine(input_head).value()
            headers = Headers(input_head).value()
            headers["Host"] = host

            with io.StringIO() as stream:
                stream.write(start_line + "\r\n")
                stream.writelines(f"{k}: {v}\r\n" for k, v in headers.items())
                stream.write(input_body.value() + "\r\n\r\n")
                new_input = stream.getvalue()

            if not port:
                port = 443 if host.startswith("https") else 80

            res = HtWire(host, port).send(new_input)
            head = Head(res)

        return res
