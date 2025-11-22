from pydantic import BaseModel, ConfigDict
from datetime import datetime
from app.schemas.user_schema import UserBaseRead
from app.schemas.task_schema import TaskOut

class FileOut(BaseModel):
    id: int
    task_id: int
    filename: str
    file_type: str
    storage_path: str
    uploaded_at: datetime
    size_bytes: int
