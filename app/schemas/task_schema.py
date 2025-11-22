from pydantic import BaseModel, ConfigDict
from datetime import datetime

class TaskCreate(BaseModel):
    name: str
    description: str | None = None

class TaskOut(BaseModel):
    id: int
    name: str
    description: str | None = None
    status: str
    created_at: datetime
    started_at: datetime | None = None
    finished_at: datetime | None = None

class NodeIds(BaseModel):
    id: str
