import { Link } from "react-router-dom";
import { Table } from "../types";
import React, { useEffect } from "react";
import { useFetchContext } from "../use-fetch-context";
import ErrorScreen from "./ErrorScreen";

export default function HomeScreen() {
  const { data: tables, error } = useFetchContext<Table[]>();
  if (!tables) {
    return <ErrorScreen />;
  }

  return (
    <div className="flex flex-col gap-10">
      {tables!.map((table) => {
        return (
          <Link key={table.architecture} to={"/table/" + table.architecture}>
            {table.architecture}
          </Link>
        );
      })}
    </div>
  );
}
