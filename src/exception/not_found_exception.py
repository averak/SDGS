from http import HTTPStatus

from exception.error_code import ErrorCode
from exception.base_exception import BaseException


class NotFoundException(BaseException):
    """
    404 Not Found
    """

    def __init__(self, error_code: ErrorCode):
        super().__init__(HTTPStatus.NOT_FOUND, error_code)
