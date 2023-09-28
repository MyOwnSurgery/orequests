from typing import Optional

from misc.head import Head
from misc.status import Status
from wires.wire import Wire


class InvalidStatus(Exception):
    def __init__(self, status: int):
        self.status = status

    def __str__(self):
        return str(self.status)


class HtRetryWire:
    def __init__(
        self, origin: Wire, attempts: int = 3, retry_statuses: Optional[list] = None
    ):
        self.origin = origin
        self.attempts = attempts
        self.statuses = retry_statuses if retry_statuses else []

    def send(self, input_: str) -> str:
        attempts = 0

        errors = []
        while attempts < self.attempts:
            try:
                response = self.origin.send(input_)
            except Exception as e:
                errors.append(e)
            else:
                if (
                    self.statuses
                    and (status := Status(Head(response=response)).int_value())
                    in self.statuses
                ):
                    errors.append(InvalidStatus(status=status))
                else:
                    return response
            attempts += 1
        raise ExceptionGroup("Errors while retrying", errors)
