import streamlit as st

st.title("Celsius to Fahrenheit Converter")

celsius = st.number_input("Temperature in Celsius", value=0.0)

if st.button("Convert"):
    fahrenheit = (celsius * 9 / 5) + 32
    st.success("Temperature in Fahrenheit is : " + str(round(fahrenheit, 2)))