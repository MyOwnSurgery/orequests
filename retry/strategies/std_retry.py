from typing import Callable, Optional

from misc.out.head import Head
from misc.out.status import Status
from retry.backoffs.backoff import BackOff
from retry.backoffs.no_backoff import NoBackoff


class InvalidStatus(Exception):
    def __init__(self, status: int):
        self.status = status

    def __str__(self):
        return str(self.status)


class StdRetry:
    def __init__(
        self,
        total: int = 3,
        retry_statuses: Optional[list] = None,
        backoff: BackOff = NoBackoff(),
    ):
        self.total = total
        self.statuses = retry_statuses if retry_statuses else []
        self.backoff = backoff

    def retry(self, target: Callable):
        attempts = 0

        errors = []
        while attempts < self.total:
            try:
                response = target()
            except Exception as e:
                errors.append(e)
            else:
                if (
                    self.statuses
                    and (status := Status(Head(input_=response)).int_value())
                    in self.statuses
                ):
                    errors.append(InvalidStatus(status=status))
                else:
                    return response
            attempts += 1
            if attempts < self.total:
                self.backoff.sleep()
        raise ExceptionGroup("Errors while retrying", errors)
