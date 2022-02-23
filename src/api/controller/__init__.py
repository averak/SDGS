from http import HTTPStatus
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware

from exception.error_code import ErrorCode
from exception.base_exception import BaseException
from api.response.error_response import ErrorResponse


def create_app() -> FastAPI:
    """
    Fast APIのセットアップ

    @return FastAPI app
    """

    fastapi_app: FastAPI = FastAPI()

    # CORSの設定
    fastapi_app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # OpenAPIの設定
    fastapi_app.title = "SDGS API"
    fastapi_app.description = "This is a document of SDGS."
    fastapi_app.version = "1.0.0"
    fastapi_app.openapi_tags = [
        {"name": "docs", "description": "ドキュメント"}
    ]

    @fastapi_app.exception_handler(BaseException)
    async def handle_base_exception(exception: BaseException) -> JSONResponse:
        """
        BaseException Handler
        """

        error_code = exception.get_error_code().value
        error_response = ErrorResponse(
            code=error_code.code,
            message=error_code.message
        )
        return JSONResponse(
            status_code=exception.get_status_code(),
            content=jsonable_encoder(error_response)
        )

    @fastapi_app.api_route("/{path_name:path}")
    def api_not_found_handler():
        """
        API Not Found Handler
        """

        error_code = ErrorCode.NOT_FOUND_API.value
        error_response = ErrorResponse(
            code=error_code.code,
            message=error_code.message
        )
        return JSONResponse(
            status_code=HTTPStatus.NOT_FOUND,
            content=jsonable_encoder(error_response)
        )

    return fastapi_app
