import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model

st.title("Test Neural Network")

model = load_model("nn_model.h5")

inputs = []
for col in ["Pregnancies","Glucose","BloodPressure","SkinThickness",
            "Insulin","BMI","DiabetesPedigreeFunction","Age"]:
    inputs.append(st.number_input(col))

if st.button("Predict NN"):
    result = model.predict([inputs])

    if result[0][0] > 0.5:
        st.error("Diabetes")
    else:
        st.success("No Diabetes")