import streamlit as st

st.title("Student Result Calculator")

name = st.text_input("Student Name")
m1 = st.number_input("Marks in Subject 1", min_value=0, max_value=100, value=0)
m2 = st.number_input("Marks in Subject 2", min_value=0, max_value=100, value=0)
m3 = st.number_input("Marks in Subject 3", min_value=0, max_value=100, value=0)

if st.button("Calculate"):
    if name.strip() == "":
        st.warning("Please enter student name")
    else:
        total = m1 + m2 + m3
        percentage = (total / 300) * 100

        st.write("Name : " + name)
        st.write("Total Marks : " + str(total) + " / 300")
        st.write("Percentage : " + str(round(percentage, 2)) + " %")

        if m1 >= 40 and m2 >= 40 and m3 >= 40:
            st.success("Result : Pass")
        else:
            st.error("Result : Fail")