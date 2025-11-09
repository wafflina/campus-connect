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
            cal_url = ("https://calendar.google.com/calendar/render?action=TEMPLATE"
    f"&text={urllib.parse.quote(event['name'])}"
    f"&details={urllib.parse.quote(event['description'])}"
    f"&location={urllib.parse.quote(event['location'])}")

            if st.button("📅 Add to Calendar"):
                webbrowser.open_new_tab(cal_url)
