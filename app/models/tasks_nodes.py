from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, DateTime, Boolean, Text, Date, ForeignKey
from datetime import date, datetime
from app.core.database import Base

class TaskNode(Base):
    __tablename__ = "tasks_nodes"

    id: Mapped[int] = mapped_column(primary_key=True)
    task_id: Mapped[int] = mapped_column(ForeignKey("tasks.id"))
    node_id: Mapped[int] = mapped_column(ForeignKey("nodes.id"))

    assigned_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    status: Mapped[str] = mapped_column(String, default="assigned")

    task: Mapped["Task"] = relationship(back_populates="nodes")
    node: Mapped["Node"] = relationship(back_populates="tasks")