import streamlit as st

def questionnaire_page():
    st.title("🌟 Find your people. Join your passions. 🌟")

    name = st.text_input("What's your name?", key = "name_input")

    interests = st.multiselect(
        "Which of these categories interest you?",
        ["Arts & Culture", "Technology & STEM", "Sports & Fitness", "Volunteering & Service",
         "Music & Performing Arts", "Sustainability & Environment", "Academics & Study Groups",
         "Career & Professional Development", "Faith & Community", "Social & Hangout Events"], key="interests_input"
    )

    event_types = st.multiselect(
        "Which types of events do you enjoy the most?",
        ["Workshops", "Guest lectures", "Networking", "Casual socials", "Performances"], key="event_input"
    )

    availability = st.multiselect(
        "When are you usually free to attend events?",
        ["Morning", "Afternoon", "Evening", "Weekends"], key = "availability_input"
    )

    planning = st.selectbox(
        "How far in advance do you like to plan your week?",
        ["1 day before", "A few days before", "A week in advance"], key = "planning_input"
    )

    mode = st.radio("Do you prefer in-person or virtual events?", ["In-person", "Virtual", "Either"], key = "mode_input")
    crowd = st.radio("How big of a crowd do you prefer?", ["Small groups", "Medium", "Large gatherings", "Any"], key = "crowd_input")
    year = st.selectbox("What's your year?", ["Freshman", "Sophomore", "Junior", "Senior"], key = "year_input")

    if st.button("Show My Events"):
        st.session_state.user_prefs = {
            "name": name,
            "interests": interests,
            "event_types": event_types,
            "availability": availability,
            "planning": planning,
            "mode": mode,
            "crowd": crowd,
            "year": year
        }
        st.session_state.page = "events"
