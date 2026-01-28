from enum import Enum


class ResponseErrorCode(str, Enum):
    """
    Response error code.
    """

    # request
    NOT_FOUND = "not_found"
    PARSE = "parse"
    # server
    SERVER = "server"


class ResponseErrorMessage(str, Enum):
    """
    Response error message.
    """

    # request
    NOT_FOUND = "Content not found"
    PARSE = "Failed to parse the request"
    # server
    SERVER = "Internal server error"


def get_response_error_message(code: ResponseErrorCode) -> ResponseErrorMessage:
    return ResponseErrorMessage[code.name]
