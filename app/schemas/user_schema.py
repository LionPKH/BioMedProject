from pydantic import BaseModel, ConfigDict
from datetime import date, datetime
from typing import Dict, Any

# ====================
# CREATE
# ====================

class UserBaseCreate(BaseModel):
    username: str
    email: str
    password: str

class UserDetailsBaseCreate(BaseModel):
    bio: str | None = None
    birth_date: date | None = None
    phone: str | None = None
    city: str | None = None

class AdminDetailsBaseCreate(BaseModel):
    department: str | None = None
    phone: str | None = None
    permission_level: int
    access_code: str

class UserCreate(UserDetailsBaseCreate, UserBaseCreate):
    pass

class AdminCreate(AdminDetailsBaseCreate, UserBaseCreate):
    pass

# ====================
# READ
# ====================


class UserBaseRead(BaseModel):
    id: int
    username: str
    email: str
    user_type: str


class UserDetailsRead(BaseModel):
    bio: str | None = None
    birth_date: date | None = None
    phone: str | None = None
    city: str | None = None
    subscription_active: bool
    created_at: datetime


class AdminDetailsRead(BaseModel):
    department: str | None = None
    phone: str | None = None
    permission_level: int
    access_code: str
    created_at: datetime


class UserRead(UserBaseRead):
    user_details: UserDetailsRead | None = None
    admin_details: AdminDetailsRead | None = None

class AuthRead(UserBaseRead):
    password: str
    


# ====================
# UPDATE
# ====================


class UserBaseUpdate(BaseModel):
    username: str | None = None
    email: str | None = None
    password: str | None = None


class UserDetailsUpdate(BaseModel):
    bio: str | None = None
    birth_date: date | None = None
    phone: str | None = None
    city: str | None = None
    subscription_active: bool | None = None


class AdminDetailsUpdate(BaseModel):
    department: str | None = None
    phone: str | None = None
    permission_level: int | None = None
    access_code: str | None = None
    
    
class UserUpdate(UserBaseUpdate):
    user_details: UserDetailsUpdate | None = None
    admin_details: AdminDetailsUpdate | None = None