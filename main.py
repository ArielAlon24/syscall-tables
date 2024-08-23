#!./venv/bin/python

from pathlib import Path
from enum import Enum
from typing import Dict, Iterator, List
import json
from pydantic import BaseModel
from pydantic.json import pydantic_encoder
import argparse


class Definition(Enum):
    REGULAR_32 = "SYSCALL32_DEFINE"
    REGULAR = "SYSCALL_DEFINE"
    COMPAT = "COMPAT_SYSCALL_DEFINE"
    PPC_32 = "PPC32_SYSCALL_DEFINE"


class Syscall(BaseModel):
    definition: Definition
    n: int
    name: str
    parameters: Dict[str, str]
    file: Path
    line: int

    def __repr__(self) -> str:
        return f"Name: {self.name} ({self.definition.value.title()} definition) [{self.file}:{self.line}] \nParameters: {self.parameters}"


class SyscallExtractor:
    def __init__(self, directory: Path) -> None:
        self.directory = directory
        self.index = 1

    def run(self, json_file_path: Path) -> None:
        syscalls = []

        for file in self.directory.glob("**/*.[c]"):
            syscalls.extend(self._find_syscalls_in_file(file))

        with open(json_file_path, "w") as file:
            json.dump(syscalls, fp=file, default=pydantic_encoder, indent=4)

    def _find_syscalls_in_file(self, file: Path) -> List[Syscall]:
        syscalls = []

        with file.open() as stream:
            for index, line in enumerate(stream):
                for definition in Definition:
                    if not line.startswith(definition.value):
                        continue

                    syscalls.append(
                        self._extract_syscall_from_file(
                            file=file,
                            definition=definition,
                            line=line,
                            stream=stream,
                            start=index,
                        )
                    )

        return syscalls

    def _extract_syscall_from_file(
        self,
        file: Path,
        definition: Definition,
        line: str,
        stream: Iterator[str],
        start: int,
    ) -> Syscall:
        declaration = line.strip()
        if not declaration.endswith(")"):
            for index, line in enumerate(stream):
                declaration += line.strip()
                if line.endswith(")\n"):
                    break

        definition_length = len(definition.value)
        n = int(declaration[definition_length : definition_length + 1])

        closing_paren = declaration.find(")")
        arguments = declaration[definition_length + 2 : closing_paren].split(",")
        name = arguments.pop(0)

        parameters = {
            arguments[i + 1].strip(): arguments[i].strip()
            for i in range(0, len(arguments) - 1, 2)
        }

        syscall = Syscall(
            file=file.relative_to(self.directory),
            line=start,
            n=n,
            definition=definition,
            name=name,
            parameters=parameters,
        )

        print(f"({str(self.index).zfill(4)}) {name}")
        self.index += 1

        return syscall


def error(message: str) -> None:
    print(f"Error: {message}")
    exit(1)


if __name__ == "__main__":
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

    try:
        syscall_extractor = SyscallExtractor(linux_dir)
        syscall_extractor.run(output)
    except Exception as e:
        error(str(e))
