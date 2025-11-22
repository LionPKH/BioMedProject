import os
import zipfile
from typing import List
from io import BytesIO
from fastapi.responses import StreamingResponse
from app.core.settings import settings
import asyncio


def _create_zip_bytes(filenames: List[str]) -> BytesIO:
    """
    Синхронная функция, которая реально создаёт ZIP в памяти.
    Вызывается в отдельном потоке.
    """
    zip_buffer = BytesIO()

    with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zip_file:
        for filename in filenames:
            file_path = os.path.join(settings.STORAGE_DIR, filename)

            if not os.path.exists(file_path):
                raise FileNotFoundError(f"Файл не найден: {filename}")

            zip_file.write(file_path, arcname=filename)

    zip_buffer.seek(0)
    return zip_buffer


async def generate_zip_response(filenames: List[str]) -> StreamingResponse:
    """
    Асинхронный интерфейс, который запускает создание ZIP в thread pool,
    не блокируя event loop.
    """

    loop = asyncio.get_event_loop()
    zip_buffer = await loop.run_in_executor(None, _create_zip_bytes, filenames)

    return StreamingResponse(
        zip_buffer,
        media_type="application/zip",
        headers={
            "Content-Disposition": "attachment; filename=files.zip"
        }
    )
