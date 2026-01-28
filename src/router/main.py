from typing import Any

from fastapi import APIRouter
from fastapi.responses import Response
from jder_fastapi.responses.json import createJsonResponse

from src.classes.models.response import JsonSuccessResponseModel
from src.modules.info.routes import router as router_info

router: APIRouter = APIRouter()


@router.get(
    "/",
    operation_id="getIndex",
    responses={
        200: {
            "model": JsonSuccessResponseModel[Any],
        },
    },
)
async def route_index() -> Response:
    return createJsonResponse()


router.include_router(
    prefix="/info",
    router=router_info,
)
