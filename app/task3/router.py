from fastapi import APIRouter

from app.task3.chain import ask_chain
from app.task3.schemas import AskRequest, AskResponse

router = APIRouter()


@router.post("/ask", response_model=AskResponse)
def ask(request: AskRequest):
    result = ask_chain.invoke(
        {
        "question": request.question
        }
    )

    return AskResponse(
        answer = result
    )