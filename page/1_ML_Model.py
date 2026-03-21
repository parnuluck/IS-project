import streamlit as st

st.title("Machine Learning Model")

st.write("""
This project uses Ensemble Learning which combines:
- Random Forest
- Gradient Boosting
- Logistic Regression

These models are combined using VotingClassifier to improve accuracy.

Data preprocessing includes:
- Handling missing values
- Replacing zero values
- Scaling features
""")
