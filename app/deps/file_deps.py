from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_session
from app.repositories.task_repository import TaskRepository
from app.repositories.file_repository import FileRepository
from app.services.file_service import FileService
from app.deps.task_deps import get_task_repo


def get_file_repo(session: AsyncSession = Depends(get_session)):
    return FileRepository(session=session)


def get_file_service(
    session: AsyncSession = Depends(get_session), 
    task_repo: TaskRepository = Depends(get_task_repo),
    file_repo: FileRepository = Depends(get_file_repo)
):
    return FileService(session=session, task_repo=task_repo, file_repo=file_repo)