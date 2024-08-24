import React from "react";
import ReactDOM from "react-dom";
import App from "./App";

import { FetchProvider } from "./use-fetch-context";
import { Table } from "./types";

ReactDOM.render(
  <FetchProvider<Table[]> url="./tables.json">
    <App />
  </FetchProvider>,
  document.getElementById("root")
);
