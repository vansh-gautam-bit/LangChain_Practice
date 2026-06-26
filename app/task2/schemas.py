from pydantic import BaseModel

class Resume(BaseModel):
    name:str
    skills: list[str]
    years_of_experience: int
    last_role: str

class ResumeRequest(BaseModel):
    resume_text: str    