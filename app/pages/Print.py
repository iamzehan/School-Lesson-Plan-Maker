import os
import csv
import streamlit as st
from datetime import datetime
from utils.essentials import (
    date_translate,
    findDay,
    show_table,
    convert_to_datetime
)

def read_from_csv(path):
    with open(path, mode='r') as file:
        reader = csv.reader(file)
        data = list(reader)
    return data

st.set_page_config(page_title="Print", page_icon="🖨️")

# this will take the range 
with st.sidebar:
    _class = st.selectbox("Class: ", ["I","II","III","IV","V","VI","VII","VIII","IX", "X"])
    section = st.selectbox("Section", ["Abyad"])
    st.markdown("<h2 align='center'> Range of Date </h2>", unsafe_allow_html=True)
    start = st.date_input("From: ", format="DD/MM/YYYY")
    end = st.date_input("To: ", format="DD/MM/YYYY")
    size = st.slider("Select header size:",min_value=12, value=18, max_value=24)
    year, month, start_day = date_translate(str(start))
    year, month, end_day = date_translate(str(end))
    path = f"app/data/{year}/{month}/"
    files = os.listdir(path)
    filtered_files = [file for file in files if int(start_day) <= int(file.replace(".csv","")) <= int(end_day)]
    

st.markdown("""<center><img height=40 width=40 style='border-radius: 50px' src="https://shorturl.at/imMSW" </center>""", unsafe_allow_html=True)
st.markdown(f"<h2 align='center' style='font-size:{size}px;'> Al-Burooj International School </h2>", unsafe_allow_html=True)
st.markdown(f"<center>Class: {_class} ({section}) </center>",unsafe_allow_html=True)
st.markdown(f"<center>(From {start}, {findDay(str(start))} to {end}, {findDay(str(end))})</center>",unsafe_allow_html=True)
for file in filtered_files:
    st.write("""<br>""",unsafe_allow_html=True)
    date = convert_to_datetime(f"{year}-{month}-{file.replace('.csv','')}")
    data = read_from_csv(path+file)
    show_table(data, date)
    
    

    