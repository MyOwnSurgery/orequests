from misc.str_input import StrInput
from wires.safe_wire import SafeWire
from wires.wire import Wire

import urllib.parse


class Response:
    def __init__(self, url: str):
        self.url = url

    def value(self) -> str:
        if not (self.url.startswith("http://") or self.url.startswith("https://")):
            url = "https://" + self.url
        else:
            url = self.url

        parsed_url = urllib.parse.urlparse(url)
        host, port, scheme = parsed_url.hostname, parsed_url.port, parsed_url.scheme

        is_safe = scheme == "https"
        if not port:
            port = 443 if is_safe else 80
        wire = SafeWire(host, port) if is_safe else Wire(host, port)

        resource, params = parsed_url.path if parsed_url.path else "/", parsed_url.query
        uri = resource + (f"?{params}" if params else "")

        return wire.send(
            StrInput(
                "\r\n".join(
                    [
                        f"GET {uri} HTTP/1.1",
                        f"Host: {host}",
                        "Connection: Close\r\n\r\n",
                    ]
                )
            )
        )
