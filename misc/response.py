from wires.ht_wire import HtWire

import urllib.parse


class Response:
    def __init__(self, url: str):
        self.url = url

    def value(self) -> str:
        if self.url.startswith('http'):
            port = 80
        elif self.url.startswith('https'):
            port = 443
        else:
            self.url = 'http://' + self.url
            port = 80

        parsed_url = urllib.parse.urlparse(self.url)
        host, port = parsed_url.hostname, parsed_url.port if parsed_url.port else port
        resource, params = parsed_url.path, parsed_url.query

        return HtWire(address=host, port=port).send("\r\n".join([f"GET {resource}?{params} HTTP/1.1",
                                                                 f"Host: {host}",
                                                                 "Connection: Close\r\n\r\n"]))
