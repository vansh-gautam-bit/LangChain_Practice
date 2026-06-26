from fastapi import APIRouter

from app.task4.chain import content_chain
from app.task4.schemas import ContentRequest, ContentResponse

router = APIRouter()

@router.post(
    "/generate-content",
    response_model=ContentResponse,
)
def generate_content(request: ContentRequest):
    result = content_chain.invoke(
        {
            "topic": request.topic
        }
    )
    return ContentResponse(**result)