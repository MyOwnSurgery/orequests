from misc.out.head import Head


class NoSuchHeader(Exception):
    pass


class Header:
    def __init__(self, head: Head, name: str):
        self.head = head
        self.name = name

    def value(self) -> str:
        splat = self.head.value().split("\r\n")

        for i, el in enumerate(splat):
            if f"{self.name}:" in splat[i]:
                return splat[i].split(":", maxsplit=1)[1].strip()

        raise NoSuchHeader
