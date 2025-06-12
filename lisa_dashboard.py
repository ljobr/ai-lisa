import streamlit as st
from datetime import datetime
import calendar

st.set_page_config(page_title="L.I.S.A. - Live Intelligent Support Agent", layout="wide")

# ---- HEADER ----
st.title("👩🏽‍💻 L.I.S.A. - Live Intelligent Support Agent")
st.caption("Your personal life. Handled with grace, structure, and care.")

# ---- TODAY'S AGENDA ----
st.subheader("📅 Today’s Agenda")
st.text_input("Appointments:")
st.text_input("Medication Reminders:")
st.text_input("Top Tasks:")
st.text_area("Lisa, don’t forget…")

# ---- MEDICAL & WELLNESS ----
st.subheader("💊 Medical & Wellness Center")
st.text_input("Upcoming Appointments:")
st.text_input("Current Medications / Dosages:")
st.text_input("Refill Needed:")
st.text_input("Symptom Notes (e.g., migraines, aches):")

# ---- VITALS ----
st.subheader("🩺 Vitals Tracker")
st.number_input("Blood Pressure (Systolic):", 80, 250)
st.number_input("Blood Pressure (Diastolic):", 40, 150)
st.number_input("Current Weight (lbs):", 50, 700)

# ---- SPIRITUAL LIFE ----
st.subheader("📖 Bible Study & Reflection")
st.text_input("Planned Scripture/Study Topic:")
st.text_area("Reflection Notes / Insights:")

# ---- MINISTRY (KWWP) ----
st.subheader("👑 Kingdom Women Who Pray - Planning")
st.text_input("Content Planning for This Week:")
st.text_area("Group Engagement / Post Ideas:")

# ---- CREDIT TRACKER ----
st.subheader("💳 Credit & Card Tracker")
st.text_input("Credit Card Name:")
credit_limit = st.number_input("Credit Limit ($):", 0)
balance = st.number_input("Current Balance ($):", 0)
if credit_limit > 0:
    utilization = (balance / credit_limit) * 100
    target = credit_limit * 0.30
    st.markdown(f"**Utilization:** {utilization:.2f}%")
    st.markdown(f"**Pay at least ${balance - target:.2f} to reach 30%**")

# ---- GROCERY + COUPONS ----
st.subheader("🛒 Grocery List & Coupons")
st.text_area("Grocery List (Store by Store):")
st.text_area("Coupons to Use:")

# ---- PROJECT WORK ----
st.subheader("🛠️ Project Work Timer")
hours = st.slider("Hours scheduled this week:", 0, 60, 0)
if hours >= 20:
    st.warning("⚠️ You're nearing burnout range. Reassess your schedule.")

# ---- WRITING & ENTREPRENEURSHIP ----
st.subheader("✍🏽 Writing & Entrepreneurial Time")
st.text_input("Today's Writing Focus:")
st.text_input("Business Work Block Today:")

# ---- PERSONAL TIME ----
st.subheader("🌸 Personal & Family Time")
st.text_input("Self-Care Activity (e.g., manicure, facial):")
st.text_input("Grandchildren Time Planned:")

# ---- SABBATH BLOCK ----
st.subheader("🕊️ Sabbath Check")
today = datetime.today().weekday()
if today == 6:  # Sunday
    st.error("🚫 It's Sunday. L.I.S.A. will not allow business tasks today.")
else:
    st.success("✅ You are clear to schedule business work today.")
