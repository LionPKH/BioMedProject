from fastapi import UploadFile
from typing import List
from app.models.files import File
from app.models.tasks import Task
from app.core.settings import settings
import os, uuid

async def save_files(files: List[UploadFile], task: Task, tag: str):
    for file in files:
        # разделяем имя и расширение
        name, ext = os.path.splitext(file.filename)

        # создаём уникальное имя
        unique_name = f"{name}_{uuid.uuid4()}{ext}"

        storage_path = os.path.join(settings.STORAGE_DIR, unique_name)

        # читаем и сохраняем файл
        file_bytes = await file.read()
        with open(storage_path, "wb") as buffer:
            buffer.write(file_bytes)

        # сохраняем в базу
        task.files.append(File(
            filename=unique_name, 
            tag=tag,
            file_type=file.content_type,
            storage_path=storage_path,
            size_bytes=len(file_bytes),
        ))