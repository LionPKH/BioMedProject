from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.file_repository import FileRepository
from app.repositories.task_repository import TaskRepository
import app.utils.zipper as zipper

class FileService:
    def __init__(self, session: AsyncSession, file_repo: FileRepository, task_repo: TaskRepository):
        self.session = session
        self.file_repo = file_repo
        self.task_repo = task_repo

    
    async def get_task_files(self, task_id: int, file_tag: str):
        async with self.session.begin():
            task = self.task_repo.find_by_id(task_id)
            if not task:
                raise ValueError("Task not found")
            filenames = await self.file_repo.get_filenames_by_task_and_role(task_id=task_id, tag=file_tag)
        return await zipper.generate_zip_response(filenames=filenames)
    