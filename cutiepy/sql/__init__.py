from pathlib import Path
from sqlalchemy import create_engine
from .models import Base


def build_engine(*, path: Path):
    print(path)
    engine = create_engine(
        url=f"sqlite:///{path.resolve()}",
        echo=True,
        future=True,
    )
    Base.metadata.create_all(engine)
    return engine
