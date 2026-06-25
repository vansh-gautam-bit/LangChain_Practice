from pydantic import BaseModel
from typing import Literal, Optional

class TransformRequest(BaseModel):
    action: Literal["summarize","translate","tone-shift"]
    language: Optional[str] =None
    text:str
    

class TransformResponse(BaseModel):
    result: str    

