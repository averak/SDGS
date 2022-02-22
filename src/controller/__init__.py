from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def create_app() -> FastAPI:
    """
    Fast APIのセットアップ

    @return FastAPI app
    """

    fastapi_app: FastAPI = FastAPI()
    fastapi_app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    )

    # OpenAPIの設定
    fastapi_app.title = 'SDGS API'
    fastapi_app.description = 'This is a document of SDGS.'
    fastapi_app.version = '1.0.0'
    fastapi_app.openapi_tags = [
        {"name": "docs", "description": "ドキュメント"}
    ]

    return fastapi_app
