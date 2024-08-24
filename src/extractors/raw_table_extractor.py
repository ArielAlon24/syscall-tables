from pathlib import Path
from typing import List
from models.raw_table import RawTable, RawEntry


class RawTableExtractor:
    def __init__(self, directory: Path) -> None:
        self.directory = directory
        self.index = 1

    def run(self) -> List[RawTable]:
        tables = []

        for file in self.directory.glob("arch/**/syscall*.tbl"):
            table = self._parse_table_file(file)
            tables.append(table)
            print(
                f'- Extracted table {str(self.index).zfill(4)}: "{table.file}" with {len(table.entries)} entires'
            )
            self.index += 1

        return tables

    def _parse_table_file(self, file: Path) -> RawTable:
        entries = []
        with file.open() as stream:
            for line in stream:
                if not line.strip() or line.startswith("#"):
                    continue

                parts = line.split()

                entry_point = None
                if len(parts) > 3:
                    entry_point = parts[3]

                compat_entry_point = None
                if len(parts) > 4 and parts[4] != "-":
                    compat_entry_point = parts[4]

                no_return = False
                if len(parts) > 5:
                    no_return = True

                entry = RawEntry(
                    number=int(parts[0]),
                    abi=parts[1],
                    name=parts[2],
                    entry_point=entry_point,
                    compat_entry_point=compat_entry_point,
                    no_return=no_return,
                )

                entries.append(entry)

        return RawTable(file=file.relative_to(self.directory), entries=entries)
