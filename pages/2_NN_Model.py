import streamlit as st
import pandas as pd
import numpy as np

st.title("🧠 Neural Network Model (Sentiment Analysis)")

# -----------------------------
# Dataset Preview
# -----------------------------
st.subheader("📁 Dataset Preview")

df = pd.DataFrame({
    "review": [
        "This movie is amazing",
        "I hate this film",
        "Best movie ever",
        "Worst experience"
    ],
    "sentiment": [1, 0, 1, 0]
})

st.write(df)

# -----------------------------
# Dataset Info
# -----------------------------
st.subheader("📏 Dataset Info")
st.write("Shape:", df.shape)

# -----------------------------
# Class Distribution
# -----------------------------
st.subheader("📊 Sentiment Distribution")
st.bar_chart(df["sentiment"].value_counts())

# -----------------------------
# Preprocessing
# -----------------------------
st.subheader("⚙️ Preprocessing Steps")
st.write("""
- Convert text to lowercase  
- Remove HTML tags  
- Remove special characters  
- TF-IDF Vectorization  
""")

# -----------------------------
# Model Structure
# -----------------------------
st.subheader("🧠 Model Architecture")
st.write("""
- Dense (64) → ReLU  
- Dense (32) → ReLU  
- Output (Sigmoid)  
""")

# -----------------------------
# Performance
# -----------------------------
st.subheader("📈 Model Performance")

accuracy = 0.85  # ใส่ค่าจริงจาก Colab
st.metric(label="Accuracy", value=f"{accuracy*100:.2f}%")

# -----------------------------
# Example Prediction
# -----------------------------
st.subheader("🔍 Example Predictions")

example_reviews = [
    "I love this movie",
    "This is terrible"
]

example_preds = ["Positive", "Negative"]

for r, p in zip(example_reviews, example_preds):
    st.write(f"**Review:** {r}")
    st.write(f"Prediction: {p}")
    st.write("---")

# -----------------------------
# Notes
# -----------------------------
st.subheader("🧠 Notes")
st.write("""
- Neural Network handles text via vectorization  
- Works better with large datasets  
- Captures complex patterns in language  
""")
