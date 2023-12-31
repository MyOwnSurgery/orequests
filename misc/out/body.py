import json


class Body:
    def __init__(self, input_: str):
        self.input_ = input_

    def value(self) -> str:
        splat = self.input_.split("\r\n\r\n")
        return splat[1]


class JsonBody:
    def __init__(self, origin: Body):
        self.origin = origin

    def value(self) -> dict:
        return json.loads(self.origin.value())


class MultipleBodies:
    def __init__(self, input_: str):
        self.input_ = input_

    def value(self):
        return
