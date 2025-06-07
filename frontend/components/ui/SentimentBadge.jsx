export default function SentimentBadge({ label }) {
  const color =
    label === "positive" ? "bg-green-200 text-green-800" :
    label === "negative" ? "bg-red-200 text-red-800" :
    "bg-yellow-200 text-yellow-800";

  return (
    <span className={`px-3 py-1 rounded-full text-sm font-medium ${color}`}>
      {label.charAt(0).toUpperCase() + label.slice(1)}
    </span>
  );
}
