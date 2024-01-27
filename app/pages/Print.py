import os
import csv
import streamlit as st
from streamlit.components.v1 import html
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

def render_all_tables(filtered_files):
    # reading the files in a loop
    tables = []
    for file in filtered_files:
        st.spinner("Loading...")
        st.write("""<br>""",unsafe_allow_html=True)
        date = convert_to_datetime(f"{year}-{month}-{file.replace('.csv','')}")
        data = read_from_csv(path+file)
        tables.append(f"""{show_table(data, date)}
                    """)
    return ("""<br>""".join(tables))

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
        generate = st.button("Generate 🗒️", use_container_width=True, type="primary")
    
    year, month, start_day = date_translate(str(start))
    year, month, end_day = date_translate(str(end))
    path = f"app/data/{year}/{month}/Class - {_class}/Section - {section}/"
    try:
        files = os.listdir(path)
        filtered_files = [file for file in files if int(start_day) <= int(file.replace(".csv","")) <= int(end_day)]
        table = f"""<div id = 'print', style='background-color:white!important'><center><img height=40 width=40 style='border-radius: 50px' src="https://www.al-buroojbd.com/img/site/1650527711.png"></center>
                    <h2 align='center' style='font-size:{size}px;'> Al-Burooj International School </h2>
                    <center>Class: {_class} ({section}) </center>
                    <center>(From {start}, {findDay(str(start))} to {end}, {findDay(str(end))})</center>
                    {render_all_tables(filtered_files)}</div>"""
        if generate or live:
            # main body starts
            with st.container():
                # logo
                st.markdown("""<span style='page-break-after: always'></span>""", unsafe_allow_html=True)
                
                st.markdown(table, unsafe_allow_html=True)
    except:
        st.error(f"No data found for {start} - {end}, Class - {_class}, Section - {section}")
        
        
    
        
    
    
    
    

            

            
    
    

    