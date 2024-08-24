import React from "react";
import ReactDOM from "react-dom";
import App from "./App";

import { FetchProvider } from "./use-fetch-context";
import { Table } from "./types";
import Footer from "./components/Footer";

ReactDOM.render(
  <div className="flex flex-col min-h-screen min-w-screen px-20 py-10 bg-zinc-950">
    <div className="flex-grow">
      <FetchProvider<Table[]> url="./tables.json">
        <App />
      </FetchProvider>
    </div>
    <Footer />
  </div>,
  document.getElementById("root")
);
