from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title="Task Manager API",
    description="A simple REST API for managing tasks",
    version="1.0.0"
)

app.include_router(router, prefix="/api/v1", tags=["tasks"])