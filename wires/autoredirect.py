import urllib.parse

from misc.in_.body import RawBody
from misc.input import Input
from misc.out.body import Body
from misc.out.head import Head
from misc.out.header import Header
from misc.out.headers import Headers
from misc.out.st_line import StLine
from misc.out.status import Status
from misc.request import Request
from wires.iwire import IWire
from wires.wire_box import WireBox


class AutoRedirect:
    def __init__(self, origin: IWire):
        self.origin = origin

    # @TODO: Refactor
    def send(self, input_: Input) -> str:
        res = self.origin.send(input_)
        head = Head(res)
        while 300 <= Status(head).int_value() <= 308:
            new_addr = urllib.parse.urlparse(Header(head, "Location").value())
            host, port, scheme = new_addr.hostname, new_addr.port, new_addr.scheme

            new_wire = WireBox(host=host, port=port, scheme=scheme).wire()

            input_val = input_.value()
            input_head, input_body = Head(input_val), Body(input_val)
            start_line = StLine(input_head).value()
            headers = Headers(input_head).value()
            headers["Host"] = host

            new_body = input_body.value()
            new_request = Request(
                st_line=start_line,
                headers=headers,
                body=RawBody(new_body, ct_type=headers["Content-Type"])
                if new_body
                else None,
            )

            res = new_wire.send(new_request)
            head = Head(res)

        return res
