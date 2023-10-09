from misc.out.head import Head


class Status:
    def __init__(self, head: Head):
        self.head = head

    def value(self):
        return self.head.value().split("\r\n")[0]

    def int_value(self):
        return int(self.value().split(" ")[1])
