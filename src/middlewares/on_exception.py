from fastapi.requests import Request
from fastapi.responses import JSONResponse
from jder_fastapi.responses.json import (
    CreateJsonFailureResponseOptions,
    JsonResponseError,
    createJsonResponse,
)

from src.classes.enums.error import (
    ResponseErrorCode,
    get_response_error_message,
)
from src.classes.exceptions.service import ServiceError
from src.configs.log import logger


async def on_exception_handler(_: Request, exc: Exception) -> JSONResponse:
    if isinstance(exc, ServiceError):
        return exc.to_json_response()

    code: ResponseErrorCode = ResponseErrorCode.SERVER

    return createJsonResponse(
        options=CreateJsonFailureResponseOptions(
            status=500,
            errors=[
                JsonResponseError(
                    code=code,
                    message=get_response_error_message(code),
                )
            ],
        )
    )
