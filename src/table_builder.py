from pathlib import Path
from typing import Dict, List

from models.raw_table import RawTable
from models.syscall import Syscall
from models.table import Entry, Table


class TableBuilder:

    def __init__(
        self, raw_tables: List[RawTable], syscall_mapping: Dict[str, List[Syscall]]
    ) -> None:
        self.raw_tables = raw_tables
        self.syscall_mapping = syscall_mapping

    def build(self) -> List[Table]:
        tables = []

        for raw_table in self.raw_tables:
            entries = []
            name = raw_table.create_name()

            for raw_entry in raw_table.entries:

                syscalls = self.syscall_mapping.get(raw_entry.name, None)

                entries.append(
                    Entry(
                        number=raw_entry.number,
                        syscalls=syscalls,
                    )
                )

            tables.append(Table(architecture=name, entries=entries))

        return tables
