from misc.head import Head


class StartLine:
    def __init__(self, head: Head):
        self.head = head

    def value(self):
        return self.head.value().split("\r\n")[0]
