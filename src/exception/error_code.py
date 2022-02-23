from enum import Enum


class ErrorCode(Enum):
    """
    エラーコードのEnum
    """

    class Error:
        """
        エラークラス
        """

        code: int
        """
        エラーコード
        """

        message: str
        """
        エラーメッセージ
        """

        def __init__(self, code: int, message: str):
            self.code = code
            self.message = message

    """
    500 Internal Server Error: 1000~1999
    """
    UNEXPECTED_ERROR = Error(1000, "予期しないエラーが発生しました")
