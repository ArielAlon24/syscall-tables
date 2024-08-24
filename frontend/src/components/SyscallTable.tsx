import { Link } from "react-router-dom";
import { Entry, Table } from "../types";
import React from "react";
import { IoIosLink } from "react-icons/io";

type SyscallTableProps = {
  table: Table;
};

export default function SyscallTable(props: SyscallTableProps) {
  const { table } = props;

  return (
    <div className="overflow-x-auto font-mono rounded-lg text-xs">
      <table className="min-w-full bg-zinc-900 text-zinc-50 rounded-xl shadow-lg">
        <thead className="bg-zinc-900">
          <tr>
            <Th label="#" center />
            <Th label="Name" />

            <Th label="ARG0" />
            <Th label="ARG1" />
            <Th label="ARG2" />
            <Th label="ARG3" />
            <Th label="ARG4" />
            <Th label="ARG5" />
          </tr>
        </thead>
        <tbody className="mt-20">
          {table.entries.map((entry: Entry, entryIndex) => {
            const syscalls = entry.syscalls;
            if (syscalls.length === 0) {
              return (
                <Tr key={entryIndex}>
                  <Td label={entry.number.toString()} center />
                  <Td colSpan={8}></Td>
                </Tr>
              );
            }

            const syscall = syscalls[0];
            return (
              <Tr key={entryIndex} filled>
                <Td center>
                  <span className="text-zinc-400 font-normal">
                    {entry.number.toString()}
                  </span>{" "}
                </Td>

                <Td>
                  <div className="flex flex-row items-center gap-2">
                    <Link
                      to={`https://github.com/torvalds/linux/blob/master/${syscall.file}#L${syscall.line}`}
                      className="text-center flex flex-row items-center justify-center"
                    >
                      <IoIosLink className="text-blue-400 hover:text-blue-500 transition-colors" />
                    </Link>
                    <span>{syscall.name}</span>{" "}
                  </div>
                </Td>
                {(() => {
                  const pairs = Object.entries(syscall.parameters);
                  const filledPairs = pairs.concat(
                    new Array(6 - pairs.length).fill(["", ""])
                  );

                  return filledPairs.map(([key, value], index) => (
                    <Td key={index}>
                      {key && value ? (
                        <span>
                          <span className="text-red-400 font-semibold">
                            {value}
                          </span>{" "}
                          <span className="text-zinc-50">{key}</span>
                        </span>
                      ) : (
                        <span className="text-zinc-400">-</span>
                      )}
                    </Td>
                  ));
                })()}
              </Tr>
            );
          })}
        </tbody>
      </table>
    </div>
  );
}

type ThProps = {
  label: string;
  center?: undefined | boolean;
};

function Th(props: ThProps) {
  return (
    <th
      className={`py-3 px-4 border-b-4  border-zinc-800 ${
        props.center ? "text-center" : "text-left"
      } font-semibold lowercase text-sm text-zinc-50 bg-zinc-900`}
    >
      {props.label}
    </th>
  );
}

type TdProps = {
  label?: undefined | string;
  center?: undefined | boolean;
  key?: undefined | number;
  children?: undefined | React.ReactNode;
  colSpan?: undefined | number;
};

function Td(props: TdProps) {
  return (
    <td
      className={`py-2 px-4 border-b-4 border-zinc-800 ${
        props.center ? " text-center " : " text-left "
      }`}
      key={props.key}
      colSpan={props.colSpan}
    >
      {props.label ? props.label : props.children}
    </td>
  );
}

type TrProps = {
  filled?: undefined | boolean;
  children?: undefined | React.ReactNode;
  key: number;
};

function Tr(props: TrProps) {
  if (props.filled) {
    return (
      <tr key={props.key} className="hover:bg-zinc-700 bg-zinc-900 ">
        {props.children}
      </tr>
    );
  }
  return (
    <tr key={props.key} className="bg-zinc-800  ">
      {props.children}
    </tr>
  );
}
