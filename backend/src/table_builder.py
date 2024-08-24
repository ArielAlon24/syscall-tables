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
            architecture = raw_table.architecture
            extension = raw_table.extension

            for raw_entry in raw_table.entries:

                syscalls = self.syscall_mapping.get(raw_entry.name, None)
                syscalls = syscalls if syscalls else list()
                actual = []

                for syscall in syscalls:
                    if syscall.file.match("arch") and not raw_table.file.match(
                        architecture
                    ):
                        continue

                    actual.append(syscall)

                entries.append(
                    Entry(
                        number=raw_entry.number,
                        syscalls=actual,
                    )
                )

            tables.append(
                Table(
                    architecture=architecture + extension,
                    entries=sorted(entries, key=lambda e: e.number),
                )
            )

            print(f"- Built table entry for {tables[-1].architecture}")

        return tables
