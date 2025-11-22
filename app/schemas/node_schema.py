from pydantic import BaseModel
from datetime import datetime

class TaskNode(BaseModel):
    task_id: int
    assigned_at: datetime
    status: str

class Node(BaseModel):
    node_id: str
    device_type: str
    status: str

class TaskNodeOut(Node):
    curren_task: TaskNode

class AddNode(BaseModel):
    node_id: str