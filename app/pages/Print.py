import os
import csv
import streamlit as st
from utils.essentials import (
    date_translate,
    findDay,
    show_table,
    convert_to_datetime
)


# getting page configs
st.set_page_config(page_title="Print", page_icon="🖨️")

def read_from_csv(path):
    with open(path, mode='r') as file:
        reader = csv.reader(file)
        data = list(reader)
    return data

if __name__ == "__main__":
    # this will take the range of dates
    with st.sidebar:
        # we should probably save files according to sections and classes
        _class = st.selectbox("Class: ", ["I","II","III","IV","V","VI","VII","VIII","IX", "X"])
        section = st.selectbox("Section", ["Abyad"])
        st.markdown("<h2 align='center'> Range of Date </h2>", unsafe_allow_html=True)
        start = st.date_input("From: ", format="DD/MM/YYYY")
        end = st.date_input("To: ", format="DD/MM/YYYY")
        # select header sizes
        size = st.slider("Select header size:",min_value=12, value=18, max_value=24)
        live = st.checkbox("Edit :red[Live!]")
        year, month, start_day = date_translate(str(start))
        year, month, end_day = date_translate(str(end))
        path = f"app/data/{year}/{month}/"
        files = os.listdir(path)
        filtered_files = [file for file in files if int(start_day) <= int(file.replace(".csv","")) <= int(end_day)]
        
        generate = st.button("Generate 🗒️", use_container_width=True, type="primary")
        
    if generate or live:
        # main body starts
        with st.container():
            # logo
            st.markdown("""<center><img height=40 width=40 style='border-radius: 50px' src="https://shorturl.at/imMSW" </center>""", unsafe_allow_html=True)

            # Title
            st.markdown(f"<h2 align='center' style='font-size:{size}px;'> Al-Burooj International School </h2>", unsafe_allow_html=True)

            # class and section
            st.markdown(f"<center>Class: {_class} ({section}) </center>",unsafe_allow_html=True)

            # date range
            st.markdown(f"<center>(From {start}, {findDay(str(start))} to {end}, {findDay(str(end))})</center>",unsafe_allow_html=True)

            # reading the files in a loop
            for file in filtered_files:
                st.spinner("Loading...")
                st.write("""<br>""",unsafe_allow_html=True)
                date = convert_to_datetime(f"{year}-{month}-{file.replace('.csv','')}")
                data = read_from_csv(path+file)
                show_table(data, date)
    
    

    