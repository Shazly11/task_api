from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from model import TaskStatus, TaskPriority
from pydantic import  field_validator


class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    status: Optional[TaskStatus] = TaskStatus.pending
    priority: Optional[TaskPriority] = TaskPriority.medium
    due_date: Optional[datetime] = None
    assigned_to: Optional[str] = None

    @field_validator("title")
    def title_must_not_be_blank(cls, v):
        if not v.strip():
            raise ValueError("Title cannot be empty or whitespace only")
        return v.strip()

    @field_validator("due_date")
    def due_date_must_be_future(cls, v):
        if v and v <= datetime.utcnow():
            raise ValueError("Due date must be in the future")
        return v

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[TaskStatus] = None
    priority: Optional[TaskPriority] = None
    due_date: Optional[datetime] = None
    assigned_to: Optional[str] = None
class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    status: TaskStatus
    priority: TaskPriority
    created_at: datetime
    updated_at: Optional[datetime] = None
    due_date: Optional[datetime] = None
    assigned_to: Optional[str] = None

    class Config:
        orm_mode = True