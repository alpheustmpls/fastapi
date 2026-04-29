from src.configs.vars import get_version
from src.modules.info.models import Info


async def service_info() -> Info:
    return Info(
        # API version
        version=get_version(),
    )
