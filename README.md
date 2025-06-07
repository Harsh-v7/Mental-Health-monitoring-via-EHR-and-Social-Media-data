# 🧠 Mental Health Monitoring via EHR and Social Media Data

A full-stack, cloud-integrated project for analyzing and visualizing mental health patterns using EHR datasets and social media inputs. Includes Streamlit-based ML prototype, AWS Lambda-based sentiment service, and a Tailwind-powered React frontend.

---

## 📚 Features

- 🧠 Sentiment analysis on social media text using TextBlob or ML models
- 📊 ML model integration (XGBoost) trained on EHR-style statements
- ⚙️ Streamlit UI with joblib models for demo/testing
- ☁️ AWS Lambda + API Gateway for real-time inference
- 💻 React + Tailwind frontend with dark/light theme and dynamic feedback

---

## 📁 Project Structure

```
Mental-Health-monitoring-via-EHR-and-Social-Media-data/
├── frontend/                  # React + Tailwind app
│   ├── pages/
│   └── components/ui/
├── sentiment_lambda/         # Lambda function code (sentiment_analysis.py)
├── app.py                    # Flask backend (optional)
├── streamlit_app/            # Streamlit ML prototype
│   ├── streamlit.ipynb
│   ├── xgb_model.pkl
│   └── vectorizer.pkl
├── README.md
```

---

## 🚀 Getting Started

### ▶️ Streamlit Interface (ML Prototype)

1. Install dependencies:
```bash
pip install streamlit scikit-learn pandas numpy xgboost
```
2. Run Streamlit:
```bash
streamlit run streamlit_app/streamlit.ipynb
```

Or convert to .py and run:
```bash
streamlit run streamlit_app/app.py
```

---

### 🌐 React + Tailwind Frontend

1. Navigate to frontend folder:
```bash
cd frontend
```
2. Install dependencies:
```bash
npm install
```
3. Run the app:
```bash
npm run dev
```
4. Update SentimentChecker.jsx:
Replace:
```js
const response = await fetch("<your-api-url>")
```
With your deployed AWS Lambda API Gateway URL.

---

### ⚙️ AWS Lambda + API Gateway (Backend)

1. Prepare Lambda function (sentiment_analysis.py)
2. Package with dependencies:
```bash
pip install textblob -t .
zip -r sentiment_lambda.zip .
```
3. Deploy to AWS Lambda
4. Set up API Gateway with POST route
5. Test via Postman or frontend fetch()

---

## 📦 Tech Stack

- 💡 Machine Learning: XGBoost, Scikit-learn
- 📊 Visualization: Streamlit
- ⚙️ API: AWS Lambda, Flask (optional)
- 💻 Frontend: React + Tailwind CSS + shadcn/ui

---
Made by Harsh Verma
