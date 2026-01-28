from logging import DEBUG, Logger, getLogger

logger: Logger = getLogger("uvicorn.error")
logger.setLevel(DEBUG)
