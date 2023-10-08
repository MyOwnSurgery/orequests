from misc.str_input import StrInput
from wires.ht_wire import HtWire

import urllib.parse


class Response:
    def __init__(self, url: str):
        self.url = url

    def value(self) -> str:
        if self.url.startswith("https"):
            port = 443
        else:
            if not self.url.startswith("http"):
                self.url = "http://" + self.url
            port = 80

        parsed_url = urllib.parse.urlparse(self.url)
        host, port = parsed_url.hostname, parsed_url.port if parsed_url.port else port
        resource, params = parsed_url.path if parsed_url.path else "/", parsed_url.query

        uri = resource + (f"?{params}" if params else "")
        return HtWire(address=host, port=port).send(
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
