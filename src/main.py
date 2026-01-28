from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.exceptions import HTTPException, RequestValidationError
from fastapi.requests import Request
from fastapi.responses import JSONResponse, Response
from fastapi.staticfiles import StaticFiles
from jder_fastapi.handlers import (
    request_validation_exception_handler,
)
from jder_fastapi.responses.json import (
    CreateJsonFailureResponseOptions,
    JsonResponseError,
    createJsonResponse,
)
from scalar_fastapi import (
    Theme,
    get_scalar_api_reference,  # type: ignore
)

from src.classes.enums.error import (
    ResponseErrorCode,
    get_response_error_message,
)
from src.configs.log import logger
from src.configs.vars import ROOT, get_py_env
from src.router.main import router


def load_env(
    name: str,
    path: Path,
) -> None:
    if Path.is_file(path):
        load_dotenv(
            dotenv_path=path,
            override=True,
        )

        logger.info(f"Environment loaded: {name}")


py_env: str = get_py_env()

env: str = ".env"

load_env(
    name=env,
    path=Path(ROOT) / env,
)

env: str = ".env.local"

load_env(
    name=env,
    path=Path(ROOT) / env,
)

env: str = f".env.{py_env}"

load_env(
    name=env,
    path=Path(ROOT) / env,
)

env: str = f".env.{py_env}.local"

load_env(
    name=env,
    path=Path(ROOT) / env,
)

app: FastAPI = FastAPI()

app.include_router(router)


@app.get("/openapi", include_in_schema=False)
async def route_api() -> Response:
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title=app.title,
        theme=Theme.NONE,
    )


app.mount("/", StaticFiles(directory=Path(ROOT) / "public"), name="static")


@app.exception_handler(404)
async def not_found(_: Request, exc: HTTPException) -> JSONResponse:
    code: ResponseErrorCode = ResponseErrorCode.NOT_FOUND

    return createJsonResponse(
        options=CreateJsonFailureResponseOptions(
            status=exc.status_code,
            headers=exc.headers or {},
            errors=[
                JsonResponseError(
                    code=code, message=get_response_error_message(code)
                )
            ],
        )
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    req: Request, exc: RequestValidationError
) -> Response:
    return request_validation_exception_handler(req, exc)
