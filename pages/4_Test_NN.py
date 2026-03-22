import streamlit as st
import pickle
import re
from tensorflow.keras.models import load_model

# load model
model = load_model("nn_model.h5")

# load vectorizer
with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

# clean text
def clean_text(text):
    text = text.lower()
    text = re.sub(r"<.*?>", "", text)
    text = re.sub(r"[^a-zA-Z]", " ", text)
    return text

st.title("Sentiment Analysis (IMDb)")

review = st.text_area("Enter your review")

if st.button("Predict"):
    cleaned = clean_text(review)
    vec = vectorizer.transform([cleaned]).toarray()
    pred = model.predict(vec)[0][0]

    if pred > 0.5:
        st.success("Positive 😊")
    else:
        st.error("Negative 😡")
