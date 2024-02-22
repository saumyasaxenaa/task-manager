from sqlalchemy import Column, Integer, String, DateTime, Boolean
from datetime import datetime, timezone
from database import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    task = Column(String)
    created_at = Column(DateTime, default=datetime.now())
    low_priority = Column(Boolean)
    medium_priority = Column(Boolean)
    high_priority = Column(Boolean)
