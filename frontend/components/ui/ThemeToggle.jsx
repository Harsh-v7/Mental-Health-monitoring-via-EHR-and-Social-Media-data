import { useEffect, useState } from "react";

export default function ThemeToggle() {
  const [theme, setTheme] = useState("light");

  useEffect(() => {
    document.documentElement.classList.toggle("dark", theme === "dark");
  }, [theme]);

  return (
    <button
      onClick={() => setTheme((prev) => (prev === "light" ? "dark" : "light"))}
      className="p-2 border rounded-lg text-sm"
    >
      Toggle {theme === "light" ? "🌙" : "☀️"}
    </button>
  );
}
