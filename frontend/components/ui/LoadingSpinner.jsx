export default function LoadingSpinner() {
  return (
    <div className="flex justify-center mt-4">
      <svg className="animate-spin h-6 w-6 text-gray-600" viewBox="0 0 24 24">
        <circle cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" fill="none" />
        <path d="M4 12a8 8 0 018-8" fill="currentColor" />
      </svg>
    </div>
  );
}
