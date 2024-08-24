export type Table = {
  architecture: string;
  entries: Entry[];
};

export type Entry = {
  number: number;
  syscalls: Syscall[];
};

export type Syscall = {
  definition: DefinitionType;
  n: int;
  name: string;
  parameters: Record<string, string>;
  file: string;
  line: number;
};

export type DefinitionType =
  | "SYSCALL32_DEFINE"
  | "SYSCALL_DEFINE"
  | "COMPAT_SYSCALL_DEFINE"
  | "PPC32_SYSCALL_DEFINE";
