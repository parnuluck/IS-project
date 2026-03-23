import streamlit as st
import joblib
import re

# load model
model = joblib.load("nn_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

def clean_text(text):
    text = text.lower()
    text = re.sub(r"<.*?>", "", text)
    text = re.sub(r"[^a-zA-Z]", " ", text)
    return text

st.title("Neural Network (Sentiment Analysis)")

review = st.text_area("Enter movie review")

if st.button("Predict"):
    if review.strip() == "":
        st.warning("Please enter a review")
    else:
        cleaned = clean_text(review)
        vec = vectorizer.transform([cleaned])
        pred = model.predict(vec)[0]

        if pred == 1:
            st.success("Positive 😊")
        else:
            st.error("Negative 😡")
