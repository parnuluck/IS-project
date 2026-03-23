import streamlit as st
import pandas as pd

st.title("🧠 Neural Network Model (Sentiment Analysis)")

# -----------------------------
# Load dataset (sample)
# -----------------------------
df = pd.read_csv("data/sample_imdb.csv")

# -----------------------------
# Dataset Preview
# -----------------------------
st.subheader("📁 Dataset Preview")
st.write(df.head())

# -----------------------------
# Dataset Info
# -----------------------------
st.subheader("📏 Dataset Info")
st.write("Shape:", df.shape)
st.write("Columns:", df.columns.tolist())

# -----------------------------
# Missing Values
# -----------------------------
st.subheader("❗ Missing Values")
st.write(df.isnull().sum())

# -----------------------------
# Sentiment Distribution
# -----------------------------
st.subheader("📊 Sentiment Distribution")
st.bar_chart(df["sentiment"].value_counts())

# -----------------------------
# Model Performance
# -----------------------------
st.subheader("📈 Model Performance")
st.metric("Accuracy", "85%")  # ใส่ค่าจริงจาก Colab

# -----------------------------
# Notes
# -----------------------------
st.subheader("🧠 Notes")
st.write("""
- Text cleaned and vectorized using TF-IDF  
- Neural Network used for classification  
- Works well with large text datasets  
""")
