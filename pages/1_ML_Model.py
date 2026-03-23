import streamlit as st
import pandas as pd
import numpy as np

st.title("📊 Machine Learning Model")

# -----------------------------
# Dataset Section
# -----------------------------
st.subheader("📁 Dataset Preview")

# demo dataset (แทนของจริง)
df = pd.DataFrame({
    "Glucose": np.random.randint(80, 180, 100),
    "BMI": np.random.randint(18, 40, 100),
    "Age": np.random.randint(20, 70, 100),
    "Outcome": np.random.choice([0, 1], 100)
})

st.write(df.head())

# -----------------------------
# Dataset Info
# -----------------------------
st.subheader("📏 Dataset Info")
st.write("Shape:", df.shape)

# -----------------------------
# Class Distribution
# -----------------------------
st.subheader("📊 Class Distribution")
st.bar_chart(df["Outcome"].value_counts())

# -----------------------------
# Model Info
# -----------------------------
st.subheader("🤖 Models Used")
st.write("""
- Random Forest  
- Gradient Boosting  
- Logistic Regression  
- Voting Classifier (Ensemble)
""")

# -----------------------------
# Performance
# -----------------------------
st.subheader("📈 Model Performance")

accuracy = 0.75  # ใส่ค่าจริงของคุณได้
st.metric(label="Accuracy", value=f"{accuracy*100:.2f}%")

# -----------------------------
# Notes
# -----------------------------
st.subheader("🧠 Notes")
st.write("""
- Data preprocessing includes handling missing values and scaling  
- Ensemble model improves stability and performance  
- Suitable for structured/tabular data  
""")
