import streamlit as st

# --- GENERAL SETTINGS ---
NAME = "Anna Bednaříková"
EMAIL = "ANNABEDNARI@GMAIL.COM"
PHONE = "+420 724 128 266"

st.set_page_config(page_title="Anna Bednaříková's CV", page_icon=":sunglasses:")

# -- TADY SE UDELA SIDE MENU
with st.sidebar:
    my_radio = st.radio("Navigation", {
        "Profile": "Profile",
        "Experience": "Experience",
        "Skills": "Skills",
        "Education": "Education",
        "Languages": "Languages",
        "Interests": "Interests"
    })

# --- TADY DVA SLOUPECKY NAHORE NA STRANCE
col1, col2 = st.columns(2, gap="small")

with col1:
    st.title(NAME)
    st.write(f"Email: {EMAIL}")
    st.write(f"Phone: {PHONE}")

with col2:
    st.image("https://via.placeholder.com/150", caption="Profile Image")

# --- A TADY SE MENI, CO JE POD NIMA, PODLE VYBRANEHO BUTTONKU V SIDE MENU
if my_radio == "Profile":
    st.subheader("Profile")
    st.write("""
    I am connecting the world of languages and IT. Having worked as an
    in-house translator, I am now ready to start a new stage of my career
    working in data. I am currently enrolled in the Digital Academy: Data,
    a  4-month  course  organised  by  Czechitas  where  I’ve  learned  to
    process data using SQL and Python and visualise and interpret data in
    Tableau. I’ve also become familiar with data modelling. The course will
    be completed with a pair-work project, analysing lyrics and features of
    Grammy nominees and winners.
    """)

if my_radio == "Experience":
    st.subheader("Work Experience")
    st.write("""
    **Czech National Bank (2005–2023)**
    - In-house translator
    - Translations and proofreading of CNB publications and website into English
    - Translations for the CNB Visitor Centre
    - Translations and proofreading for the European Central Bank
    - Communication with translation agencies
    
    **Ministry of the Interior of the Czech Republic (2002–2005)**
    - In-house translator and interpreter
    - Translations for the Czech Ministry of the Interior and the Czech Police into/from English
    - Consecutive and simultaneous interpreting at meetings, press conferences, trainings, and conferences
    - Communication with freelance translators and interpreters
    
    **Gymnázium Jiřího z Poděbrad, Poděbrady (2000–2002)**
    - Secondary school English teacher
    """)

if my_radio == "Skills":
    st.subheader("Skills")
    st.write("""
    - Basics of Python, SQL
    - Tableau, Power BI
    - Word, Outlook
    - SDL Studio/Trados
    """)

if my_radio == "Education":
    st.subheader("Education")
    st.write("""
    **Masaryk University in Brno, Faculty of Arts (1994–2000)**
    - Master’s degree in English language and literature
    - Master’s degree in German language and literature
    
    **Courses**
    - 2024: Digital Academy: Data (Czechitas course spanning 300 hours, to be completed in June 2024)
    - 2024: Basics of Data Analysis (Czechitas, 36 hours)
    - 2024: Programming in Python (Czechitas, 25 hours)
    - 2024: Python for Data Analysis (Czechitas, 15 hours)
    - 2004: Legal English course for interpreters and translators (Law School, Charles University, Prague)
    - 1999: Teacher training (Masaryk University in Brno)
    """)

if my_radio == "Languages":
    st.subheader("Languages")
    st.write("""
    - Czech: Native speaker
    - English: Professional
    - German: Advanced
    - Dutch: False beginner
    - Japanese: False beginner
    """)

if my_radio == "Interests":
    st.subheader("Interests")
    st.write("""
    - Chasing U2 all around the globe
    - Traditional couture techniques
    """)