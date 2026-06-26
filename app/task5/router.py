from fastapi import APIRouter, HTTPException

from app.task5.chain import safe_json_chain
from app.task5.schemas import SafeJsonRequest, SafeJsonResponse

router = APIRouter()

@router.post(
    "/safe-json",
    response_model=SafeJsonResponse,
)
def safe_json(request: SafeJsonRequest):
    
    try:
        result = safe_json_chain.invoke(
            {
                "text": request.text
            }
        )

        return SafeJsonResponse(
            data=result
        )
    
    except Exception as e:
        raise HTTPException(
            status_code=422,
            detail=str(e),
        )