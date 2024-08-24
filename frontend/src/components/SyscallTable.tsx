import { Link } from "react-router-dom";
import { Entry, Table } from "../types";
import React from "react";

type SyscallTableProps = {
  table: Table;
};

export default function SyscallTable(props: SyscallTableProps) {
  const { table } = props;

  return (
    <table>
      <tr>
        <th>number</th>
        <th>name</th>
        <th>ARG0</th>
        <th>ARG1</th>
        <th>ARG2</th>
        <th>ARG3</th>
        <th>ARG4</th>
        <th>ARG5</th>
        <th>link</th>
      </tr>
      {table.entries.map((entry: Entry) => {
        const syscalls = entry.syscalls;
        if (syscalls.length == 0) {
          return (
            <tr>
              <td>{entry.number}</td>
              <td>no entry</td>
            </tr>
          );
        }

        const syscall = syscalls[0];
        return (
          <tr>
            <td>{entry.number}</td>
            <td>{syscall.name}</td>
            {Object.entries(syscall.parameters).map((pairs) => {
              const [key, value] = pairs;
              return (
                <td>
                  {key}: {value}
                </td>
              );
            })}
            <Link
              to={`https://github.com/torvalds/linux/blob/master/${syscall.file}#L${syscall.line}`}
            >
              Github
            </Link>
          </tr>
        );
      })}
    </table>
  );
}
