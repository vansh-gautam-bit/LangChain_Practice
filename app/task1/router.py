from fastapi import APIRouter

from app.task1.schemas import TransformRequest, TransformResponse
from app.task1.chain import transform_chain

router =APIRouter()

@router.post(
    "/transform",
    response_model=TransformResponse
)
def transform(request: TransformRequest):

    result = transform_chain.invoke(
        {
            "action": request.action,
            "text" : request.text,
            "language": request.language,
        }
    )

    return TransformResponse(result=result)