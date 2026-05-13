import streamlit as st

st.set_page_config(page_title="Diebold Nixdorf × Snowflake | ATM AI Assist", page_icon="❄️", layout="wide")

pages = {
    "Deliverables": [
        st.Page("pilot_evaluation.py", title="Pilot Evaluation Plan", icon="🎯"),
        st.Page("executive_brief.py", title="Executive Brief", icon="📋"),
        st.Page("business_value.py", title="Business Value Analysis", icon="💰"),
        st.Page("architecture.py", title="Future State Architecture", icon="🏗️"),
        st.Page("personal_video.py", title="Stakeholder Briefing", icon="🎬"),
        st.Page("interactive_demo.py", title="Interactive Demo", icon="🚀"),
    ]
}

pg = st.navigation(pages)
pg.run()
