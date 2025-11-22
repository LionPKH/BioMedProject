from app.schemas.task_schema import *
from app.models.tasks import Task
from app.models.user import User
from app.models.tasks_nodes import TaskNode
from typing import List

def map_to_model(schema: TaskCreate, user: User) -> Task:
    task = Task(**schema.model_dump(exclude_none=True))
    task.user = user
    return task

def map_to_dto(task: Task) -> TaskOut:
    return TaskOut.model_validate(task, from_attributes=True)

def map_task_list_to_dto_list(tasks: List[Task]) -> List[TaskOut]:
    result = []
    for task in tasks:
        result.append(TaskOut.model_validate(task, from_attributes=True))
    return result