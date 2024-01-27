import streamlit as st
from utils.essentials import (
    findDay,
    read_from_csv,
    write_to_csv,
    show_table
)

def main():
    with st.container(border=True):
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
            st.markdown(show_table(data, date), unsafe_allow_html=True)
        


if __name__ == "__main__":
    st.set_page_config(page_title="Make LP", page_icon="✏️")
    main()