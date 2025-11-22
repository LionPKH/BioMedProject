from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.core.database import init_db
from app.routers import (
    user_router,
    task_router,
    file_rouer,
    node_router,
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

app = FastAPI(title="FastAPI App", lifespan=lifespan)

app.include_router(user_router.router)
app.include_router(task_router.router)
app.include_router(file_rouer.router)
app.include_router(node_router.router)