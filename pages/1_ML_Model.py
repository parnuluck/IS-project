import streamlit as st

st.title("Machine Learning Model")

st.write("""
Dataset:
- Pima Indians Diabetes Dataset

Data preprocessing:
- Replaced zero values with NaN
- Filled missing values using mean
- Applied feature scaling

Model:
- Random Forest
- Gradient Boosting
- Logistic Regression
- Combined using VotingClassifier

Result:
- Accuracy around 75%
""")

st.subheader("Additional Dataset")
st.write("""
Dataset: Breast Cancer Wisconsin Dataset

Source:
- Built-in dataset from scikit-learn library

Features:
- Mean radius
- Mean texture
- Mean perimeter
- Mean area
- Mean smoothness
- And other statistical features (total ~30 features)

Data Characteristics:
- Binary classification (Malignant / Benign)
- Some features require scaling due to different ranges
- Contains noise and requires preprocessing

Preprocessing:
- Feature scaling using StandardScaler
- Handling inconsistent feature ranges

Purpose:
- Used to validate model performance on a different dataset
- Demonstrates generalization ability of the model
""")
