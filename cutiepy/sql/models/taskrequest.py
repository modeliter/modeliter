from dataclasses import dataclass
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String


Base = declarative_base()

@dataclass
class TaskRequest(Base):
    __tablename__ = "t_taskrequest"

    id = Column(String, primary_key=True)
    f_name = Column(String)
