class Head:
    def __init__(self, response: str):
        self.response = response

    def value(self) -> str:
        splat = self.response.split("\r\n")
        return '\r\n'.join(splat[:splat.index('')]).strip()
