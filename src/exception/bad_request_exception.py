from http import HTTPStatus

from exception.error_code import ErrorCode
from exception.base_exception import BaseException


class BadRequestException(BaseException):
    """
    400 Bad Request
    """

    def __init__(self, error_code: ErrorCode):
        super().__init__(HTTPStatus.BAD_REQUEST, error_code)
