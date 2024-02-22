from pydantic import BaseModel
from datetime import datetime


class Task(BaseModel):
    id: int
    task: str
    low_priority: bool = False
    medium_priority: bool = False
    high_priority: bool = False

    class Config:
        orm_mode = True


# class TaskCreate(Task):
#     pass


class TaskResponse(Task):
    created_at: datetime

    class Config:
        orm_mode = True
