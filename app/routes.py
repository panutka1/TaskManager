from typing import List
from uuid import uuid4

from fastapi import APIRouter, HTTPException

from app.models import Task, TaskCreate

router = APIRouter()

# ===== BAZA =====

tasks: List[Task] = []


# ===== ENDPOINTY =====


@router.get("/health-check")
def health_check():
    return {"status": "ok"}


@router.get("/tasks", response_model=List[Task])
def get_tasks():
    return tasks


@router.post("/tasks", response_model=Task)
def create_task(task: TaskCreate):
    new_task = Task(
        id=str(uuid4()), title=task.title, description=task.description, completed=False
    )
    tasks.append(new_task)
    return new_task


@router.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: str):
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")


@router.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: str, updated_task: TaskCreate):
    for task in tasks:
        if task.id == task_id:
            task.title = updated_task.title
            task.description = updated_task.description
            return task
    raise HTTPException(status_code=404, detail="Task not found")


@router.delete("/tasks/{task_id}")
def delete_task(task_id: str):
    for task in tasks:
        if task.id == task_id:
            tasks.remove(task)
            return {"message": "Task deleted"}
    raise HTTPException(status_code=404, detail="Task not found")


@router.get("/")
def root():
    return {"message": "Task Manager API działa!"}
