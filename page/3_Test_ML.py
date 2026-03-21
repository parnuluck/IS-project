import streamlit as st
import numpy as np
import pickle

st.title("Test Machine Learning Model")

st.subheader("Enter patient data")

model = pickle.load(open("model.pkl", "rb"))

inputs = []
for col in ["Pregnancies","Glucose","BloodPressure","SkinThickness",
            "Insulin","BMI","DiabetesPedigreeFunction","Age"]:
    inputs.append(st.number_input(col))

if st.button("Predict ML"):
    result = model.predict([inputs])
    
    if result[0] == 1:
        st.error("Diabetes")
    else:
        st.success("No Diabetes")
