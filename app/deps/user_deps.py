from fastapi import Depends
from app.repositories.user_repository import UserRepository
from app.services.user_service import UserService
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database  import get_session


def get_user_repository(
    session: AsyncSession = Depends(get_session)
) -> UserRepository:
    # print("repo session:", id(session))       # проверка корректного DI
    return UserRepository(session=session)


def get_user_service(
    user_repo: UserRepository = Depends(get_user_repository),
    session: AsyncSession = Depends(get_session)
) -> UserService:
    # print("service session:", id(session))      # проверка корректного DI
    return UserService(user_repository=user_repo, session=session)