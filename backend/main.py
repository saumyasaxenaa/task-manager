from fastapi import FastAPI, Depends, HTTPException, status, Response
from typing import List
import models
import schemas
from database import engine, get_db
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/tasks", response_model=List[schemas.TaskResponse])
def get_tasks(db: Session = Depends(get_db)):
    tasks = db.query(models.Task).all()
    return tasks


@app.post("/tasks", status_code=status.HTTP_201_CREATED, response_model=schemas.TaskResponse)
async def add_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    new_task = models.Task(**task.dict())
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


@app.delete("/tasks/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(id: int, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == id)
    if task.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"task with id: {id} does not exist")
    task.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/tasks/{id}", response_model=schemas.TaskResponse)
def update_task(id: int, updated_task: schemas.TaskCreate, db: Session = Depends(get_db)):
    task_query = db.query(models.Task).filter(models.Task.id == id)
    task = task_query.first()
    if task == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"task with id: {id} does not exist")
    task_query.update(updated_task.dict(), synchronize_session=False)
    db.commit()
    return task_query.first()
