#!./venv/bin/python

from pathlib import Path
import sys
from typing import Dict, List
import json
from pydantic.json import pydantic_encoder
import argparse

from models.syscall import Syscall
from extractors.syscall_extractor import SyscallExtractor
from extractors.raw_table_extractor import RawTableExtractor
from models.raw_table import RawTable
from models.table import Table
from table_builder import TableBuilder


def extract_syscalls(linux_dir: Path) -> Dict[str, List[Syscall]]:
    syscall_extractor = SyscallExtractor(linux_dir)
    syscalls = syscall_extractor.run()
    return create_syscall_name_mapping(syscalls)


def extract_raw_tables(linux_dir: Path) -> List[RawTable]:
    table_extractor = RawTableExtractor(linux_dir)
    tables = table_extractor.run()
    return tables


def create_syscall_name_mapping(syscalls: List[Syscall]) -> Dict[str, List[Syscall]]:
    mapping = {}

    for syscall in syscalls:
        if syscall.name in mapping:
            mapping[syscall.name].append(syscall)
        else:
            mapping[syscall.name] = [syscall]

    return mapping


def build_tables(
    raw_tables: List[RawTable], syscall_mapping: Dict[str, List[Syscall]]
) -> List[Table]:
    table_builder = TableBuilder(raw_tables=raw_tables, syscall_mapping=syscall_mapping)
    return table_builder.build()


def error(message: str) -> None:
    print(f"Error: {message}")
    sys.exit(1)


def run(linux_dir: Path, output: Path) -> None:
    syscall_mapping = extract_syscalls(linux_dir)
    raw_tables = extract_raw_tables(linux_dir)
    tables = build_tables(raw_tables, syscall_mapping)

    with open(output, "w") as file:
        json.dump(tables, fp=file, default=pydantic_encoder, indent=4)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Extract syscalls from C files in a Linux directory."
    )
    parser.add_argument(
        "linux_dir", type=str, help="The directory containing Linux source files."
    )
    parser.add_argument(
        "output",
        type=str,
        help="The path to save the extracted syscalls in JSON format.",
    )

    args = parser.parse_args()

    linux_dir = Path(args.linux_dir)
    if not linux_dir.exists():
        error("linux_dir directory does not exist.")

    if not linux_dir.is_dir():
        error("linux_dir isn't a directory.")

    output = Path(args.output)
    if not output.exists():
        output.parent.mkdir(parents=True, exist_ok=True)

    run(linux_dir=linux_dir, output=output)


if __name__ == "__main__":
    main()
