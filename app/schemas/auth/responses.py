from pydantic import BaseModel


class AuthToken(BaseModel):
    iat: str
