class StrInput:
    def __init__(self, input_: str):
        self.input_ = input_

    def value(self) -> str:
        return self.input_

    def bytes(self) -> bytes:
        return self.input_.encode()
