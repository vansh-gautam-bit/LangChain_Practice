from langchain_openrouter import ChatOpenRouter

from app.core.config import settings
llm = ChatOpenRouter(
    model="cohere/north-mini-code:free",
    api_key=settings.OPENROUTER_API_KEY
)