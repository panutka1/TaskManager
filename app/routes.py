from typing import List
from uuid import uuid4

from fastapi import APIRouter, HTTPException, Depends

from app.models import Task, TaskCreate, TaskModel, TaskUpdate
from app.database import get_db
from sqlalchemy.orm import Session
from fastapi import Response, status

router = APIRouter()

# ===== ENDPOINTS =====


@router.get("/health-check")
def health_check():
    return {"status": "ok"}

@router.get("/tasks")
def get_tasks(db: Session = Depends(get_db)):
    return db.query(TaskModel).all()

@router.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    new_task = TaskModel(id=str(uuid4()), title=task.title, description=task.description)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


@router.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: str, db: Session = Depends(get_db)):
    task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    else:
        return task

@router.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: str, updated_task: TaskUpdate, db: Session = Depends(get_db)):
    task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    else:
        task.title = updated_task.title
        task.description = updated_task.description
        task.completed = updated_task.completed
        db.commit()
        db.refresh(task)
        return task

@router.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: str, db: Session = Depends(get_db)):
    task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    else:
            db.delete(task)
            db.commit()
            return

@router.get("/")
def root():
    return {"message": "Task Manager API works!"}
