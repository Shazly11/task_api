from fastapi import APIRouter, Depends
from sqlmodel import Session
from model import Task
from database import get_session
from schemas import TaskCreate, TaskResponse
from datetime import datetime

router = APIRouter()

@router.post("/tasks", response_model=TaskResponse, status_code=201)
def create_task(task: TaskCreate, session: Session = Depends(get_session)):
    new_task = Task.model_validate(task)
    new_task.created_at = datetime.utcnow()
    session.add(new_task)
    session.commit()
    session.refresh(new_task)
    return new_task

from typing import List
from sqlmodel import select

@router.get("/tasks", response_model=List[TaskResponse])
def get_tasks(session: Session = Depends(get_session)):
    tasks = session.exec(select(Task)).all()
    return tasks
from fastapi import HTTPException

@router.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, session: Session = Depends(get_session)):
    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

from schemas import TaskUpdate

@router.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task_data: TaskUpdate, session: Session = Depends(get_session)):
    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    task_data_dict = task_data.dict(exclude_unset=True)
    for key, value in task_data_dict.items():
        setattr(task, key, value)
    
    session.add(task)
    session.commit()
    session.refresh(task)
    return task

@router.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int, session: Session = Depends(get_session)):
    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    session.delete(task)
    session.commit()

from model import Task, TaskStatus, TaskPriority

@router.get("/tasks/status/{status}", response_model=List[TaskResponse])
def get_tasks_by_status(status: TaskStatus, session: Session = Depends(get_session)):
    tasks = session.exec(select(Task).where(Task.status == status)).all()
    return tasks

@router.get("/tasks/priority/{priority}", response_model=List[TaskResponse])
def get_tasks_by_priority(priority: TaskPriority, session: Session = Depends(get_session)):
    tasks = session.exec(select(Task).where(Task.priority == priority)).all()
    return tasks

@router.get("/tasks", response_model=List[TaskResponse])
def get_tasks(skip: int = 0, limit: int = 10, session: Session = Depends(get_session)):
    tasks = session.exec(select(Task).offset(skip).limit(limit)).all()
    return tasks
