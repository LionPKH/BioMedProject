from fastapi import APIRouter, Depends, UploadFile, File
from typing import List
from app.schemas.task_schema import *
from app.services.task_service import TaskService
from app.deps.task_deps import *


router = APIRouter(prefix="/tasks", tags=["Tasks"])


# ===========
# GET
# ===========

@router.get("/all/{user_id}", response_model=List[TaskOut])
async def list_user_tasks(user_id: int, service: TaskService = Depends(get_task_service)):
    return await service.get_all_tasks(user_id=user_id)


# ===========
# POST
# ===========

# превод статуса в таблице task в pending
@router.post("/{user_id}", response_model=TaskOut)
async def create_task(
    user_id: int, 
    schema: TaskCreate,
    task_service: TaskService = Depends(get_task_service)
):
    return await task_service.create_task(user_id=user_id, schema=schema)


# ===========
# PUT
# ===========

@router.put("/{task_id}/add-files")
async def add_files_into_task(task_id: int, files: List[UploadFile] = File(...), task_service: TaskService = Depends(get_task_service)):
    await task_service.upload_input_files(task_id=task_id, files=files)

# перевод таска в working
@router.put("/{task_id}/start", response_model=TaskOut, 
    description="Мастер нода инициирует старт задачи на указанных нодах"
)
async def start_task(task_id: int, node_ids: List[NodeIds] | None = None):
    pass

# изменить статус результата на completed
@router.put("/{task_id}/complete")
async def complete_task(task_id: int, result_files: List[UploadFile] | None = None, task_service: TaskService = Depends(get_task_service)):
    await task_service.complete(task_id=task_id, files=result_files)


# изменить статус задачи на failed
@router.put("/{task_id}/fail", response_model=TaskOut)
async def fail_task(task_id: int):
    pass


# ===========
# DELETE
# ===========

@router.delete("/{task_id}", status_code=204)
async def delete_task(task_id: int):
    pass
