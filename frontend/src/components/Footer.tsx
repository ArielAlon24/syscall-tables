import React, { useEffect, useState } from "react";

export default function Footer() {
  const [datetime, setDatetime] = useState<string | null>(null);

  useEffect(() => {
    fetch("./last-update.txt")
      .then((response) => response.text())
      .then(setDatetime);
  });

  return (
    <div className="relative mt-5 bg-zinc-900 px-4 py-3 rounded-lg">
      <p className="w-full text-center text-xs text-zinc-50 font-mono">
        last update: {datetime ? datetime : "Loading..."}
      </p>
    </div>
  );
}
