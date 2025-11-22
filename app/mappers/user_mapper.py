from app.models.user import User
from app.models.user_details import UserDetails
from app.models.admin_details import AdminDetails
from app.schemas.user_schema import (
    UserRead, AuthRead,
    UserCreate, AdminCreate, AdminDetailsBaseCreate, UserDetailsBaseCreate,
    UserUpdate
)

def map_user_create_to_user(schema: UserCreate) -> User:
    details_fields = UserDetailsBaseCreate.model_fields.keys()
    details = UserDetails(**schema.model_dump(include=details_fields))
    user = User(
        **schema.model_dump(exclude=details_fields, exclude_none=True), 
        user_details=details
    )
    return user

def map_admin_create_to_user(schema: AdminCreate) -> User:
    details_fiels = AdminDetailsBaseCreate.model_fields.keys()
    details = AdminDetails(**schema.model_dump(include=details_fiels, exclude_none=True))
    user = User(
        **schema.model_dump(exclude=details_fiels, exclude_none=True),
        admin_details=details
    )
    return user

def map_user_to_user_read(user: User) -> UserRead:
    return UserRead.model_validate(user, from_attributes=True)

def map_user_to_auth_read(user: User) -> UserRead:
    return AuthRead.model_validate(user, from_attributes=True)


def apply_user_update(model: User, schema: UserUpdate) -> User:
    # Обновляем базовые поля юзера
    base_data = schema.model_dump(
        exclude={"user_details", "admin_details"},
        exclude_unset=True,
        exclude_none=True
    )

    for field, value in base_data.items():
        setattr(model, field, value)

    # --- Обновляем детали ---

    # Администратор
    if model.user_type == "admin" and schema.admin_details:
        admin_details_data = schema.admin_details.model_dump(
            exclude_unset=True,
            exclude_none=True
        )
        for field, value in admin_details_data.items():
            setattr(model.admin_details, field, value)

    # Обычный пользователь
    elif model.user_type == "user" and schema.user_details:
        user_details_data = schema.user_details.model_dump(
            exclude_unset=True,
            exclude_none=True
        )
        for field, value in user_details_data.items():
            setattr(model.user_details, field, value)

    return model