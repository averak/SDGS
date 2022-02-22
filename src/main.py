import uvicorn

from controller import create_app
from config.api_config import ApiConfig

app = create_app()
uvicorn.run(app, host=ApiConfig.HOST, port=ApiConfig.PORT)
