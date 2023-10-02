import json


class Body:
    def __init__(self, input_: str):
        self.input_ = input_

    def value(self) -> str:
        splat = self.input_.split("\r\n")
        return "\r\n".join(splat[splat.index("") :]).strip()

    def as_json(self):
        return json.loads(self.value())
