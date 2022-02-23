from exception.error_code import ErrorCode


class BaseException(Exception):
    """
    カスタム例外の基底クラス
    """

    __status_code: int
    """
    ステータスコード
    """

    __error_code: ErrorCode
    """
    エラーコード
    """

    def __init__(self, status_code: int, error_code: ErrorCode):
        self.__status_code = status_code
        self.__error_code = error_code

    def get_status_code(self) -> int:
        """
        ステータスコードのGetter

        @return ステータスコード
        """
        return self.__status_code

    def get_error_code(self) -> ErrorCode:
        """
        エラーコードのGetter

        @return エラーコード
        """

        return self.__error_code.value
