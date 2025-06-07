# Flask backend to receive user input and forward it to AWS Lambda API
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Replace this with your real API Gateway endpoint
API_GATEWAY_URL = "https://k9doxyr2a.execute-api.ap-south-1.amazonaws.com/sentiment"   

@app.route("/analyze", methods=["POST"])
def analyze_sentiment():
    try:
        user_input = request.json.get("text", "")

        if not user_input:
            return jsonify({"error": "Text is required"}), 400

        # Forward request to AWS Lambda (API Gateway)
        response = requests.post(
            API_GATEWAY_URL,
            json={"text": user_input},
            headers={"Content-Type": "application/json"},
        )

        result = response.json()
        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
