from typing import Optional, Self

from fastapi.responses import JSONResponse
from jder_fastapi.responses.json import (
    CreateJsonFailureResponseOptions,
    JsonResponseError,
    createJsonResponse,
)


class ServiceError(Exception):
    """
    Custom error for service-layer failures.
    """

    def __init__(self, message: Optional[str] = None) -> None:
        super().__init__(message)

        self._status: int = 500
        self._code: str = "unknown"
        self._path: list[str] = []
        self._message: Optional[str] = message

    def set_status(self, status: int) -> Self:
        self._status = status
        return self

    def get_status(self) -> int:
        return self._status

    def set_code(self, code: str) -> Self:
        self._code = code
        return self

    def get_code(self) -> str:
        return self._code

    def set_path(self, path: list[str]) -> Self:
        self._path = path
        return self

    def get_path(self) -> list[str]:
        return self._path

    def set_message(self, message: str) -> Self:
        self._message = message
        return self

    def get_message(self) -> Optional[str]:
        return self._message

    def to_json_response_error(self) -> JsonResponseError:
        return JsonResponseError(
            code=self.get_code(),
            path=self.get_path(),
            message=self.get_message(),
        )

    def to_json_response(self) -> JSONResponse:
        return createJsonResponse(
            options=CreateJsonFailureResponseOptions(
                status=self.get_status(),
                errors=[self.to_json_response_error()],
            )
        )
