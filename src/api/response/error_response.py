from pydantic import BaseModel


class ErrorResponse(BaseModel):
    """
    エラーレスポンス
    """

    code: int
    """
    エラーコード
    """

    message: str
    """
    エラーメッセージ
    """
