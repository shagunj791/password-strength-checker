# app_streamlit.py
import streamlit as st
from check_password import check_password_strength

st.title("Password Strength Checker")
pwd = st.text_input("Enter password", type="password")
if st.button("Check"):
    res = check_password_strength(pwd)
    st.subheader(res['label'])
    st.write(f"Entropy: {res['entropy']:.1f} bits")
    st.write("Suggestions:")
    for s in res['suggestions']:
        st.write("-", s)
