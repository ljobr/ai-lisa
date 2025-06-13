
import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo
import calendar
import json
import os

st.set_page_config(page_title="L.I.S.A. - Live Intelligent Support Agent", layout="wide")

# ---- HEADER IMAGE + TIME ----
st.image("AI Lisa.png", use_container_width=True)

current_time = datetime.now(ZoneInfo("America/New_York")).strftime("%A, %B %d, %Y — %I:%M %p")
st.markdown(f"<div style='text-align:center;font-size:18px;padding:10px 0;'>🕒 Today is: <b>{current_time}</b></div>", unsafe_allow_html=True)

# ---- TABS ----
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs([
    "📅 Dashboard", "🩺 Health & Wellness", "💳 Credit & Finance",
    "📚 Study & School", "👑 Ministry & Prayer", "💼 Projects & Business",
    "🌸 Family & Self-Care", "📆 Calendar & Scheduling"
])

# ---- TAB 1: Dashboard ----
with tab1:
    st.subheader("📅 Today’s Agenda")
    st.text_input("Appointments:")
    st.text_input("Medication Reminders:")
    st.text_input("Top Tasks:")
    st.text_area("Lisa, don’t forget…")

# ---- TAB 2: Health & Wellness ----
with tab2:
    st.subheader("💊 Medical & Wellness Center")
    st.text_input("Upcoming Appointments:")
    st.text_input("Current Medications / Dosages:")
    st.text_input("Refill Needed:")
    st.text_input("Symptom Notes (e.g., migraines, aches):")

    st.subheader("🩺 Vitals Tracker")
    st.number_input("Blood Pressure (Systolic):", 80, 250)
    st.number_input("Blood Pressure (Diastolic):", 40, 150)
    st.number_input("Current Weight (lbs):", 50, 700)

# ---- TAB 3: Credit & Finance ----
with tab3:
    st.subheader("💳 Credit & Card Tracker")
    st.text_input("Credit Card Name:")
    credit_limit = st.number_input("Credit Limit ($):", 0)
    balance = st.number_input("Current Balance ($):", 0)
    if credit_limit > 0:
        utilization = (balance / credit_limit) * 100
        target = credit_limit * 0.30
        st.markdown(f"**Utilization:** {utilization:.2f}%")
        st.markdown(f"**Pay at least ${balance - target:.2f} to reach 30%**")

    st.subheader("📅 Bills & Budget")
    st.text_area("Monthly Bills:")
    st.text_area("Upcoming Payments:")

# ---- TAB 4: Study & School ----
with tab4:
    st.subheader("📚 Theology School Schedule")
    st.markdown("**Classes:** Monday & Wednesday at 7:00 PM")
    st.text_input("Upcoming Assignments:")

    st.subheader("✍️ Writing Time")
    st.text_input("Book Writing Focus Today:")

    st.subheader("📖 Study Notes")
    st.text_area("Bible or Class Study Notes:")

# ---- TAB 5: Ministry & Prayer ----
with tab5:
    st.subheader("📖 Bible Study & Reflection")
    st.text_input("Planned Scripture/Study Topic:")
    st.text_area("Reflection Notes / Insights:")

    st.subheader("👑 Kingdom Women Who Pray")
    st.text_input("Content Planning for This Week:")
    st.text_area("Group Engagement / Post Ideas:")

# ---- TAB 6: Projects & Business ----
with tab6:
    st.subheader("🛠️ Project Work Timer")
    hours = st.slider("Hours scheduled this week:", 0, 60, 0)
    if hours >= 20:
        st.warning("⚠️ You're nearing burnout range. Reassess your schedule.")

    st.subheader("💼 Entrepreneur Time Block")
    st.text_input("Business Work Block Today:")

# ---- TAB 7: Family & Self-Care ----
with tab7:
    st.subheader("🌸 Self-Care Activities")
    st.text_input("Facial / Nails / Hair / Eyebrows:")

    st.subheader("👶 Grandchildren Time")
    st.text_input("Time Planned with Grandbabies:")

    st.subheader("🔔 Sabbath Check")
    today = datetime.today().weekday()
    if today == 6:
        st.error("🚫 It's Sunday. L.I.S.A. will not allow business tasks today.")
    else:
        st.success("✅ You are clear to schedule business work today.")

# ---- TAB 8: Calendar & Scheduling ----
with tab8:
    st.subheader("📆 View Your Calendar")
    events_file = "lisa_calendar_events.json"

    if os.path.exists(events_file):
        with open(events_file, "r") as f:
            try:
                events = json.load(f)
                for event in events.get("events", []):
                    st.markdown(f"**{event.get('date', 'Unknown Date')} — {event.get('title', 'No Title')}**")
                    st.write(event.get('description', 'No description available.'))
            except json.JSONDecodeError:
                st.error("Calendar file found, but could not be read.")
    else:
        st.info("No events found. Please upload your calendar JSON file named 'lisa_calendar_events.json' to this directory.")

    st.caption("This calendar will expand with editing features soon!")
