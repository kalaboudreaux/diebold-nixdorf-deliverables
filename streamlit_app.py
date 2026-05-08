import streamlit as st

st.set_page_config(page_title="Diebold Nixdorf × Snowflake | ATM AI Assist", page_icon="❄️", layout="wide")

pages = {
    "Home": [st.Page("launcher.py", title="Overview", icon="🏠")],
    "Deliverables": [
        st.Page("executive_brief.py", title="Executive Brief", icon="📋"),
        st.Page("architecture.py", title="Architecture", icon="🏗️"),
        st.Page("personal_video.py", title="Stakeholder Briefing", icon="🎬"),
        st.Page("interactive_demo.py", title="Interactive Demo", icon="🚀"),
    ]
}

pg = st.navigation(pages)
pg.run()
