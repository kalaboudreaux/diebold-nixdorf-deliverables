import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="Snowflake for ATM AI Assist | Diebold Nixdorf", page_icon="❄️", layout="wide")

st.markdown("""
<style>
    .main-header {font-size: 2.8rem; font-weight: 700; color: #29B5E8; margin-bottom: 0;}
    .sub-header {font-size: 1.3rem; color: #6e7681; margin-top: 0;}
    .value-card {background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%); padding: 2rem; border-radius: 12px; border-left: 4px solid #29B5E8; margin: 1rem 0;}
    .metric-big {font-size: 2.5rem; font-weight: 700; color: #29B5E8;}
    .metric-label {font-size: 0.9rem; color: #a0a0a0; text-transform: uppercase;}
    .differentiator-box {background: #0d1b2a; padding: 1.5rem; border-radius: 10px; border: 1px solid #29B5E8;}
    .year-badge {display: inline-block; background: #29B5E8; color: white; padding: 4px 12px; border-radius: 20px; font-weight: 600; font-size: 0.85rem;}
    .objection-answer {background: #1a2332; padding: 1.5rem; border-radius: 10px; border-left: 3px solid #4CAF50; margin: 0.5rem 0;}
    .snowflake-blue {color: #29B5E8;}
    .highlight-green {color: #4CAF50;}
    div[data-testid="stExpander"] {border: 1px solid #29B5E8; border-radius: 10px;}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-header">Why Snowflake for ATM AI Assist</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Executive Education Brief — Prepared for Diebold Nixdorf Leadership</p>', unsafe_allow_html=True)
st.markdown("---")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Data Sources Consolidated", "5+ → 1", "Unified Platform")
with col2:
    st.metric("Insight Latency", "Hours → Seconds", "Real-time AI")
with col3:
    st.metric("Year 3 ACV Potential", "$1.5M–$2.5M+", "Platform Growth")
with col4:
    st.metric("Tool Reduction", "60–70%", "Cost Savings")

st.markdown("---")

st.markdown("## 🎯 Addressing Your Key Questions")

tab1, tab2 = st.tabs(["**Snowflake ≠ Grafana — Here's the Difference**", "**Why This Should Be a Priority NOW**"])

with tab1:
    st.markdown("""
    ### The Core Distinction
    
    **Grafana** is an **observability visualization tool** — it displays metrics and logs from systems like Prometheus and Loki. 
    It answers: *"Is the system up? What's the error rate?"*
    
    **Snowflake** is a **data cloud platform with built-in AI** — it unifies all your data, enables AI/ML, and powers business decisions. 
    It answers: *"Why did that ATM fail? What will happen next? How do we serve customers better?"*
    """)
    
    comparison_data = {
        "Capability": [
            "Primary Purpose",
            "Data Storage",
            "AI/ML Built-in",
            "Multi-Tenant Data Sharing",
            "Historical Analytics",
            "Natural Language Queries",
            "Real-time + Batch Processing",
            "Governance & Compliance",
            "Cost at Scale",
            "Custom App Development"
        ],
        "Grafana": [
            "Dashboard visualization for ops metrics",
            "❌ No — relies on Prometheus/Loki",
            "❌ No",
            "❌ No",
            "Limited (retention issues)",
            "❌ No",
            "Metrics only (no business data)",
            "❌ No built-in governance",
            "Expensive at scale (Loki/Prometheus)",
            "❌ No"
        ],
        "Snowflake": [
            "Unified data platform + AI engine",
            "✅ Unlimited, scalable cloud storage",
            "✅ Cortex AI (LLMs, ML, NLP built-in)",
            "✅ Secure data sharing across tenants",
            "✅ Unlimited historical depth",
            "✅ Cortex Analyst (ask questions in English)",
            "✅ Streaming + batch in one platform",
            "✅ Row-level security, masking, auditing",
            "Pay-per-use, scales to zero",
            "✅ Streamlit apps built-in"
        ]
    }
    
    df_compare = pd.DataFrame(comparison_data)
    st.dataframe(df_compare, use_container_width=True, hide_index=True)
    
    st.markdown("""
    > **Bottom Line:** Grafana stays in your stack for operational monitoring. Snowflake sits *underneath* as the platform 
    > that consolidates your data, powers AI, and delivers business value. They're complementary — not competitive.
    """)

with tab2:
    st.markdown("""
    ### Why Snowflake Actually *Reduces* Competing Priorities
    
    The biggest drain on your team's time today isn't any single project — it's **managing complexity across fragmented systems**.
    """)
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("""
        #### ❌ Today's Priority Tax
        - Maintaining Oracle DB + SERAS Warehouse + Shared Files
        - Managing Prometheus/Loki scaling issues
        - Building custom ETL for each new data flow
        - Recreating dashboards across Power BI, Grafana, SafeCentral
        - Manual CSV transfers for ATM balancing
        - No AI capabilities without months of development
        """)
    with col_b:
        st.markdown("""
        #### ✅ With Snowflake (Priorities Consolidated)
        - **One platform** for all data (streaming + batch)
        - **Built-in AI** — no separate ML infrastructure
        - **Streamlit apps** replace fragmented dashboards
        - **Automated ingestion** replaces manual CSV
        - **Governance built-in** — no separate tooling
        - **Team focuses on value**, not infrastructure
        """)
    
    st.markdown("""
    > **The ask isn't to add a priority.** It's to *replace 5 existing priorities with 1 platform* 
    > that delivers more value with less effort.
    """)

st.markdown("---")
st.markdown("## 📈 Value Roadmap: Year 1, 2, 3")

year_tab1, year_tab2, year_tab3 = st.tabs(["**Year 1 — Foundation & Quick Wins**", "**Year 2 — Scale & Differentiation**", "**Year 3 — Market Leadership**"])

with year_tab1:
    st.markdown('<span class="year-badge">YEAR 1: $350K–$625K ACV</span>', unsafe_allow_html=True)
    st.markdown("")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        #### Use Cases Delivered
        | Use Case | Business Value |
        |----------|---------------|
        | **ATM AI Assist (Pilot)** | Real-time AI on transaction audio → faster resolution, reduced call center load |
        | **Transaction Analytics** | Unified view of all ATM transactions across Kafka, Oracle, CSVs |
        | **Anomaly Detection** | Cortex AI identifies suspicious patterns in real-time |
        | **Customer Dashboards** | Multi-tenant Streamlit dashboards replace Power BI/Portal |
        | **Data Consolidation** | Oracle + SERAS + Shared Files → Snowflake |
        """)
    with col2:
        st.markdown("""
        #### Key Metrics
        """)
        st.metric("Insight Speed", "10x faster", "Hours → Minutes")
        st.metric("Dashboard Tools", "5 → 1", "Consolidated")
        st.metric("AI Development", "Weeks → Days", "Cortex AI")

with year_tab2:
    st.markdown('<span class="year-badge">YEAR 2: $700K–$1.2M ACV</span>', unsafe_allow_html=True)
    st.markdown("")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        #### Use Cases Delivered
        | Use Case | Business Value |
        |----------|---------------|
        | **Predictive Maintenance** | IoT sensor data → predict ATM failures before they happen |
        | **Cash Management Optimization** | AI-driven cash forecasting across ATM networks |
        | **Security/Tamper Detection** | Cortex AI on sensor data for real-time threat detection |
        | **IT Log Analysis** | Consolidate observability data into Snowflake for AI-powered root cause |
        | **Multi-tenant Benchmarking** | Sell anonymized benchmarking data to banking clients |
        | **Microsoft Fabric Displacement** | Move Azure analytics workloads to Snowflake |
        """)
    with col2:
        st.markdown("""
        #### Key Metrics
        """)
        st.metric("ATM Uptime", "+15–25%", "Predictive maintenance")
        st.metric("Cash Optimization", "$2M+ saved", "Across network")
        st.metric("New Revenue", "Benchmarking", "Data product")

with year_tab3:
    st.markdown('<span class="year-badge">YEAR 3: $1.5M–$2.5M+ ACV</span>', unsafe_allow_html=True)
    st.markdown("")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        #### Use Cases Delivered
        | Use Case | Business Value |
        |----------|---------------|
        | **Data Product Monetization** | Sell ATM intelligence as a service to banking clients |
        | **Global Scale** | 80-country deployment on single platform |
        | **Enterprise Data Platform** | Finance, HR, Supply Chain all on Snowflake |
        | **AI-Powered RFP Tool** | Cortex AI generates proposals from knowledge base |
        | **Language Translation** | Real-time multilingual ATM assistance |
        | **Sign Language Avatars** | AI accessibility features powered by Cortex |
        """)
    with col2:
        st.markdown("""
        #### Key Metrics
        """)
        st.metric("New Revenue Streams", "3+", "Data products")
        st.metric("Enterprise Consolidation", "80%", "On Snowflake")
        st.metric("Competitive Moat", "Unassailable", "AI + Data + Scale")

st.markdown("---")
st.markdown("## 🚀 What Snowflake Enables That You Can't Do Today")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    ### 🆕 Net-New Capabilities
    - **Real-time AI inference** on ATM transactions (Cortex AI)
    - **Natural language queries** — ask questions in English, get answers
    - **Secure multi-tenant data sharing** — each banking client sees only their data
    - **AI-powered anomaly detection** without building ML infrastructure
    - **Data monetization** — sell ATM intelligence as a product
    """)

with col2:
    st.markdown("""
    ### ⬆️ What Gets Better
    - **Dashboard creation**: Weeks → Hours (Streamlit)
    - **Data freshness**: Hours → Seconds (Snowpipe Streaming)
    - **Cross-team collaboration**: Siloed → Unified
    - **Compliance**: Manual → Automated governance
    - **Cost**: Pay-per-use vs. always-on infrastructure
    """)

with col3:
    st.markdown("""
    ### 💡 Why You Need It Now
    - **IBM WatsonX** is approaching your AI teams
    - **Microsoft Fabric** PoC is underway — Snowflake is superior for AI
    - **First-mover advantage** in ATM AI monetization
    - **Technical debt** compounds — every month adds cost
    - **Pilot is funded** — $10K eval credits + PS workshop ready
    """)

st.markdown("---")

fig_value = go.Figure()
years = ["Today", "Year 1", "Year 2", "Year 3"]
snowflake_value = [0, 625, 1200, 2500]
cost_savings = [0, 150, 400, 800]
new_revenue = [0, 0, 200, 600]

fig_value.add_trace(go.Bar(name="Snowflake ACV ($K)", x=years, y=snowflake_value, marker_color="#29B5E8"))
fig_value.add_trace(go.Bar(name="Cost Savings ($K)", x=years, y=cost_savings, marker_color="#4CAF50"))
fig_value.add_trace(go.Bar(name="New Revenue Enabled ($K)", x=years, y=new_revenue, marker_color="#FF9800"))

fig_value.update_layout(
    title="Total Value Creation with Snowflake",
    barmode="group",
    template="plotly_dark",
    height=400,
    yaxis_title="$ Thousands"
)
st.plotly_chart(fig_value, use_container_width=True)

st.markdown("---")
st.markdown("## 👥 What's In It For Your Team")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    ### Bruce Diesel
    *Director, Product Management*
    
    - Ship AI-powered ATM features **faster**
    - Differentiate DN products with built-in intelligence
    - Deliver customer-facing analytics as a product feature
    - Reduce dependency on engineering for dashboards
    """)

with col2:
    st.markdown("""
    ### Tanya Gill
    *Global Director, Security Architecture*
    
    - **Unified security posture** across all data
    - Row-level security, dynamic masking, encryption at rest
    - Complete audit trail for compliance
    - AI-powered threat detection on ATM telemetry
    - Eliminate data sprawl security risks
    """)

with col3:
    st.markdown("""
    ### Michael Engel
    *VP Software, Managed Services & R&D*
    
    - **Reduce tech debt** — consolidate 5+ data systems
    - Accelerate R&D with built-in AI (no ML team needed)
    - Lower infrastructure costs (pay-per-use)
    - Team focuses on innovation, not maintenance
    - Managed services become AI-powered
    """)

st.markdown("---")
st.markdown("### Next Step: Activate the Pilot")
st.info("""
**The pilot is already funded and scoped.** Snowflake has approved $10K in evaluation credits and a no-cost Professional Services workshop.
Kirubel Legasion (Chief Architect) is ready to execute. The only thing needed is alignment from leadership to proceed.

**Timeline:** 8 weeks from kickoff to first AI-powered insights on live ATM data.
""")

st.markdown("---")
st.caption("Prepared by Snowflake for Diebold Nixdorf | ATM AI Assist Initiative | May 2026")
