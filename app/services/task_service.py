from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.user_repository import UserRepository
from app.repositories.task_repository import TaskRepository
from app.schemas.task_schema import *
import app.mappers.task_mapper as mapper
import app.utils.file_utils as utils
from fastapi import UploadFile
from typing import List

class TaskService:
    def __init__(self, session: AsyncSession, task_repo: TaskRepository, user_repo: UserRepository):
        self.session = session
        self.task_repo = task_repo
        self.user_repo = user_repo

    
    async def create_task(self, user_id: int, schema: TaskCreate) -> TaskOut:
        async with self.session.begin():
            user = await self.user_repo.find_by_id(user_id)
            if not user:
                raise ValueError("User not found")
            task = mapper.map_to_model(schema, user)
            await self.task_repo.save(task)
        return mapper.map_to_dto(task)
    

    async def get_all_tasks(self, user_id: id) -> List[TaskOut]:
        async with self.session.begin():
            user = await self.user_repo.find_by_id(user_id)
            if not user:
                raise ValueError("User not found")
            tasks = await self.task_repo.find_task_by_user_id(user_id)
        return mapper.map_task_list_to_dto_list(tasks)
    

    async def upload_input_files(self, task_id: int, files: list[UploadFile]):
        async with self.session.begin():
            task = await self.task_repo.find_by_id(task_id)
            if not task:
                raise ValueError("Task not found")
            await utils.save_files(files=files, task=task, tag="input")


    async def complete(self, task_id: int, files: List[UploadFile]):
        async with self.session.begin():
            task = await self.task_repo.find_by_id(task_id)
            if not task:
                raise ValueError("Task not found")
            if files:
                await utils.save_files(files=files, task=task, tag="result")
            task.status = "completed"