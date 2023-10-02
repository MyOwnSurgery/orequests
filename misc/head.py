class Head:
    def __init__(self, input_: str):
        self.input_ = input_

    def value(self) -> str:
        splat = self.input_.split("\r\n")
        return "\r\n".join(splat[: splat.index("")]).strip()
