from sqlalchemy.ext.asyncio import AsyncSession
import app.mappers.user_mapper as mapper
from app.repositories.user_repository import UserRepository
from app.schemas.user_schema import *

class UserService:
    def __init__(self, user_repository: UserRepository, session: AsyncSession):
        self.user_repository = user_repository
        self.session = session


    async def create_user(self, schema: UserCreate) -> UserRead:
        async with self.session.begin():
            existed = await self.user_repository.find_by_username(schema.username)
            if existed:
                raise ValueError("User with current username already exists")
            user = mapper.map_user_create_to_user(schema)
            await self.user_repository.save(user)
        return mapper.map_user_to_user_read(user)
    

    async def create_admin(self, schema: AdminCreate) -> UserRead:
        async with self.session.begin():
            existed = await self.user_repository.find_by_username(schema.username)
            if existed:
                raise ValueError("User with current username already exists")
            user = mapper.map_user_create_to_user(schema)
            await self.user_repository.save(user)
        return mapper.map_user_to_user_read(user)


    async def find_user(self, id: int) -> UserRead:
        async with self.session.begin():
            user = await self.user_repository.find_by_id(id)
            if not user:
                raise ValueError("User not found")
        return mapper.map_user_to_user_read(user)
    

    async def find_user_by_username(self, username: str) -> AuthRead:
        async with self.session.begin():
            user = await self.user_repository.find_by_username(username)
            if not user:
                raise ValueError("User not found")
        return mapper.map_user_to_auth_read(user)
    

    async def update_user(self, id: int, schema: UserUpdate) -> UserRead:
        async with self.session.begin():
            user = await self.user_repository.find_by_id(id)
            if not user:
                raise ValueError("User not found")
            mapper.apply_user_update(user, schema)
        return mapper.map_user_to_user_read(user)
    

    async def delete_user(self, id: int) -> None:
        async with self.session.begin():
            user = await self.user_repository.find_by_id(id)
            if not user:
                raise ValueError("User not found")
            await self.user_repository.delete_user(user)

                
