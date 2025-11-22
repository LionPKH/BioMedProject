from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, DateTime, Boolean, Text, Date, ForeignKey
from datetime import date, datetime
from app.core.database import Base

class Node(Base):
    __tablename__ = "nodes"

    id: Mapped[int] = mapped_column(primary_key=True)
    node_id: Mapped[str] = mapped_column(String(30), unique=True)
    device_type: Mapped[str] = mapped_column(String)
    status: Mapped[str] = mapped_column(String)

    tasks: Mapped[list["TaskNode"]] = relationship(back_populates="node")