from pydantic import BaseModel

class ContentRequest(BaseModel):
    topic: str

class ContentResponse(BaseModel):
    summary: str
    tweet: str
    linkedin_post: str 
