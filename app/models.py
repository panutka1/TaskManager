from pydantic import BaseModel, ConfigDict
from sqlalchemy import Boolean, Column, String

from app.database import Base


class TaskCreate(BaseModel):
    title: str
    description: str | None = None


class Task(TaskCreate):
    id: str
    completed: bool = False

    model_config = ConfigDict(from_attributes=True)


class TaskModel(Base):
    __tablename__ = "tasks"
    id = Column(String, primary_key=True)
    title = Column(String)
    description = Column(String, nullable=True)
    completed = Column(Boolean, default=False)


class TaskUpdate(BaseModel):
    title: str
    description: str | None = None
    completed: bool = False
