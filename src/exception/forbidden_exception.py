from http import HTTPStatus

from exception.error_code import ErrorCode
from exception.base_exception import BaseException


class ForbiddenException(BaseException):
    """
    403 Forbidden
    """

    def __init__(self, error_code: ErrorCode):
        super().__init__(HTTPStatus.FORBIDDEN, error_code)
