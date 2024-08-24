import { Link } from "react-router-dom";
import { Table } from "../types";
import React from "react";
import { useFetchContext } from "../use-fetch-context";

export default function ArchitecturesGrid() {
  const { data: tables, error } = useFetchContext<Table[]>();
  if (!tables) {
    return (
      <p className="font-mono text-zinc-50 text-sm text-center py-12">
        Loading...
      </p>
    );
  }

  return (
    <div className="grid grid-cols-5 gap-2 ">
      {tables!.map((table) => (
        <Link key={table.architecture} to={"/" + table.architecture}>
          <div className="px-2 py-2 text-sm shadow-lg bg-zinc-900 rounded-lg text-zinc-50 font-mono text-center hover:bg-zinc-700">
            {table.architecture}
          </div>
        </Link>
      ))}
    </div>
  );
}
