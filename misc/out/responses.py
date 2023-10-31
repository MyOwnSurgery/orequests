class Responses:
    def __init__(self, input_: str):
        self.input_ = input_

    def value(self) -> list[str]:
        return [x for x in self.input_.split("\r\n0\r\n\r\n") if x]
