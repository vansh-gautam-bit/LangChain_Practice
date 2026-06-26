from pydantic import BaseModel
from typing import Literal

class AskRequest(BaseModel):
    question: str

class AskResponse(BaseModel):
    answer: str    

class Classification(BaseModel):
    category: Literal[
        "coding",
        "math",
        "general",
    ]    