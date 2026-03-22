import streamlit as st

st.title("Neural Network Model")

st.write("""
Dataset:
- IMDb Movie Reviews (text data)

Features:
- review (text)
- sentiment (positive / negative)

Data Issues:
- HTML tags
- symbols
- inconsistent text length

Preprocessing:
- convert to lowercase
- remove HTML tags
- remove special characters
- TF-IDF vectorization (convert text to numbers)

Model structure:
- Dense 128 (ReLU)
- Dense 64 (ReLU)
- Output layer (Sigmoid)

Training:
- Optimizer: Adam
- Loss: Binary Crossentropy
- Epochs: 3

Purpose:
- Predict sentiment of movie reviews
""")
