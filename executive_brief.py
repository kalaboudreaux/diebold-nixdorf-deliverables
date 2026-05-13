import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from notes_utils import render_section_notes

st.set_page_config(page_title="Executive Brief | Diebold Nixdorf × Snowflake", page_icon="❄️", layout="wide")

BRAND_CSS = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    .stApp {font-family: 'Inter', sans-serif;}
    .dn-header {background: linear-gradient(135deg, #003366 0%, #004d99 50%, #29B5E8 100%); padding: 3rem 2rem; border-radius: 0 0 20px 20px; margin: -1rem -1rem 2rem -1rem; text-align: center;}
    .dn-title {font-size: 2.8rem; font-weight: 800; color: white; margin: 0; letter-spacing: -0.5px;}
    .dn-subtitle {font-size: 1.1rem; color: #b3d9ff; margin-top: 0.5rem; font-weight: 300;}
    .exec-summary {background: linear-gradient(135deg, #f8fbff 0%, #e8f4fd 100%); padding: 2.5rem; border-radius: 16px; border: 1px solid #29B5E820; margin: 1.5rem 0;}
    .exec-summary h3 {color: #003366; margin-top: 0;}
    .exec-summary p {color: #1a1a2e; font-size: 1.05rem; line-height: 1.8;}
    .value-metric {background: white; padding: 1.5rem; border-radius: 12px; text-align: center; box-shadow: 0 2px 12px rgba(0,0,0,0.06); border-top: 3px solid #29B5E8;}
    .value-metric h2 {color: #29B5E8; margin: 0; font-size: 2rem;}
    .value-metric p {color: #666; margin: 0.3rem 0 0 0; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.5px;}
    .section-divider {height: 3px; background: linear-gradient(90deg, #003366, #29B5E8, #003366); margin: 2.5rem 0; border-radius: 2px; opacity: 0.3;}
    .insight-card {background: white; padding: 1.5rem; border-radius: 12px; border-left: 4px solid #29B5E8; box-shadow: 0 2px 8px rgba(0,0,0,0.04); margin: 0.8rem 0;}
    .engagement-ref {background: #f0f7ff; padding: 1rem 1.5rem; border-radius: 8px; border-left: 3px solid #003366; margin: 0.5rem 0; font-size: 0.9rem; color: #003366;}
    .compare-table th {background: #003366 !important; color: white !important;}
    .year-section {background: white; padding: 2rem; border-radius: 16px; box-shadow: 0 2px 12px rgba(0,0,0,0.05); margin: 1rem 0; border-top: 4px solid #29B5E8;}
    .pillar-icon {font-size: 2.5rem; margin-bottom: 0.5rem;}
    .footer-bar {background: #003366; padding: 1.5rem; border-radius: 12px; text-align: center; color: white; margin-top: 2rem;}
</style>
"""
st.markdown(BRAND_CSS, unsafe_allow_html=True)

st.markdown("""
<div class="dn-header">
    <div class="dn-title">Why Snowflake for ATM AI Assist</div>
    <div class="dn-subtitle">Executive Education Brief — Prepared for Diebold Nixdorf Leadership<br>Bruce Diesel · Tanya Gill · Michael Engel</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="exec-summary">
<h3>📌 Executive Summary</h3>
<p>
<strong>Diebold Nixdorf's Transaction Assist product</strong> — which enables banking customers to connect with remote tellers via ATM — generates rich call data through Zoom, Twilio, and Kafka streams. Today, this data is delivered to banking clients as basic CSV reports and Power BI dashboards. <strong>There is no AI, no real-time analytics, and no competitive differentiation.</strong>
</p>
<p>
<strong>Snowflake transforms Transaction Assist into an AI-powered analytics platform</strong> — enabling real-time sentiment analysis on call transcripts, intelligent call classification, cross-customer benchmarking, and natural language querying. This is a <strong>product differentiator that generates new revenue</strong> for Diebold Nixdorf and creates a competitive moat vs. NCR Atleos and Hyosung.
</p>
<p>
<strong>The pilot is fully scoped and funded.</strong> Kirubel Legasion (Chief Architect) has evaluated the technology over 9 months of engagement with Snowflake. $10K in evaluation credits are approved, a no-cost Professional Services workshop is ready, and 3–5 banking clients are identified for the 8-week pilot. <strong>The only remaining step is leadership alignment to proceed.</strong>
</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown('<div class="value-metric"><h2>$0</h2><p>Pilot Cost to DN</p></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="value-metric"><h2>8 Weeks</h2><p>Time to First AI Insight</p></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="value-metric"><h2>20+</h2><p>Use Cases Identified</p></div>', unsafe_allow_html=True)
with col4:
    st.markdown('<div class="value-metric"><h2>20+</h2><p>Use Cases Identified</p></div>', unsafe_allow_html=True)

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

st.markdown("## 🎯 Addressing Your Key Concerns")

tab2, tab1 = st.tabs(["**Why This Should Be a Priority NOW**", "**Snowflake vs. Grafana (Reference)**"])

with tab1:
    st.markdown("""
    ### Different Tools for Different Jobs
    
    A common question from stakeholders: *"How is Snowflake different from Grafana?"*
    
    **The short answer:** Grafana is a dashboard for infrastructure monitoring. Snowflake is a data platform with built-in AI. They serve completely different purposes.
    """)
    
    comparison_data = {
        "Dimension": [
            "What it is",
            "Primary Question it Answers",
            "Data Storage",
            "AI / Machine Learning",
            "Multi-Tenant Data Sharing",
            "Natural Language Queries",
            "Security & Governance",
            "Recommendation"
        ],
        "Grafana": [
            "Observability dashboard tool",
            '"Is the ATM system healthy right now?"',
            "None — relies on Prometheus/Loki",
            "None",
            "Not supported",
            "Not supported",
            "Basic — no data governance",
            "KEEP for ops monitoring"
        ],
        "Snowflake": [
            "Data Cloud Platform + AI Engine",
            '"Why did that call fail? What will happen next? How do we serve banking clients better?"',
            "Unlimited, scalable cloud storage",
            "Cortex AI — 16 LLMs, ML functions, NLP built-in",
            "Native — serve 50+ banking clients from one platform",
            "Cortex Analyst — ask questions in English",
            "Enterprise-grade: row-level security, masking, PCI/SOC2/HIPAA",
            "ADD as the data + AI platform"
        ]
    }
    
    st.dataframe(pd.DataFrame(comparison_data), use_container_width=True, hide_index=True)
    
    st.markdown("""
    <div class="engagement-ref">
    📎 <strong>From our engagement:</strong> Kirubel's architecture (which you've seen) shows Grafana receiving webhook alerts from Prometheus/oTel. 
    Snowflake sits underneath as the intelligence layer — processing Kafka streams, running Cortex AI, and delivering multi-tenant analytics to banking clients. 
    They are complementary, not competitive.
    </div>
    """, unsafe_allow_html=True)

with tab2:
    st.markdown("### Snowflake Reduces Competing Priorities — It Doesn't Add One")
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("""
        #### ❌ Today's Priority Tax
        - Managing Oracle DB + SERAS Warehouse + Shared File Locations
        - Building manual CSV reports for each banking client
        - No AI capabilities → can't differentiate vs. NCR Atleos
        - Each new client requires custom reporting setup
        - IBM WatsonX & Microsoft Fabric approaching your teams
        """)
    with col_b:
        st.markdown("""
        #### ✅ With Snowflake (Priorities Consolidated)
        - **One platform** for all ATM call data (real-time streaming)
        - **Auto-generated** multi-tenant client dashboards
        - **Built-in AI** → immediate competitive differentiation
        - **New clients onboard in hours**, not weeks
        - **You own the AI stack** → not dependent on IBM
        """)
    
    st.markdown("""
    <div class="engagement-ref">
    📎 <strong>From our engagement:</strong> In our April planning sessions with Kirubel, we identified that DN currently delivers only basic CSV + Power BI reports 
    to banking clients for Transaction Assist. Meanwhile, NCR Atleos is investing in analytics. Snowflake enables DN to leapfrog with AI-powered insights 
    that no competitor offers today — turning a cost center into a revenue generator.
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
st.markdown("## 📈 Value Roadmap: Year 1, 2, 3")

year_tab1, year_tab2, year_tab3 = st.tabs(["**Year 1 — Foundation**", "**Year 2 — Scale**", "**Year 3 — Leadership**"])

with year_tab1:
    st.markdown("""
    <div class="year-section">
    <h3>Year 1: Build the Foundation</h3>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        | Use Case | What It Delivers | Champion |
        |----------|-----------------|----------|
        | **Transaction Assist — Full Deployment** | AI sentiment analysis, call classification, NL queries, multi-tenant benchmarking for 10–20 banking clients | Kirubel → Michael Engel |
        | **Supply Chain Demand Planning** | Unify 40K–50K SKUs across 80 countries, ML forecasting | Aamir Reyaz, Sangeeta Doni |
        | **Finance Data Consolidation** | Replace Alteryx workarounds, consolidate 80-country ERP data | Tyler Wise |
        """)
    with col2:
        st.metric("Banking Clients on Platform", "10–20", "Up from 3–5 pilot")
        st.metric("Forecast Accuracy", "+30–50%", "ML vs. manual")
        st.metric("Analyst Hours Saved", "100–200/mo", "Eliminated manual ETL")

with year_tab2:
    st.markdown("""
    <div class="year-section">
    <h3>Year 2: Scale Intelligence</h3>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        | Use Case | What It Delivers | Champion |
        |----------|-----------------|----------|
        | **AI-Powered RFP Tool** | Fine-tuned LLM on RFP history, auto-generation in multiple languages | John Apgar, Sachin Handoo |
        | **ATM Cash Management** | Predict cash demand, prevent cash-outs, optimize Brinks/Loomis scheduling | Marco (Berlin) |
        | **Language Translation** | Real-time ATM UI translation, document localization | John Apgar, Pradeep |
        | **Microsoft Fabric Displacement** | Migrate Azure analytics PoC to Snowflake (superior for AI) | David Champagne |
        """)
    with col2:
        st.metric("RFP Win Rate", "+10–20%", "AI-generated responses")
        st.metric("Cash Float Savings", "5–10%", "Across ATM network")
        st.metric("Translation Savings", "$200K–$500K", "Eliminate outsourcing")

with year_tab3:
    st.markdown("""
    <div class="year-section">
    <h3>Year 3: Market Leadership</h3>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        | Use Case | What It Delivers | Champion |
        |----------|-----------------|----------|
        | **Security & Tamper Detection** | AI camera analytics, skimming detection, loitering alerts | John Apgar, Security Team |
        | **Accessibility (ASL Avatars)** | Sign language AI for ATM kiosks — first in industry | Product Team |
        | **Predictive Maintenance (IoT)** | Sensor data ML → predict failures, auto-create ServiceNow tickets | IT/Operations |
        | **Enterprise Data Platform** | Full Snowflake deployment across Finance, IT, HR | Tyler Wise, Alam Mulla |
        | **Data Monetization** | Sell anonymized ATM intelligence as a product to banking clients | Michael Engel, CRO Joe |
        """)
    with col2:
        st.metric("Fraud Prevention", "7-figure", "Per banking client")
        st.metric("ATM Downtime", "-30–50%", "Predictive maintenance")
        st.metric("New Revenue Streams", "3+", "Data products")

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

fig_value = go.Figure()
phases = ["Pilot<br>(Now)", "Year 1<br>(FY27)", "Year 2<br>(FY28)", "Year 3<br>(FY29)"]
use_cases = [1, 3, 8, 20]
banking_clients = [5, 20, 35, 50]

fig_value.add_trace(go.Bar(name="Use Cases Deployed", x=phases, y=use_cases, marker_color="#003366"))
fig_value.add_trace(go.Bar(name="Banking Clients on Platform", x=phases, y=banking_clients, marker_color="#29B5E8"))
fig_value.update_layout(title="Platform Growth Trajectory", barmode="group", template="plotly_white", height=350, yaxis_title="Count", font=dict(family="Inter"))
st.plotly_chart(fig_value, use_container_width=True)

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

st.markdown("## 🚀 What Snowflake Enables for Transaction Assist")

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
    <div class="insight-card">
    <div class="pillar-icon">🧠</div>
    <h4>AI on Every Call</h4>
    <ul>
    <li>Sentiment analysis on call transcripts</li>
    <li>Intelligent call classification & tagging</li>
    <li>Anomaly detection (fraud patterns)</li>
    <li>Call quality scoring</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="insight-card">
    <div class="pillar-icon">📊</div>
    <h4>Analytics as a Product</h4>
    <ul>
    <li>Multi-tenant dashboards per banking client</li>
    <li>Cross-customer benchmarking (anonymized)</li>
    <li>Natural language queries for bank execs</li>
    <li>Premium tier pricing → new revenue</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="insight-card">
    <div class="pillar-icon">⚡</div>
    <h4>Real-Time Intelligence</h4>
    <ul>
    <li>Sub-second Kafka ingestion via connector</li>
    <li>Live staffing optimization by volume</li>
    <li>Real-time alerting on call anomalies</li>
    <li>Dynamic Tables → always-fresh data</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

st.markdown("## 👥 What This Means for Your Team")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
    <div class="insight-card">
    <h4>Director, Product Management</h4>
    <em>Branch and Cash Automation</em>
    <hr>
    <ul>
    <li>AI becomes a <strong>product feature</strong> that banking clients pay for</li>
    <li>Competitive differentiation vs. NCR Atleos</li>
    <li>Ship analytics features 10x faster</li>
    <li>New revenue stream from premium tier</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="insight-card">
    <h4>Global Director, Security Architecture</h4>
    <em>Security Architecture and Engineering</em>
    <hr>
    <ul>
    <li><strong>Unified security posture</strong> — one platform to secure</li>
    <li>PCI-DSS, SOC2, HIPAA, FedRAMP compliant</li>
    <li>Row-level security for banking client isolation</li>
    <li>Eliminate CSV file transfer risks</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown("""
    <div class="insight-card">
    <h4>VP Software, Managed Services & R&D</h4>
    <em>Software, Managed Services and R&D</em>
    <hr>
    <ul>
    <li><strong>AI without an AI team</strong> — Cortex AI is a function call</li>
    <li>Reduce tech debt — consolidate 5+ data systems</li>
    <li>Engineering team is already aligned and ready</li>
    <li>8-week pilot, zero risk, funded by Snowflake</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)



render_section_notes("exec_brief_summary", "Executive Summary")
render_section_notes("exec_brief_grafana", "Snowflake vs Grafana")
render_section_notes("exec_brief_roadmap", "Value Roadmap (Year 1/2/3)")
render_section_notes("exec_brief_stakeholders", "Stakeholder Impact")
render_section_notes("exec_brief_general", "General Notes — Executive Brief")
