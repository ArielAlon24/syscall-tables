from pydantic import BaseModel
from .definition import Definition
from typing import Dict
from pathlib import Path

class Syscall(BaseModel):
    definition: Definition
    n: int
    name: str
    parameters: Dict[str, str]
    file: Path
    line: int

    def __repr__(self) -> str:
        return f"Name: {self.name} ({self.definition.value.title()} definition) [{self.file}:{self.line}] \nParameters: {self.parameters}"
