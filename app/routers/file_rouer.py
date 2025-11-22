from fastapi import APIRouter, Depends, UploadFile
from fastapi.responses import FileResponse, StreamingResponse
from typing import List
from app.schemas.file_schema import FileOut
from app.services.file_service import FileService
from app.deps.file_deps import get_file_service

router = APIRouter(prefix="/files", tags=["Files"])


# download

@router.get("/download/{file_id}", response_class=FileResponse)
async def download_file(file_id: int):
    pass

@router.get("/download/input-files/{task_id}", response_class=StreamingResponse)
async def download_input_files_zip(task_id: int, file_service: FileService = Depends(get_file_service)):
    return await file_service.get_task_files(task_id=task_id, file_tag="input")

@router.get("/download/result-files/{task_id}", response_class=StreamingResponse)
async def download_result_files_zip(task_id: int, file_service: FileService = Depends(get_file_service)):
    return await file_service.get_task_files(task_id=task_id, file_tag="result")


#info

@router.get("/info/{file_id}", response_model=FileOut)
async def get_file_info(file_id: int):
    pass

@router.get("/info/input-files/{task_id}", response_model=List[FileOut])
async def list_input_files(task_id: int):
    pass

@router.get("/info/result-files/{task_id}", response_model=List[FileOut])
async def list_result_files(task_id: int):
    pass