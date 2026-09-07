import streamlit as st

import pandas as pd
from datetime import datetime
from src.agent import WaterIntakeAgent
from src.database import log_intake, get_intake_history

if "tracker_started" not in st.session_state:
    st.session_state.tracker_started = False

### welcome sessio

if not st.session_state.tracker_started:
    st.title("Welcome to AI water Tracker")
    st.markdown("""
    Track your daily hydration with help of AI assistant.
    log your intake, get smart feedback and stay healthy effirtlessly

    """)

    if st.button("Start Tracking"):
        st.session_state.tracker_started = True
        st.experimental_rerun()