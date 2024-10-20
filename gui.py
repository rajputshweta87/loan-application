import streamlit as st
st.title('Loan Application App')
l=st.number_input("Please Enter your number for loan")
s=st.number_input("Please Enter your number for salary")
c=st.number_input("Please Enter your number for credit score")
if s>=40000 and c>=500:
    st.write("Congratulations!")
else:
    st.write("We are sorry")