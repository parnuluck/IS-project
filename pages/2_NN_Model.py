import streamlit as st

st.title("Neural Network Model")

st.write("""
Dataset preprocessing:
- Normalization using StandardScaler

Model structure:
- Input layer
- 2 hidden layers (ReLU)
- Output layer (Sigmoid)

Training:
- Optimizer: Adam
- Loss: Binary Crossentropy
- Epochs: 20

Result:
- Accuracy around 74%
""")


st.subheader("Additional Dataset")

st.write("""
Dataset: Breast Cancer Wisconsin Dataset

Source:
- Scikit-learn

Preprocessing:
- Normalization using StandardScaler

Model Usage:
- Neural Network can also be applied to this dataset
- Suitable for binary classification tasks

Purpose:
- To compare model performance across multiple datasets
- Ensures robustness of the Neural Network model
""")
