from pydantic import BaseModel
from datetime import datetime


# class Task(BaseModel):
#     task: str
#     priority: bool = False


class TaskBase(BaseModel):
    task: str
    priority: bool = False


class TaskCreate(TaskBase):
    pass


class TaskResponse(TaskBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
