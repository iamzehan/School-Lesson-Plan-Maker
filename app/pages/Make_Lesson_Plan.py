import streamlit as st
from utils.essentials import (
    findDay,
    read_from_csv,
    write_to_csv,
    show_table
)

def main():
    with st.container(border=True):
        st.markdown("""<center><img height=100 width=100 style='border-radius: 50px' src="https://www.al-buroojbd.com/img/site/1650527711.png" </center>""", unsafe_allow_html=True)
        st.markdown("""<h2 align='center'> Lesson Plan maker </h2>""", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([4,4,4])
        date = col1.date_input("Pick a date: ", format="DD/MM/YYYY")
        _class = col2.selectbox("Class: ", options=["I","II","III","IV","V","VI","VII","VIII","IX", "X"] )
        section = col3.selectbox("Section: ", ["Abyad"])
        try:
            data = read_from_csv(str(date),_class,section)
        except:
            data = None
            st.error(f"No table created for {date}")
        col1, col2, col3 = st.columns([3,4,3])
        type_note = col2.radio("Plan Type: ", options=["Periodic", "Special"], horizontal=True)

        if type_note == "Periodic":
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
            write_to_csv(submission_data,str(date),_class, section)
            st.empty()
            data = read_from_csv(str(date),_class, section)
    if data:
        with st.expander("Preview"):
            st.markdown(show_table(data, date), unsafe_allow_html=True)
        


if __name__ == "__main__":
    st.set_page_config(page_title="Make LP", page_icon="✏️")
    main()