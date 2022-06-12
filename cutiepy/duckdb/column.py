from pydantic.dataclasses import dataclass

@dataclass
class DuckDBColumn:
    name: str
    type: str
    constraints: str

    def __str__(self):
        self.name
