from pydantic import BaseModel


class Object(BaseModel):
    args: dict
    data: str
    files: dict
    form: dict
    headers: dict
    method: str
    origin: str
    url: str
