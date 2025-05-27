import streamlit as st
import time
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# --- Load model and vectorizer ---
model = joblib.load('xgb_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

# --- Label mapping ---
label_mapping = {
    0: 'Anxiety',
    1: 'Normal',
    2: 'Depression',
    3: 'Suicidal',
    4: 'Stress',
    5: 'Bipolar',
    6: 'Personality disorder'
}

# --- Page Configuration ---
st.set_page_config(page_title="Mental Health Classifier", page_icon="🧠", layout="wide")
st.markdown("""
    <style>
        .main .block-container {
            max-width: 1100px;
            padding-left: 2rem;
            padding-right: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("### 🧠 Mental Health Classifier")
    st.title("About the App")

    st.markdown("""
    **Mental Health Monitoring Tool**  
    Built with **XGBoost**, **TF-IDF**, and **Streamlit**.

    This app classifies mental health-related statements into:
    """)

    st.markdown("""
    - 🌀 Anxiety  
    - 🙂 Normal  
    - 🌧 Depression  
    - ⚠️ Suicidal  
    - 😣 Stress  
    - 🔄 Bipolar  
    - 🎭 Personality Disorder  
    """)

    st.markdown("—" * 30)

    st.subheader("💬 Try these:")
    st.markdown("""
    - *"I feel like nothing makes sense anymore."*  
    - *"I’m just tired and anxious all the time."*  
    - *"Everything’s been okay lately."*
    """)

    st.markdown("—" * 30)

    st.subheader("⚙️ Options")
    dark_mode = st.checkbox("🌙 Use Dark Mode (browser theme)")

    if 'history' in st.session_state and st.session_state.history:
        hist_df = pd.DataFrame(st.session_state.history, columns=["Statement", "Prediction"])
        csv = hist_df.to_csv(index=False).encode("utf-8")
        st.download_button("⬇️ Download Prediction History", csv, "prediction_history.csv", "text/csv")


# --- Title and Description ---
st.title("🧠 Mental Health Statement Classifier")
st.markdown("Use this app to classify mental health-related statements into categories like **anxiety**, **depression**, or **stress** using a machine learning model.")

# --- Initialize session state ---
if 'history' not in st.session_state:
    st.session_state.history = []

# --- Input Form ---
with st.form(key="predict_form"):
    user_input = st.text_area("✍️ Enter your statement here", height=150, placeholder="Type a mental health-related sentence...")
    submitted = st.form_submit_button("🔍 Predict")

# --- Prediction Display ---
prediction_container = st.container()

if submitted:
    if user_input.strip():
        # Spinner effect
        with st.spinner("Analyzing your statement..."):
            time.sleep(0.4)

        # Prediction
        vect_text = vectorizer.transform([user_input])
        prediction = model.predict(vect_text)[0]
        st.session_state.history.append((user_input, label_mapping[prediction]))

        # Show prediction
        with prediction_container:
            st.success(f"🧾 **Prediction:** {label_mapping[prediction]}")

            if hasattr(model, "predict_proba"):
                probs = model.predict_proba(vect_text)[0]
                st.subheader("📊 Confidence Scores")
                fig, ax = plt.subplots(figsize=(8, 5))
                sns.barplot(x=probs, y=list(label_mapping.values()), palette="crest", ax=ax)
                ax.set_xlim(0, 1)
                ax.set_xlabel("Confidence Probability")
                ax.set_title("Model Confidence per Class")
                st.pyplot(fig)
    else:
        st.warning("⚠️ Please enter a valid statement.")

# --- History View ---
with st.expander("🕒 View Prediction History (last 10)"):
    if st.session_state.history:
        for idx, (text, pred) in enumerate(reversed(st.session_state.history[-10:]), 1):
            st.markdown(f"**{idx}.** _\"{text}\"_ → **{pred}**")
    else:
        st.info("No predictions yet.")

# --- Footer ---
st.markdown("---")
st.markdown("📍 *Built for the Major Project on Mental Health Monitoring via EHR and Social Media Data.*")
