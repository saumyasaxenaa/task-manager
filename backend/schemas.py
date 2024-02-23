from pydantic import BaseModel
from datetime import datetime


class Task(BaseModel):
    task: str
    low_priority: bool = False
    medium_priority: bool = False
    high_priority: bool = False


class TaskBase(BaseModel):
    task: str
    low_priority: bool = False
    medium_priority: bool = False
    high_priority: bool = False


class TaskCreate(TaskBase):
    pass


class TaskResponse(TaskBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
