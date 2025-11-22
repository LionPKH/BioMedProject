from app.models.user import User
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete
import asyncio

class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session


    async def save(self, user: User):
        self.session.add(user)
        await self.session.flush()
        await self.session.refresh(user)

    
    async def find_by_id(self, id: int) -> User | None:
        return await self.session.get(User, id)
    
    
    async def find_by_username(self, username: str) -> User | None:
        result = await self.session.execute(
            select(User).where(User.username == username)
        )
        return result.scalar_one_or_none()
    
    
    async def delete_user(self, user: User) -> None:
        await self.session.delete(user)