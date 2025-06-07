import React from "react";
import SentimentChecker from "./pages/SentimentChecker";

export default function App() {
  return (
    <main className="min-h-screen bg-white dark:bg-gray-950 text-gray-900 dark:text-gray-100 p-4">
      <div className="flex justify-end">
        {/* Optional: Theme Toggle */}
        {/* You can uncomment the next line if ThemeToggle is set up */}
        {/* <ThemeToggle /> */}
      </div>
      <SentimentChecker />
    </main>
  );
}
