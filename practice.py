import pandas as pd
import streamlit as st

# Simple login page
email = st.text_input("Enter email")
password = st.text_input("Enter password")
gender = st.selectbox("Select Gender", ["male", "female", "other"])
btn = st.button("Login")
if btn:
    if email == "omkar@gmail.com" and password == "123":
        # st.success("Login Successful")
        st.balloons()
        st.write(gender)
    else:
        st.error("Login Failed")
# st.title('Startup Dashboard')
# st.header("I'm learning streamlit")
# st.subheader("I'm new to streamlit")
# # For writing paragraph
# st.write("This is paragraph")
#
# st.markdown("""
# ### My Favourite cars
# - Range Rover Vogue
# - Mercedes G63
# - Ford Endeavour
# """)
#
# # for writing code in your website
# st.code("""
# def find_sum(num):
#     sum = 0
#     for i in range(num):
#         sum += i
#
#     return sum
# """)
#
# df = pd.DataFrame({
#     "name": ["Omkar", "Omi", "Jadhav"],
#     "marks": [90, 98, 96],
#     "package": [12, 10, 8]
# })
#
# st.dataframe(df)
#
# # displaying metrics
# # st.metric("Revenue")
#
# # Creating layouts
# # sidebar
# st.sidebar.subheader("This is sidebar")
#
# # columns
# col1, col2 = st.columns(2)
#
# with col1:
#     st.subheader("This is column1")
#
# with col2:
#     st.subheader("This is column2")
#
# # showing status
# st.success("Login Successful.")
# st.error("Login failed.")
#
# # Progress bar
# # st.progress()
#
# # Taking input from user
# # taking text input
# email = st.text_input("Enter your email")
# number = st.number_input("Enter your age")
# date = st.date_input("Enter date")