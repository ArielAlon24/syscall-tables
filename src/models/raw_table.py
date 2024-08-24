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

    @property
    def architecture(self) -> str:
        for part in self.file.parts:
            if part == "arch":
                index = self.file.parts.index(part)
                if index + 1 < len(self.file.parts):
                    return self.file.parts[index + 1]

        return "Unknown"  # unreachable

    @property
    def extension(self) -> str:
        print(self.file.name)
        basename = self.file.name
        basename = basename.removesuffix(".tbl")
        parts = basename.split("_")

        print(parts)
        if len(parts) == 1:
            return ""

        return "_" + parts[-1]
