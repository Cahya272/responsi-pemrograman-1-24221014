import streamlit as st

st.title("Hitung Keliling dan Luas")
st.write("deskripsi"
)
panjang = st.number_input("masukkan panjang persegi: ", value=0)
st.write("The current number is ", panjang)

lebar = st.number_input("masukkan lebar persegi: ", value=0)
st.write("The current number is ", lebar)

if(panjang & lebar):
    st.subheader('keliling')
    st.write(2 * (panjang + lebar))
    st.subheader('luas')
    st.write(panjang + lebar)
    