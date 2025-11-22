from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from app.core.database import Base

class User(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key=True)

    username: Mapped[str] = mapped_column(String(255), unique=True)
    email: Mapped[str] = mapped_column(String(255))
    password: Mapped[str] = mapped_column(String(255))
    user_type: Mapped[str] = mapped_column(String(255), default="user")

    user_details: Mapped["UserDetails"] = relationship(
        back_populates="user", uselist=False, cascade="all, delete", lazy="selectin"
    )

    admin_details: Mapped["AdminDetails"] = relationship(
        back_populates="user", uselist=False, cascade="all, delete", lazy="selectin"
    )
    
    tasks: Mapped[list["Task"]] = relationship(
        back_populates="user", cascade="all, delete"
    )