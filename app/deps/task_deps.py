from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_session
from app.repositories.task_repository import TaskRepository
from app.repositories.user_repository import UserRepository
from app.services.task_service import TaskService
from app.deps.user_deps import get_user_repository


def get_task_repo(session: AsyncSession = Depends(get_session)):
    return TaskRepository(session=session)


def get_task_service(
    session: AsyncSession = Depends(get_session), 
    task_repo: TaskRepository = Depends(get_task_repo),
    user_repo: UserRepository = Depends(get_user_repository)
):
    return TaskService(session=session, task_repo=task_repo, user_repo=user_repo)