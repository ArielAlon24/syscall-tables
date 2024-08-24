from pathlib import Path
from typing import List, Iterator
from models.syscall import Syscall
from models.definition import Definition


class SyscallExtractor:
    def __init__(self, directory: Path) -> None:
        self.directory = directory
        self.index = 1

    def run(self) -> List[Syscall]:
        syscalls = []

        for file in self.directory.glob("**/*.[c]"):
            syscalls.extend(self._find_syscalls_in_file(file))

        return syscalls

    def _find_syscalls_in_file(self, file: Path) -> List[Syscall]:
        syscalls = []

        with file.open() as fp:
            data = fp.read().splitlines()
            for index, line in enumerate(data):
                for definition in Definition:
                    if not line.startswith(definition.value):
                        continue

                    syscalls.append(
                        self._extract_syscall_from_file(
                            file=file,
                            definition=definition,
                            line=line,
                            stream=iter(data[index + 1 :]),
                            start=index + 1,
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

        while not declaration.endswith(")"):
            declaration += next(stream).strip()

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

        print(f"- Extracted syscall {str(self.index).zfill(4)}: {name}")
        self.index += 1

        return syscall
