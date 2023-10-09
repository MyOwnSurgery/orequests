from misc.out.head import Head


class Headers:
    def __init__(self, head: Head):
        self.head = head

    def value(self) -> dict:
        splat = self.head.value().split("\r\n")

        res = {}
        for el in splat:
            if ":" not in el:
                continue
            header_name, header_val = el.split(":", maxsplit=1)
            res[header_name] = header_val.strip()

        return res
