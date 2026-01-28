from fastapi import APIRouter
from fastapi.responses import Response
from jder_fastapi.responses.json import (
    CreateJsonSuccessResponseOptions,
    createJsonResponse,
)

from src.classes.models.response import JsonSuccessResponseModel
from src.modules.info.services import Info, service_info

router: APIRouter = APIRouter()


@router.get(
    "/",
    operation_id="getInfo",
    responses={
        200: {
            "model": JsonSuccessResponseModel[Info],
        },
    },
)
async def route_info() -> Response:
    return createJsonResponse(
        options=CreateJsonSuccessResponseOptions(
            data=await service_info(),
        )
    )
