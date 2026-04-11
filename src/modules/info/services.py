from src.configs.vars import get_version
from src.modules.info.models import Info, InfoAPI


async def service_info() -> Info:
    return Info(
        api=InfoAPI(
            # API version
            version=get_version(),
        )
    )
