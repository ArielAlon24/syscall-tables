import React from "react";
import { Table } from "../types";
import SyscallTable from "../components/SyscallTable";
import { useFetchContext } from "../use-fetch-context";
import LoadingScreen from "./LoadingScreen";
import ErrorScreen from "./ErrorScreen";
import { useParams } from "react-router-dom";

type TableScreenProps = {
  architecture: string;
};

export default function TableScreen() {
  const { architecture } = useParams<TableScreenProps>();
  const { data: tables, error } = useFetchContext<Table[]>();
  if (!tables) {
    return <LoadingScreen />;
  }
  if (error) {
    return <ErrorScreen />;
  }

  const table = tables!.find((table) => table.architecture == architecture)!;
  return <SyscallTable table={table} />;
}
