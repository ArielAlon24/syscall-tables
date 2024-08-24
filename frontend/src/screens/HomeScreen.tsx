import { Link } from "react-router-dom";
import { Table } from "../types";
import React, { useEffect } from "react";
import { useFetchContext } from "../use-fetch-context";
import ErrorScreen from "./ErrorScreen";
import { TiHome } from "react-icons/ti";
import { FaGithub } from "react-icons/fa";
import Header from "../components/Header";
import Footer from "../components/Footer";
import ArchitecturesGrid from "../components/ArchitecturesGrid";

export default function HomeScreen() {
  return (
    <div className="flex flex-col gap-4 ">
      <Header heading="Syscall Tables" />
      <p className="font-mono text-zinc-50 text-sm p-2">
        All of the following syscall tables were extracted from the{" "}
        <Link
          to="https://github.com/torvalds/linux"
          className="text-blue-400 hover:text-blue-500 hover:underline transition-colors"
        >
          Linux GitHub repo
        </Link>
      </p>

      <ArchitecturesGrid />
    </div>
  );
}
