from langchain_openrouter import ChatOpenRouter
from langchain_google_genai import ChatGoogleGenerativeAI

from app.core.config import settings
llm = ChatOpenRouter(
    model="cohere/north-mini-code:free",
    api_key=settings.OPENROUTER_API_KEY
)

llm2 = ChatGoogleGenerativeAI(
    model ="gemini-2.5-flash",
    api_key=settings.GEMINI_API_KEY
)