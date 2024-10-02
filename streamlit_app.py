import streamlit as st

# Judul aplikasi
st.title("🎈 Masukkan Nama Lengkap")

# Input untuk nama depan
first_name = st.text_input("Nama Depan:")

# Input untuk nama belakang
last_name = st.text_input("Nama Belakang:")

# Menampilkan pesan
if first_name and last_name:  # Memeriksa apakah kedua input terisi
    st.write('Halo,', first_name, last_name)
else:
    st.write("Silakan masukkan nama lengkap kamu!")
