import streamlit as st
def home_page():

    st.image("campusconnect_logo.png", use_container_width=True)
    st.write("CampusConnect helps students find clubs, events, and opportunities tailored to their interests and schedule. Get personalized recommendations and make the most of campus life!")
    
    if st.button("Get Started"):
        st.session_state.page = "questionnaire"
    if st.button("Login"):
        st.session_state.page = "login"