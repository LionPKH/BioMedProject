from fastapi import APIRouter, Depends, UploadFile, File
from fastapi.responses import FileResponse
from app.schemas.user_schema import *
from app.services.user_service import UserService
from app.deps.user_deps import *


router = APIRouter(prefix="/users", tags=["Users"])

# ==============
# GET
# ==============

@router.get("/auth/{username}", response_model=AuthRead)
async def get_auth_details(username: str, user_service: UserService = Depends(get_user_service)):
    return await user_service.find_user_by_username(username)

@router.get("/{user_id}", response_model=UserRead)
async def get_user_info(user_id: int, user_service: UserService = Depends(get_user_service)):
    return await user_service.find_user(user_id)

@router.get("/{user_id}/avatar", response_class=FileResponse)
async def get_avatar(user_id: int, user_service: UserService = Depends(get_user_service)):
    pass

# ==============
# POST
# ==============

@router.post("/", response_model=UserRead)
async def register_user(schema: UserCreate, user_service: UserService = Depends(get_user_service)):
    return await user_service.create_user(schema)

@router.post("/admin", response_model=UserRead)
async def register_admin(schema: AdminCreate, user_service: UserService = Depends(get_user_service)):
    return await user_service.create_admin(schema)

# ==============
# PUT
# ==============

@router.put("/{user_id}", response_model=UserRead)
async def update_user(user_id: int, schema: UserUpdate, user_service: UserService = Depends(get_user_service)):
    return await user_service.update_user(id=user_id, schema=schema)

@router.put("/{user_id}/avatar", response_class=FileResponse)
async def upload_avatar(user_id: int, file: UploadFile = File(...), user_service: UserService = Depends(get_user_service)):
    pass

# ==============
# DELETE
# ==============

@router.delete("/{user_id}")
async def delete_user(user_id: int, user_service: UserService = Depends(get_user_service)):
    await user_service.delete_user(user_id)

@router.delete("/{user_id}/avatar")
async def delete_avatar(user_id: int, user_service: UserService = Depends(get_user_service)):
    pass