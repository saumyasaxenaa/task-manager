from fastapi import FastAPI, Depends, HTTPException, status, Response
from typing import List
import models
import schemas
from database import engine, SessionLocal, get_db
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/tasks", response_model=List[schemas.Task])
def get_tasks(db: Session = Depends(get_db)):
    tasks = db.query(models.Task).all()
    return tasks


@app.post("/task", status_code=status.HTTP_201_CREATED, response_model=schemas.TaskResponse)
async def add_task(task: schemas.Task, db: Session = Depends(get_db)):
    new_task = models.Task(**task.dict())
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task
