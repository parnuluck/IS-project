import streamlit as st
import pickle
import re

# load model
model = pickle.load(open("nn_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

def clean_text(text):
    text = text.lower()
    text = re.sub(r"<.*?>", "", text)
    text = re.sub(r"[^a-zA-Z]", " ", text)
    return text

st.title("Neural Network (Sentiment Analysis)")

review = st.text_area("Enter movie review")

if st.button("Predict"):
    cleaned = clean_text(review)
    vec = vectorizer.transform([cleaned])
    pred = model.predict(vec)[0]

    if pred == 1:
        st.success("Positive 😊")
    else:
        st.error("Negative 😡")

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
