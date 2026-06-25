from fastapi import FastAPI

from app.health.router import router as health_router

from app.task1.router import router as task1_router

app =FastAPI(
    title="LangChain Practice API",
    version="1.0.0"
)

app.include_router(
    health_router,
    tags=["Health"]
)

app.include_router(
    task1_router,
    tags=["task1"]
)

