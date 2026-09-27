import streamlit as st
import joblib


# Load trained model
model = joblib.load("phishing_model.pkl")


# Page configuration
st.set_page_config(
    page_title="AI Phishing Email Detector",
    page_icon="🛡️",
    layout="centered"
)


# Title
st.title("🛡️ AI Phishing Email Detector")

st.write(
    "Enter an email below and the machine-learning model "
    "will classify it as legitimate or phishing."
)


# Email input
email_text = st.text_area(
    "Paste email content here:",
    height=250,
    placeholder="Paste the email you want to analyze..."
)


# Analyze button
if st.button("🔍 Analyze Email"):

    if email_text.strip() == "":
        st.warning("Please enter an email before analyzing.")

    else:
        # Make prediction
        prediction = model.predict([email_text])[0]

        # Get prediction probability
        probabilities = model.predict_proba([email_text])[0]

        confidence = max(probabilities) * 100

        # Display result
        if prediction == 1:
            st.error("🚨 PHISHING EMAIL")
            st.write(f"**Confidence:** {confidence:.2f}%")

        else:
            st.success("✅ LIKELY LEGITIMATE")
            st.write(f"**Confidence:** {confidence:.2f}%")

        # Show probabilities
        st.subheader("Prediction Details")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Legitimate",
                f"{probabilities[0] * 100:.2f}%"
            )

        with col2:
            st.metric(
                "Phishing",
                f"{probabilities[1] * 100:.2f}%"
            )
            