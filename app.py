import streamlit as st
import joblib
import pandas as pd

model = joblib.load("linear.pkl")

st.title(":red[Insurance Prediction]")


age = st.number_input("Enter your age", min_value=18, max_value=60)

sex = st.selectbox("Enter your Gender", ["male", "female"])

bmi = st.number_input("Enter your bmi", min_value=20.0, max_value=50.0)

children = st.number_input("How many childrens", min_value=0, max_value=5)

smoker = st.selectbox("Are u a smooker", ["yes", "no"])

region = st.selectbox("Enter your Region", ["southeast", "southwest", "northwest", "northeast"])


if st.button("Predict"):
    input_data = pd.DataFrame(
        {
            "age":[age],
            "sex":[sex],
            "bmi":[bmi],
            "children":[children],
            "smoker":[smoker],
            "region":[region]
        }
    )
    
    pred = model.predict(input_data)
    st.success(pred)
