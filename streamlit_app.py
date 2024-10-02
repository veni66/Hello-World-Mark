import streamlit as st

st.title("🎈 my haechanie")

name = st.text_input("Name :")

st.write('Helo,', name)

if(name):
    st.write('helo,', name)
else:
    st.write("isi nama sayang!!!")