import streamlit as st
import json
from event_ranking import rank_events

def events_page():
    st.title("🎯 Your Personalized Campus Events")

    with open("events.json", "r") as f:
        events = json.load(f)

    ranked_events = rank_events(st.session_state.user_prefs, events)

    for idx, (event, score) in enumerate(ranked_events, start=1):
        with st.container(border=True):
            st.subheader(f"{idx}. {event['name']}")
            st.write(f"**Host:** {event['host']}  |  **Location:** {event['location']}")
            st.write(f"📅 {event['date']}  ⏰ {event['time']}")
            st.write(event["description"])
            st.caption(f"Tags: {', '.join(event['tags'])}")

            # Optional: Save & Add to Calendar
            st.button("❤️ Save", key=event["name"])
            for i, event in enumerate(events):
            st.subheader(event["name"])
            st.write(event["description"])

            event_url = (f"https://calendar.google.com/calendar/render?action=TEMPLATE"
        f"&text={event['name'].replace(' ', '+')}"
        f"&details={event['description'].replace(' ', '+')}"
        f"&location={event['location'].replace(' ', '+')}")

            if st.button(f"📅 Add to Calendar", key=i):
                webbrowser.open_new_tab(event_url)
