from typing import Any, Literal

from pydantic import BaseModel


class JsonResponseErrorModel[C = str, P = str, M = str](BaseModel):
    """
    JSON response error.
    """

    code: C
    """
    Code representing the error.
    """
    path: list[P] = []
    """
    Indicates where the error occurred.
    """
    message: M
    """
    Detail of the error.
    """


class JsonSuccessResponseModel[T = Any](BaseModel):
    """
    JSON success response.
    """

    success: Literal[True] = True
    """
    Indicates whether the response is successful or not.
    """
    data: T
    """
    Requested information for the response when `success` is `true`.
    """
    errors: list[None] = []
    """
    A list of errors for the response when `success` is `false`.
    """


class JsonFailureResponseModel[E = Any](BaseModel):
    """
    JSON failure response.
    """

    success: Literal[False] = False
    """
    Indicates whether the response is successful or not.
    """
    data: None = None
    """
    Requested information for the response when `success` is `true`.
    """
    errors: list[E] = []
    """
    A list of errors for the response when `success` is `false`.
    """
