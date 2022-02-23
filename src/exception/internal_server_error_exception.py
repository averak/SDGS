from http import HTTPStatus

from exception.error_code import ErrorCode
from exception.base_exception import BaseException


class InternalServerErrorException(BaseException):
    """
    500 Internal Server Error
    """

    def __init__(self, error_code: ErrorCode):
        super().__init__(HTTPStatus.INTERNAL_SERVER_ERROR, error_code)
