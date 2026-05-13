import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from notes_utils import render_section_notes

st.set_page_config(page_title="Future State Architecture | Diebold Nixdorf", page_icon="🏗️", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    .stApp {font-family: 'Inter', sans-serif;}
    .dn-header {background: linear-gradient(135deg, #003366 0%, #004d99 50%, #29B5E8 100%); padding: 2.5rem 2rem; border-radius: 0 0 20px 20px; margin: -1rem -1rem 2rem -1rem; text-align: center;}
    .dn-title {font-size: 2.4rem; font-weight: 800; color: white; margin: 0;}
    .dn-subtitle {font-size: 1rem; color: #b3d9ff; margin-top: 0.5rem;}
    .before-box {background: #fff5f5; padding: 1.5rem; border-radius: 10px; border-left: 4px solid #e74c3c; margin: 0.5rem 0; color: #333;}
    .after-box {background: #f0fff4; padding: 1.5rem; border-radius: 10px; border-left: 4px solid #27ae60; margin: 0.5rem 0; color: #333;}
    .change-box {background: #fffbf0; padding: 1.5rem; border-radius: 10px; border-left: 4px solid #f39c12; margin: 0.5rem 0; color: #333;}
    .section-divider {height: 2px; background: linear-gradient(90deg, #003366, #29B5E8, #003366); margin: 2rem 0; border-radius: 2px; opacity: 0.2;}
    .engagement-ref {background: #f0f7ff; padding: 1rem 1.5rem; border-radius: 8px; border-left: 3px solid #003366; margin: 0.5rem 0; font-size: 0.9rem; color: #003366;}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="dn-header">
    <div class="dn-title">Future State Architecture</div>
    <div class="dn-subtitle">Transaction Assist Reporting — Before & After with Snowflake<br>Based on Kirubel Legasion's architecture design (April 2026)</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="engagement-ref">
📎 <strong>Context:</strong> This architecture was designed in collaboration with Kirubel Legasion (Chief Architect) during our October 2025 – April 2026 engagement. 
The current state diagram reflects Kiru's Confluence page "Transaction Assist Reporting Architecture with Snowflake." 
Our recommended future state consolidates the data layer while keeping Grafana for operational monitoring.
</div>
""", unsafe_allow_html=True)

view_mode = st.radio("View Mode", ["Before & After Comparison", "Detailed Change Log", "Cost & Capability Analysis"], horizontal=True)

if view_mode == "Before & After Comparison":
    st.markdown("## Current State (Before)")
    st.markdown("""
    <div class="mermaid-container">
    """, unsafe_allow_html=True)
    
    st.markdown("""
    ```
    ┌─────────────────────────────────────────────────────────────────────────────────────────┐
    │                          CURRENT STATE ARCHITECTURE                                       │
    │                                                                                           │
    │  ┌──────────────────┐          ┌─────────────────────┐     ┌────────────────────────┐   │
    │  │  CUSTOMER ENV     │          │  TRANSACTION         │     │  File Transfer          │   │
    │  │  ATM Terminals    │─────────▶│  Automation Server   │     │  Location (CSV)         │   │
    │  │  Contact Center   │          └─────────┬───────────┘     └───────────┬────────────┘   │
    │  └──────────────────┘                     │                             │                 │
    │                                           │ Call State Data              │ ATM Balancing   │
    │                                           │ (RTP & Batch)               │ Reports (CSV)   │
    │                                           ▼                             ▼                 │
    │  ┌──────────────┐    ┌──────────────┐   ┌──────────┐   ┌──────────────────────────┐    │
    │  │              │    │              │   │          │   │                          │    │
    │  │   Grafana    │◀───│  Prometheus  │◀──│  oTel    │   │    Kafka                 │    │
    │  │  Dashboards  │    │              │   │Collector │   │  (Transaction Data -     │    │
    │  │              │    └──────────────┘   └──────────┘   │   Batch Processing)      │    │
    │  └──────┬───────┘    ┌──────────────┐                  └──────────┬───────────────┘    │
    │         │            │  Loki DB     │                             │                     │
    │         │            │  Server      │                             │                     │
    │    Webhooks          └──────────────┘                             ▼                     │
    │         │                                              ┌─────────────────────┐          │
    │         ▼                                              │  eServices ICE(2)   │          │
    │  ┌─────────────┐                                      │  Server             │          │
    │  │ Zoom/Twilio │                                      └──────────┬──────────┘          │
    │  │ Alerts      │                                                 │                      │
    │  └─────────────┘                                                 ▼                      │
    │                              ┌─────────────┐  ┌──────────────┐  ┌─────────┐            │
    │  ┌──────────────┐           │ eServices   │  │ SERAS/NA MS  │  │Power BI │            │
    │  │  Snowflake   │◀─ ─ ─ ─ ─│ Oracle DB   │  │ Data         │  │         │            │
    │  │  Cortex AI   │           │             │  │ Warehouse    │  └─────────┘            │
    │  │  (Limited)   │           └─────────────┘  └──────────────┘                          │
    │  └──────────────┘                                                                       │
    │                              ┌──────────────┐                                           │
    │                              │  Shared File │──────────▶ SafeCentral                    │
    │                              │  Location    │                                           │
    │                              └──────────────┘                                           │
    └─────────────────────────────────────────────────────────────────────────────────────────┘
    ```
    """)
    
    st.markdown("""
    <div class="before-box">
    <strong>❌ Pain Points in Current State:</strong>
    <ul>
    <li><strong>5 separate data stores</strong> (Oracle, SERAS, Loki, Shared Files, Prometheus) — high maintenance cost</li>
    <li><strong>Batch processing only</strong> — Kafka data processed in batches, CSV files transferred manually</li>
    <li><strong>No AI capabilities</strong> — Snowflake/Cortex AI shown but barely connected (dashed lines)</li>
    <li><strong>Fragmented visualization</strong> — Grafana, Power BI, SafeCentral, eServices Portal all separate</li>
    <li><strong>No multi-tenant sharing</strong> — each customer report is manually generated</li>
    <li><strong>Grafana limitations</strong> — great for ops metrics, cannot do business analytics or AI</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("## Recommended Future State (After)")
    
    st.markdown("""
    ```
    ┌─────────────────────────────────────────────────────────────────────────────────────────┐
    │                         FUTURE STATE ARCHITECTURE (RECOMMENDED)                           │
    │                                                                                           │
    │  ┌──────────────────┐          ┌─────────────────────┐                                  │
    │  │  CUSTOMER ENV     │          │  Transaction         │                                  │
    │  │  ATM Terminals    │─────────▶│  Automation Server   │                                  │
    │  │  Contact Center   │          └─────────┬───────────┘                                  │
    │  └──────────────────┘                     │                                              │
    │                                           │ Call State Data (Real-time)                   │
    │                                           ▼                                              │
    │  ┌──────────────┐    ┌──────────────┐   ┌──────────┐                                   │
    │  │              │    │              │   │          │                                     │
    │  │   Grafana    │◀───│  Prometheus  │◀──│  oTel    │         ┌──────────────────┐       │
    │  │  (Ops Only)  │    │  (Metrics)   │   │Collector │         │                  │       │
    │  │              │    └──────┬───────┘   └──────────┘         │    Kafka         │       │
    │  └──────────────┘          │                                  │  (Streaming)     │       │
    │         │                   │ Metrics                          │                  │       │
    │         │                   │ Feed                             └────────┬─────────┘       │
    │         │                   ▼                                           │                 │
    │         │          ┌────────────────────────────────────────────────────┼────────────┐   │
    │         │          │              ❄️  SNOWFLAKE DATA CLOUD              │            │   │
    │         │          │                                                    │            │   │
    │         │          │  ┌─────────────────┐   ┌──────────────────────┐   │            │   │
    │         │          │  │ Snowpipe        │◀──┘ Real-time Streaming  │   │            │   │
    │         └─────────▶│  │ Streaming       │      (replaces batch)    │   │            │   │
    │    Metrics into    │  └────────┬────────┘   └──────────────────────┘               │   │
    │    Snowflake       │           │                                                    │   │
    │                    │           ▼                                                     │   │
    │                    │  ┌─────────────────────────────────────────────────────────┐   │   │
    │                    │  │           UNIFIED DATA LAKE                              │   │   │
    │                    │  │  • Transaction Data (from Kafka - real-time)             │   │   │
    │                    │  │  • Call State / Audio Data (from oTel)                   │   │   │
    │                    │  │  • ATM Balancing (automated ingestion - no CSV)          │   │   │
    │                    │  │  • Operational Metrics (from Prometheus)                 │   │   │
    │                    │  │  • Historical Data (migrated from Oracle/SERAS)          │   │   │
    │                    │  └────────────────────────────┬────────────────────────────┘   │   │
    │                    │                               │                                 │   │
    │                    │              ┌────────────────┼───────────────────┐             │   │
    │                    │              ▼                ▼                   ▼             │   │
    │                    │  ┌──────────────┐  ┌──────────────────┐  ┌─────────────────┐  │   │
    │                    │  │  Cortex AI   │  │  Cortex Analyst  │  │  Cortex Search  │  │   │
    │                    │  │              │  │                  │  │                 │  │   │
    │                    │  │ • Anomaly    │  │ • Natural Lang   │  │ • Knowledge     │  │   │
    │                    │  │   Detection  │  │   Queries        │  │   Base Search   │  │   │
    │                    │  │ • Predictive │  │ • Self-service   │  │ • RFP Auto-     │  │   │
    │                    │  │   Maint.     │  │   Analytics      │  │   generation    │  │   │
    │                    │  │ • Audio NLP  │  │ • Exec Dashboards│  │                 │  │   │
    │                    │  └──────┬───────┘  └────────┬─────────┘  └────────┬────────┘  │   │
    │                    │         │                    │                      │           │   │
    │                    │         └────────────────────┼──────────────────────┘           │   │
    │                    │                              ▼                                  │   │
    │                    │  ┌─────────────────────────────────────────────────────────┐   │   │
    │                    │  │           STREAMLIT APPS (Multi-Tenant)                  │   │   │
    │                    │  │                                                          │   │   │
    │                    │  │  • Bank A Dashboard    • Bank B Dashboard               │   │   │
    │                    │  │  • Executive Analytics • Operations Center               │   │   │
    │                    │  │  • Customer Self-Service Portal                          │   │   │
    │                    │  │  (Replaces: Power BI, SafeCentral, eServices Portal)    │   │   │
    │                    │  └─────────────────────────────────────────────────────────┘   │   │
    │                    │                                                                 │   │
    │                    │  ┌─────────────────────────────────────────────────────────┐   │   │
    │                    │  │           SECURE DATA SHARING                            │   │   │
    │                    │  │  • Per-customer data isolation (row-level security)      │   │   │
    │                    │  │  • Benchmarking data product (anonymized, monetizable)   │   │   │
    │                    │  │  • Partner integrations (Hakkoda, etc.)                  │   │   │
    │                    │  └─────────────────────────────────────────────────────────┘   │   │
    │                    └────────────────────────────────────────────────────────────────┘   │
    │                                                                                         │
    │  ┌────────────────────────────────────────────┐                                        │
    │  │  DECOMMISSIONED / CONSOLIDATED:            │                                        │
    │  │  ✗ Oracle DB (migrated to Snowflake)       │                                        │
    │  │  ✗ SERAS/NA MS Warehouse (consolidated)    │                                        │
    │  │  ✗ Loki DB Server (logs → Snowflake)       │                                        │
    │  │  ✗ Shared File Location (automated)        │                                        │
    │  │  ✗ Power BI (replaced by Streamlit)        │                                        │
    │  │  ✗ SafeCentral (replaced by Streamlit)     │                                        │
    │  │  ✗ eServices Portal (replaced)             │                                        │
    │  └────────────────────────────────────────────┘                                        │
    └─────────────────────────────────────────────────────────────────────────────────────────┘
    ```
    """)
    
    st.markdown("""
    <div class="after-box">
    <strong>✅ Future State Benefits:</strong>
    <ul>
    <li><strong>Single platform</strong> — All data in Snowflake (real-time + historical)</li>
    <li><strong>Built-in AI</strong> — Cortex AI, Analyst, and Search for all use cases</li>
    <li><strong>Real-time streaming</strong> — Snowpipe Streaming replaces batch Kafka processing</li>
    <li><strong>Multi-tenant dashboards</strong> — Streamlit apps with secure data sharing per bank</li>
    <li><strong>7 systems decommissioned</strong> — Oracle, SERAS, Loki, Shared Files, Power BI, SafeCentral, eServices Portal</li>
    <li><strong>Grafana retained</strong> — For operational alerting (its strength), feeding metrics into Snowflake</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

elif view_mode == "Detailed Change Log":
    st.markdown("## Architecture Changes — Detailed Breakdown")
    
    changes = [
        {
            "num": "1",
            "title": "Kafka Batch → Snowpipe Streaming (Real-time)",
            "action": "UPGRADE",
            "before": "Kafka processes transaction data in batches, introducing latency of hours before data is available for analysis.",
            "after": "Snowpipe Streaming ingests from Kafka in real-time (sub-second latency). AI can act on transactions as they happen.",
            "value": "Enables real-time anomaly detection, instant customer insights, and live dashboards."
        },
        {
            "num": "2",
            "title": "Oracle DB + SERAS Warehouse → Snowflake Unified Lake",
            "action": "CONSOLIDATE",
            "before": "eServices Oracle DB and SERAS/NA MS Data Warehouse store overlapping data in separate systems, requiring ETL between them.",
            "after": "All transactional and analytical data lives in Snowflake. Zero-copy cloning for dev/test. Time travel for recovery.",
            "value": "Eliminates Oracle licensing ($200K+/yr), removes ETL complexity, single source of truth."
        },
        {
            "num": "3",
            "title": "Shared File Location (CSV) → Automated Ingestion",
            "action": "REMOVE",
            "before": "ATM Balancing Reports transferred as CSV files to shared locations, then manually processed into SafeCentral.",
            "after": "Automated Snowpipe ingestion from source systems. No manual file transfers. Data available instantly.",
            "value": "Eliminates manual processes, reduces errors, saves 10+ hours/week of team time."
        },
        {
            "num": "4",
            "title": "Loki DB Server → Snowflake (Log Analytics)",
            "action": "CONSOLIDATE",
            "before": "Loki stores logs separately from business data. Limited retention, expensive at scale, no AI capabilities.",
            "after": "Logs ingested into Snowflake alongside business data. Cortex AI performs root cause analysis across logs + transactions.",
            "value": "Correlate operational issues with business impact. AI-powered incident response."
        },
        {
            "num": "5",
            "title": "Power BI + SafeCentral + eServices Portal → Streamlit",
            "action": "REPLACE",
            "before": "Three separate visualization tools, each requiring licenses, maintenance, and separate data pipelines.",
            "after": "Streamlit apps built directly on Snowflake. Multi-tenant, real-time, AI-powered. Deploy in hours, not weeks.",
            "value": "Eliminates $100K+/yr in BI licensing. Faster dashboard creation. Built-in AI features."
        },
        {
            "num": "6",
            "title": "Snowflake Cortex AI (Dashed → Solid Connection)",
            "action": "ACTIVATE",
            "before": "Snowflake and Cortex AI shown but barely integrated (dashed lines in current architecture).",
            "after": "Cortex AI is the central intelligence layer: NLP on audio, anomaly detection, predictive maintenance, natural language queries.",
            "value": "AI capabilities without building ML infrastructure. Production AI in weeks, not months."
        },
        {
            "num": "7",
            "title": "Grafana: Retained for Operational Monitoring",
            "action": "KEEP",
            "before": "Grafana used as primary analytics tool (beyond its design purpose).",
            "after": "Grafana focused on real-time ops alerting (its strength). Business analytics and AI handled by Snowflake.",
            "value": "Each tool does what it's best at. Grafana metrics feed into Snowflake for holistic analysis."
        },
        {
            "num": "8",
            "title": "Add: Secure Data Sharing (Multi-Tenant)",
            "action": "ADD",
            "before": "No capability to securely share per-customer data. Each bank's report is manually created.",
            "after": "Snowflake Secure Data Sharing provides each banking client their own governed view. Zero-copy, real-time.",
            "value": "Enables data-as-a-product business model. Each bank self-serves. New revenue stream."
        }
    ]
    
    for change in changes:
        action_color = {"UPGRADE": "#FF9800", "CONSOLIDATE": "#29B5E8", "REMOVE": "#ff4444", "REPLACE": "#9C27B0", "ACTIVATE": "#4CAF50", "KEEP": "#607D8B", "ADD": "#4CAF50"}
        color = action_color.get(change["action"], "#29B5E8")
        
        with st.expander(f"**Change #{change['num']}**: {change['title']} — `{change['action']}`", expanded=False):
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"""<div class="before-box"><strong>Before:</strong><br>{change["before"]}</div>""", unsafe_allow_html=True)
            with col2:
                st.markdown(f"""<div class="after-box"><strong>After:</strong><br>{change["after"]}</div>""", unsafe_allow_html=True)
            st.markdown(f"""<div class="change-box"><strong>💡 Value Delivered:</strong> {change["value"]}</div>""", unsafe_allow_html=True)

elif view_mode == "Cost & Capability Analysis":
    st.markdown("## Cost Savings Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Systems Eliminated / Consolidated")
        savings_data = pd.DataFrame({
            "System": ["Oracle DB Licensing", "SERAS/NA MS Warehouse", "Power BI Licensing", "Loki DB Infrastructure", "Manual File Processing (FTE)", "SafeCentral Licensing", "ETL Maintenance (FTE)", "eServices Portal"],
            "Est. Annual Cost": ["$200K–$350K", "$100K–$150K", "$50K–$100K", "$40K–$80K", "$80K–$120K (labor)", "$30K–$50K", "$60K–$100K (labor)", "$25K–$40K"],
            "Status": ["Decommission Y1-Y2", "Migrate to Snowflake Y1", "Replace with Streamlit Y1", "Consolidate into Snowflake Y2", "Automated via Snowpipe Y1", "Replace with Streamlit Y1", "Eliminated (native connectors)", "Replace with Streamlit Y1"]
        })
        st.dataframe(savings_data, use_container_width=True, hide_index=True)
        
        st.markdown("### Total Estimated Savings")
        st.markdown("""
        | Timeframe | Estimated Savings |
        |-----------|-------------------|
        | Year 1 | $200K–$400K |
        | Year 2 | $450K–$700K |
        | Year 3 | $600K–$990K |
        """)
    
    with col2:
        st.markdown("### New Capabilities Unlocked")
        capabilities = pd.DataFrame({
            "Capability": [
                "Real-time AI Inference",
                "Natural Language Queries",
                "Multi-Tenant Data Sharing",
                "Predictive Maintenance",
                "Data Monetization",
                "Automated Governance",
                "Self-Service Analytics",
                "Cross-Data Correlation"
            ],
            "Enabled By": [
                "Cortex AI + Snowpipe Streaming",
                "Cortex Analyst",
                "Secure Data Sharing",
                "Cortex AI + IoT Data",
                "Snowflake Marketplace",
                "Row-level Security + Masking",
                "Streamlit + Cortex Analyst",
                "Unified Data Lake"
            ],
            "Business Impact": [
                "Detect fraud/anomalies in real-time",
                "Execs ask questions, get answers",
                "Serve 100s of bank clients from 1 platform",
                "Reduce ATM downtime 15-25%",
                "New revenue: sell ATM benchmarking data",
                "Audit-ready without manual effort",
                "Non-technical users build own dashboards",
                "Link ops issues to business outcomes"
            ]
        })
        st.dataframe(capabilities, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    st.markdown("### ROI Visualization")
    
    fig = go.Figure()
    quarters = ["Q1", "Q2", "Q3", "Q4", "Q5", "Q6", "Q7", "Q8", "Q9", "Q10", "Q11", "Q12"]
    investment = [75, 125, 150, 100, 80, 60, 50, 50, 50, 50, 50, 50]
    savings = [0, 25, 75, 150, 200, 275, 350, 400, 450, 500, 550, 600]
    net_value = [s - i for s, i in zip(savings, investment)]
    
    fig.add_trace(go.Scatter(x=quarters, y=investment, name="Snowflake Investment ($K)", line=dict(color="#29B5E8", width=3)))
    fig.add_trace(go.Scatter(x=quarters, y=savings, name="Cumulative Savings ($K)", line=dict(color="#4CAF50", width=3)))
    fig.add_trace(go.Scatter(x=quarters, y=net_value, name="Net Value ($K)", line=dict(color="#FF9800", width=2, dash="dash"), fill="tozeroy", fillcolor="rgba(255,152,0,0.1)"))
    
    fig.update_layout(
        title="Investment vs. Savings Over 3 Years (Quarterly)",
        template="plotly_dark",
        height=400,
        yaxis_title="$ Thousands",
        xaxis_title="Quarter"
    )
    st.plotly_chart(fig, use_container_width=True)
    
    st.success("**Break-even point: Quarter 4** — After Q4, Snowflake pays for itself through eliminated systems and productivity gains.")

st.markdown("---")

st.markdown("## Snowflake vs. Grafana: Complete Differentiation")
st.markdown("""
| Dimension | Grafana | Snowflake | Why It Matters for DN |
|-----------|---------|-----------|----------------------|
| **What it is** | Observability dashboard tool | Data Cloud Platform + AI | Different categories entirely |
| **Data Storage** | None (uses Prometheus/Loki) | Unlimited cloud storage | Snowflake IS the database; Grafana just visualizes |
| **AI/ML** | None | Cortex AI (LLMs, ML, NLP) | ATM AI Assist needs AI — Grafana can't provide it |
| **Use Case** | "Is the system healthy?" | "Why? What next? How to improve?" | Business value vs. operational health |
| **Multi-tenant** | No | Yes (Secure Sharing) | Serve 100s of bank customers from 1 platform |
| **Cost Model** | Per-user licensing + infra | Pay-per-query (scales to zero) | Snowflake costs scale with actual usage |
| **Recommendation** | KEEP for ops monitoring | ADD as data + AI platform | Complementary — both stay in the stack |
""")

st.info("""
**Key Message for Stakeholders:** Snowflake is NOT replacing Grafana. Grafana remains for operational alerting. 
Snowflake is the platform that makes your data *intelligent* — AI, analytics, sharing, and apps — all from one place.
""")

st.markdown("---")
st.caption("Architecture Recommendation | Prepared by Snowflake for Diebold Nixdorf | May 2026")

render_section_notes("arch_before_after", "Before & After Architecture")
render_section_notes("arch_changes", "Change Log & Cost Analysis")
render_section_notes("arch_general", "General Notes — Architecture")
