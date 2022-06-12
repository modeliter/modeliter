from pydantic.dataclasses import dataclass
from sqlalchemy import Column, String, LargeBinary
from sqlalchemy.orm import relationship
from .base import Base


@dataclass
class TaskRequestModel(Base):
    __tablename__ = "t_taskrequest"

    id = Column(String, primary_key=True)
    f_name = Column(String)
    args_pickled = Column(LargeBinary)
    kwargs_pickled = Column(LargeBinary)
    status = Column(String, nullable=True)
    result_pickled = Column(LargeBinary, nullable=True)

    task_runs = relationship("TaskRunModel", back_populates="task_request")
