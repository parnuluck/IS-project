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
