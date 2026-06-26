from fastapi import APIRouter

from app.task2.chain import resume_chain
from app.task2.schemas import Resume, ResumeRequest

router = APIRouter()

@router.post(
    "/parse-resume",
    response_model=Resume,
)
def parse_resume(request: ResumeRequest):
    result =resume_chain.invoke(
        {
            "resume_text": request.resume_text
        }
    )
    return result    
    