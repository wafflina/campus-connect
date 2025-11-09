import streamlit as st

import json
import os

# ---------- Sample club data ----------


# ---------- Mock recommendation function ----------
import streamlit as st
from home import home_page
from questionnaire import questionnaire_page
from events_page import events_page

if "page" not in st.session_state:
    st.session_state.page = "home"

if st.session_state.page == "home":
    home_page()
elif st.session_state.page == "questionnaire":
    questionnaire_page()
elif st.session_state.page == "events":
    events_page()


