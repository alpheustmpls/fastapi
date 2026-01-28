from pydantic import BaseModel


class InfoAPI(BaseModel):
    version: str


class Info(BaseModel):
    api: InfoAPI
