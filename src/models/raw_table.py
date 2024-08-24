from pydantic import BaseModel, Field
from pathlib import Path
from typing import List


class RawEntry(BaseModel):
    number: int
    abi: str
    name: str
    entry_point: str | None = Field(default=None)
    compat_entry_point: str | None = Field(default=None)
    no_return: bool = Field(default=False)

class RawTable(BaseModel):
    file: Path
    entries: List[RawEntry]

    def create_name(self) -> str:
        extension = ""
        parts = self.file.name.replace(".tbl", "").split('_')
        if len(parts) >= 2:
            extension = "_" + parts[-1]

        return self.file.parents[-3].name + extension
