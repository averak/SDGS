from http import HTTPStatus

from exception.error_code import ErrorCode
from exception.base_exception import BaseException


class UnauthorizedException(BaseException):
    """
    401 Unauthorized
    """

    def __init__(self, error_code: ErrorCode):
        super().__init__(HTTPStatus.UNAUTHORIZED, error_code)
