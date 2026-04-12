from contextlib import asynccontextmanager
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
from starlette.exceptions import HTTPException as StarletteHTTPException

from src.classes.enums.error import (
    ResponseErrorCode,
    get_response_error_message,
)
from src.configs.log import logger
from src.configs.vars import ROOT, get_py_env
from src.middlewares.on_exception import on_exception_handler
from src.router.main import router


def load_env_file(
    path: Path,
    name: str,
) -> None:
    if not path.exists():
        return

    load_dotenv(
        dotenv_path=path,
        override=True,
    )

    logger.info(f"Environment loaded: {name}")


def load_env_files(
    root: Path,
    py_env: str,
) -> None:
    files: list[str] = [
        ".env",
        ".env.local",
        f".env.{py_env}",
        f".env.{py_env}.local",
    ]

    for file in files:
        load_env_file(
            path=root / file,
            name=file,
        )


@asynccontextmanager
async def lifespan(_: FastAPI):
    py_env: str = get_py_env()

    load_env_files(
        root=Path(ROOT),
        py_env=py_env,
    )

    yield


app: FastAPI = FastAPI(lifespan=lifespan)

app.include_router(router)


@app.get("/openapi", include_in_schema=False)
async def route_api() -> Response:
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title=app.title,
        theme=Theme.NONE,
    )


app.mount("/", StaticFiles(directory=Path(ROOT) / "public"), name="static")


@app.exception_handler(StarletteHTTPException)
async def not_found(_: Request, exc: StarletteHTTPException) -> Response:
    match exc.status_code:
        case 404:
            code = ResponseErrorCode.NOT_FOUND
        case _:
            code = ResponseErrorCode.SERVER

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


@app.exception_handler(Exception)
async def exception_handler(req: Request, exc: Exception) -> Response:
    return await on_exception_handler(req, exc)
