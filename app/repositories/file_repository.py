from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.files import File
from typing import List

class FileRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    
    async def get_filenames_by_task_and_role(self, task_id: int, tag: str) -> List[str]:
        stmt = (
            select(File.filename)
            .where(File.task_id == task_id)
            .where(File.tag == tag)
        )
        result = await self.session.execute(stmt)
        return result.scalars().all()