from datetime import datetime as dt
import streamlit as st
from utils.essentials import (
    date_translate,
    findDay,
    read_from_csv,
    write_to_csv
)

def add_rows(rows):
    my_table = f"""<tr align="center">
                        <th>Subject</th>
                        <th>Period</th>
                        <th>C.W.</th>
                        <th>H.W.</th>
                    </tr>
                    {rows}"""
    return my_table


        

def show_table(data,date):
    rows = []
    rowspan=0
    year, month, day = date_translate(str(date))
    date = f"""{day} - {month} - {year} <br> ({findDay(str(date))})"""
    for row in data:
        if len(row)>1:
            rows.append(f"""
                <tr align="center">
                    <td>{str(row[1])}</td>
                    <td>{str(row[2])}</td>
                    <td>{row[3]}</td>
                    <td>{row[4]}</td>
                </tr>
            """)
        if len(row)==1:
            rowspan+=1
            rows.append(f"""
                <tr align="center">
                    <td colspan=4>{"".join(row)}</td>
                </tr>
            """)
    rows = """""".join(rows)
    st.markdown(f"""
                <table align="center" style='width:100%!important;'>
                <tr align="center"><th style='background-color:aqua'>Date & Day</th><td colspan=3>{date}</td></tr>
                    {add_rows(rows)}
                </table>
                """, unsafe_allow_html=True)


def main():
    with st.container(border=True):
        st.markdown("""<div style='page-break-after: always'></div>""")
        st.markdown("""<center><img height=100 width=100 style='border-radius: 50px' src="https://shorturl.at/imMSW" </center>""", unsafe_allow_html=True)
        st.markdown("""<h2 align='center'> Lesson Plan maker </h2>""", unsafe_allow_html=True)
        col1, _ = st.columns([2,8])
        
        with col1:
            date = st.date_input("Pick a date: ", format="DD/MM/YYYY")
        try:
            data = read_from_csv(str(date))
        except:
            data = None
            st.error(f"No table created for {date}")
            
        type_note = st.selectbox("Type: ", options=["Regular", "Special"])

        if type_note == "Regular":
            col1, col2 = st.columns(2)
            with col1: 
                subject = st.text_area("Subject:")
            with col2:
                period = st.text_area("Period: ")
            col1, col2 = st.columns(2)
            with col1:
                classwork = st.text_area("Classwork:")
            with col2:
                homework = st.text_area("Homework:")
            submission_data = [str(date)+"<br>"+findDay(str(date)), subject.replace("\n","<br>"), period.replace("\n", "<br>"), classwork.replace("\n","<br>"), homework.replace("\n","<br>")]
            
        elif type_note == "Special":
            note = st.text_area("Note: ")
            submission_data = [note]
            
        submit = st.button("Add", use_container_width=True,type="primary")
        if submit:
            write_to_csv(submission_data,str(date))
            st.empty()
            data = read_from_csv(str(date))
    if data:
        with st.expander("Preview"):
            show_table(data, date)
        


if __name__ == "__main__":
    st.set_page_config(page_title="Make LP", page_icon="✏️")
    main()