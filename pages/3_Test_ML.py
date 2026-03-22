import streamlit as st
import numpy as np
import pickle

st.title("Test Machine Learning Model")

# load model
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

st.subheader("Enter patient data")

inputs = []
for col in ["Pregnancies","Glucose","BloodPressure","SkinThickness",
            "Insulin","BMI","DiabetesPedigreeFunction","Age"]:
    inputs.append(st.number_input(col, min_value=0.0))

if st.button("Predict ML"):
    data = scaler.transform([inputs])
    result = model.predict(data)

    if result[0] == 1:
        st.error("Diabetes")
    else:
        st.success("No Diabetes")
