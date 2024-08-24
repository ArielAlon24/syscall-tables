import React from "react";
import { Table } from "../types";
import SyscallTable from "../components/SyscallTable";
import { useFetchContext } from "../use-fetch-context";
import LoadingScreen from "./LoadingScreen";
import ErrorScreen from "./ErrorScreen";
import { Link, useParams } from "react-router-dom";
import { TiHome } from "react-icons/ti";
import Header from "../components/Header";
import Footer from "../components/Footer";

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
  return (
    <div className="flex flex-col gap-4">
      <Header heading={architecture!} />
      <div className="m-2 p-2"></div>

      <SyscallTable table={table} />
    </div>
  );
}
