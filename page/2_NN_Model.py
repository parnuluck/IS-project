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
