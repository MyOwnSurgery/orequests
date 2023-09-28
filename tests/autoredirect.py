from misc.head import Head
from misc.status import Status
from wires.autoredirect import AutoRedirect


class RedirectWire:
    def send(self, input_: str) -> str:
        return "HTTP/1.1 301 Moved Permanently\r\nLocation: https://www.google.com/\r\n\r\n"


res_head = Head(AutoRedirect(RedirectWire()).send("\r\n".join([
    "GET / HTTP/1.1", "Host: www.google.com",
    "Connection: Close\r\n\r\n"
])))

assert Status(res_head).int_value() == 200
assert 'google.com' in res_head.value()
