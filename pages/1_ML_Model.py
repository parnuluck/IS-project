import streamlit as st
import pandas as pd

st.title("📊 Machine Learning Model")

# -----------------------------
# Load dataset
# -----------------------------
df = pd.read_csv("diabetes.csv")

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
# Class Distribution
# -----------------------------
st.subheader("📊 Class Distribution")
st.bar_chart(df["Outcome"].value_counts())

# -----------------------------
# Statistics
# -----------------------------
st.subheader("📊 Statistical Summary")
st.write(df.describe())

# -----------------------------
# Model Performance
# -----------------------------
st.subheader("📈 Model Performance")
st.metric("Accuracy", "75%")  # ใส่ค่าจริง

# -----------------------------
# Models Used
# -----------------------------
st.subheader("🤖 Models Used")
st.write("""
- Random Forest  
- Gradient Boosting  
- Logistic Regression  
- Voting Classifier  
""")
