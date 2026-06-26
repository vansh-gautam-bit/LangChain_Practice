from fastapi import FastAPI

from app.health.router import router as health_router

from app.task1.router import router as task1_router

from app.task2.router import router as task2_router

from app.task3.router import router as task3_router

from app.task4.router import router as task4_router

from app.task5.router import router as task5_router

app =FastAPI(
    title="LangChain Practice API",
    version="1.0.0"
)

app.include_router(
    health_router,
    tags=["Health"],
)

app.include_router(
    task1_router,
    tags=["task1"],
)

app.include_router(
    task2_router,
    tags=["Task 2"],
)

app.include_router(
    task3_router,
    tags=["Task 3"],
)

app.include_router(
    task4_router,
    tags=["Task4"],
)

app.include_router(
    task5_router,
    tags=["task5"],
)