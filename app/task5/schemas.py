from pydantic import BaseModel

class UserInfo(BaseModel):
    name: str
    age: int
    occupation : str

class SafeJsonRequest(BaseModel):
    text: str

class SafeJsonResponse(BaseModel):
    data: UserInfo        