from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.tasks import Task
from typing import List

class TaskRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    
    async def save(self, task: Task):
        self.session.add(task)
        await self.session.flush()
        await self.session.refresh(task)


    async def find_by_id(self, id: int) -> Task | None:
        return await self.session.get(Task, id)
    

    async def find_task_by_user_id(self, user_id: int) -> List[Task]:
        stmt = select(Task).where(Task.user_id == user_id)
        result = await self.session.execute(stmt)
        return result.scalars().all()