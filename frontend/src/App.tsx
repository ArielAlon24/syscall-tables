import React from "react";
import { HashRouter as Router, Route, Routes } from "react-router-dom";
import TableScreen from "./screens/TableScreen";
import HomeScreen from "./screens/HomeScreen";
import "./index.css";

export default function App() {
  return (
    <Router basename="/">
      <Routes>
        <Route path="/" element={<HomeScreen />} />
        <Route path="/table/:architecture" element={<TableScreen />} />
      </Routes>
    </Router>
  );
}
