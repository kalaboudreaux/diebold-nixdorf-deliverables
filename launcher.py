import streamlit as st

st.set_page_config(page_title="Diebold Nixdorf — Snowflake Deliverables", page_icon="❄️", layout="wide")

st.markdown("""
<style>
    .main-title {font-size: 2.5rem; font-weight: 700; color: #29B5E8; text-align: center;}
    .subtitle {font-size: 1.2rem; color: #a0a0a0; text-align: center; margin-bottom: 2rem;}
    .card {background: linear-gradient(135deg, #0d1b2e 0%, #1a2744 100%); padding: 2rem; border-radius: 16px; border: 1px solid #29B5E833; margin: 1rem 0; min-height: 200px;}
    .card-title {font-size: 1.4rem; font-weight: 700; color: #29B5E8;}
    .card-desc {color: #c0c0c0; margin-top: 0.5rem; line-height: 1.6;}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-title">❄️ Diebold Nixdorf × Snowflake</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">ATM AI Assist — Executive Deliverables for Bruce Diesel, Tanya Gill, and Michael Engel</p>', unsafe_allow_html=True)

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
        <div class="card-title">📋 1. Executive Education Brief</div>
        <div class="card-desc">
            High-level "Why Snowflake" for the ATM AI Assist use case. Includes Year 1/2/3 value roadmap, 
            Snowflake vs. Grafana differentiation, and what it enables that you can't do today.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("**Run:** `streamlit run executive_brief.py`")
    
    st.markdown("""
    <div class="card">
        <div class="card-title">🎬 3. Personal Stakeholder Briefing</div>
        <div class="card-desc">
            Personalized messaging for each stakeholder — curated to their specific role and answering 
            "What's in it for me?" for Bruce (Product), Tanya (Security), and Michael (R&D/Software).
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("**Run:** `streamlit run personal_video.py`")

with col2:
    st.markdown("""
    <div class="card">
        <div class="card-title">🏗️ 2. Future State Architecture</div>
        <div class="card-desc">
            Before/after architecture comparison with detailed change log. Shows what gets consolidated, 
            what's new, cost savings analysis, and ROI timeline. Clarifies Snowflake vs. Grafana roles.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("**Run:** `streamlit run architecture.py`")
    
    st.markdown("""
    <div class="card">
        <div class="card-title">🚀 4. Interactive Demo Experience</div>
        <div class="card-desc">
            Full interactive demo with real-time ATM monitoring, AI anomaly detection, natural language queries 
            (Cortex Analyst), predictive maintenance, and multi-tenant secure data sharing. The "wow" factor.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("**Run:** `streamlit run interactive_demo.py`")

st.markdown("---")
st.markdown("### Quick Start")
st.code("""
# Run any individual deliverable:
cd diebold_nixdorf_deliverables
streamlit run executive_brief.py --server.port 8501
streamlit run architecture.py --server.port 8502
streamlit run personal_video.py --server.port 8503
streamlit run interactive_demo.py --server.port 8504

# Or run this launcher:
streamlit run launcher.py
""", language="bash")

st.markdown("---")
st.markdown("### Stakeholders")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("**Bruce Diesel**\n\nDirector, Product Management\n\nBranch and Cash Automation")
with col2:
    st.markdown("**Tanya Gill**\n\nGlobal Director\n\nSecurity Architecture & Engineering")
with col3:
    st.markdown("**Michael Engel**\n\nVP Software\n\nManaged Services and R&D")

st.caption("Prepared by Snowflake Account Team | Working with Kirubel Legasion, Chief Architect | May 2026")
