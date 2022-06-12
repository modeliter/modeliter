from pydantic.dataclasses import dataclass
from sqlalchemy import Column, LargeBinary, String, DateTime
from sqlalchemy.orm import relationship
from .base import Base


@dataclass
class TaskRunModel(Base):
    __tablename__ = "t_taskrun"

    id = Column(String, primary_key=True)
    task_request = relationship("TaskRequestModel", back_populates="task_runs")
    worker_ref = Column(String)
    broker_created_at = Column(DateTime)
    worker_received_at = Column(DateTime, nullable=True)
    worker_returned_at = Column(DateTime, nullable=True)
    broker_received_at = Column(DateTime, nullable=True)
    result_pickled = Column(LargeBinary, nullable=True)
