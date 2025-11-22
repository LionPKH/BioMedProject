from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, DateTime, Boolean, Text, Date, ForeignKey, BigInteger
from datetime import date, datetime
from app.core.database import Base

class File(Base):
    __tablename__ = "files"

    id: Mapped[int] = mapped_column(primary_key=True)
    task_id: Mapped[int] = mapped_column(ForeignKey("tasks.id"))

    filename: Mapped[str] = mapped_column(String(255))
    tag: Mapped[str] = mapped_column(String(50))
    file_type: Mapped[str] = mapped_column(String(255))
    storage_path: Mapped[str] = mapped_column(Text)
    uploaded_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.now())
    size_bytes: Mapped[int] = mapped_column(BigInteger)

    task: Mapped["Task"] = relationship(back_populates="files")