from pydantic import BaseModel
from typing import List, Any
from .syscall import Syscall


class Entry(BaseModel):
    number: int
    syscalls: List[Syscall] | None

    def model_post_init(self, __context: Any) -> None:
        self.syscalls = self.syscalls or list()


class Table(BaseModel):
    architecture: str
    entries: List[Entry]
