// Full functional SentimentChecker component with reusable UI parts
// Requires: Tailwind CSS setup and these files in frontend/components/ui/
// - SentimentBadge.jsx
// - LoadingSpinner.jsx
// - ThemeToggle.jsx
// - Footer.jsx

import React, { useState } from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";

import SentimentBadge from "./components/ui/SentimentBadge";
import LoadingSpinner from "./components/ui/LoadingSpinner";
import ThemeToggle from "./components/ui/ThemeToggle";
import Footer from "./components/ui/Footer";

export default function SentimentChecker() {
  const [text, setText] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    setLoading(true);
    setResult(null);
    try {
      const response = await fetch("https://k9doxyr2a.execute-api.ap-south-1.amazonaws.com/sentiment", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ text }),
      });

      const data = await response.json();
      setResult(data);
    } catch (error) {
      console.error("Error fetching sentiment:", error);
    }
    setLoading(false);
  };

  return (
    <div className="min-h-screen bg-white dark:bg-gray-900 text-gray-900 dark:text-white flex flex-col justify-between">
      <div className="max-w-xl mx-auto mt-10 p-4">
        <div className="flex justify-between items-center mb-4">
          <h2 className="text-2xl font-bold">Mental Health Sentiment Checker</h2>
          <ThemeToggle />
        </div>

        <Card>
          <CardContent className="space-y-4">
            <Input
              type="text"
              placeholder="Enter your thoughts..."
              value={text}
              onChange={(e) => setText(e.target.value)}
            />
            <Button onClick={handleSubmit} disabled={loading || !text}>
              {loading ? "Checking..." : "Analyze"}
            </Button>
            {loading && <LoadingSpinner />}
            {result && (
              <div className="bg-gray-100 dark:bg-gray-800 p-3 rounded-xl mt-4 space-y-2">
                <p className="text-sm">Sentiment Score: {result.sentiment_score}</p>
                <SentimentBadge label={result.sentiment_label} />
              </div>
            )}
          </CardContent>
        </Card>
      </div>

      <Footer />
    </div>
  );
}
