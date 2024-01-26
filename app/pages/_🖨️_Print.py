import streamlit as st

st.set_page_config(page_title="Print", page_icon="🖨️")
with st.sidebar:
    start = st.date_input("From: ", format="DD/MM/YYYY")
    end = st.date_input("To: ", format="DD/MM/YYYY")
    
    