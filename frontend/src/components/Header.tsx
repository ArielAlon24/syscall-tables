import React from "react";
import { FaGithub } from "react-icons/fa";
import { TiHome } from "react-icons/ti";
import { Link } from "react-router-dom";

type HeaderProps = {
  heading: string;
};

export default function Header(props: HeaderProps) {
  const { heading } = props;
  return (
    <div className="relative flex items-center bg-zinc-900 px-4 py-2 rounded-lg">
      <Link to="/" className="absolute left-0 px-5">
        <TiHome className="text-zinc-50 hover:text-zinc-400" />
      </Link>
      <h1 className="w-full text-center font-semibold text-zinc-50 font-mono">
        {heading}
      </h1>
      <Link
        to="https://github.com/ArielAlon24/syscall-tables"
        className="absolute right-0 px-5"
      >
        <FaGithub className="text-zinc-50 hover:text-zinc-400" />
      </Link>
    </div>
  );
}
