from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, DateTime, Integer, ForeignKey
from app.core.database import Base
from datetime import datetime

class AdminDetails(Base):
    __tablename__ = "admin_details"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), unique=True)

    department: Mapped[str | None] = mapped_column(String(100))
    phone: Mapped[str | None] = mapped_column(String(20))
    permission_level: Mapped[int] = mapped_column(Integer, default=1)
    access_code: Mapped[str] = mapped_column(String(50))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())

    user: Mapped["User"] = relationship(back_populates="admin_details")
