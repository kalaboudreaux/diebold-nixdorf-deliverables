import streamlit as st
import pandas as pd
from notes_utils import render_section_notes

st.set_page_config(page_title="Pilot Evaluation Plan | Diebold Nixdorf × Snowflake", page_icon="❄️", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    .stApp {font-family: 'Inter', sans-serif;}
    .dn-header {background: linear-gradient(135deg, #003366 0%, #004d99 50%, #29B5E8 100%); padding: 2.5rem 2rem; border-radius: 0 0 20px 20px; margin: -1rem -1rem 2rem -1rem; text-align: center;}
    .dn-title {font-size: 2.4rem; font-weight: 800; color: white; margin: 0;}
    .dn-subtitle {font-size: 1rem; color: #b3d9ff; margin-top: 0.5rem;}
    .section-divider {height: 2px; background: linear-gradient(90deg, #003366, #29B5E8, #003366); margin: 2.5rem 0; border-radius: 2px; opacity: 0.2;}
    .phase-card {background: white; padding: 1.8rem; border-radius: 14px; box-shadow: 0 2px 12px rgba(0,0,0,0.06); border-top: 4px solid #29B5E8; margin: 0.8rem 0;}
    .phase-card h4 {color: #003366; margin-top: 0;}
    .checklist-card {background: #f8fbff; padding: 1.5rem; border-radius: 12px; border: 1px solid #29B5E820; margin: 0.6rem 0;}
    .success-card {background: linear-gradient(135deg, #f0fff4 0%, #e8f8ed 100%); padding: 1.5rem; border-radius: 12px; border-left: 4px solid #27ae60; margin: 0.6rem 0;}
    .move-forward-card {background: linear-gradient(135deg, #003366 0%, #004d99 100%); padding: 2rem; border-radius: 14px; color: white; margin: 1rem 0;}
    .partner-badge {background: #29B5E8; color: white; padding: 4px 14px; border-radius: 20px; font-size: 0.8rem; font-weight: 600;}
    .date-badge {background: #003366; color: white; padding: 3px 12px; border-radius: 8px; font-size: 0.8rem; font-weight: 600;}
    .owner-tag {background: #e8f4fd; color: #003366; padding: 2px 10px; border-radius: 6px; font-size: 0.8rem; font-weight: 500;}
    .footer-bar {background: #003366; padding: 1.5rem; border-radius: 12px; text-align: center; color: white; margin-top: 2rem;}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="dn-header">
    <div class="dn-title">Pilot Evaluation Plan</div>
    <div class="dn-subtitle">ATM AI Assist — Transaction Assist with Snowflake + Cortex AI<br>
    <span style="font-size: 1.1rem; color: white; font-weight: 600;">May 14, 2026 — June 14, 2026 (30 Days)</span><br>
    Implementation Partner: <span class="partner-badge">Anblicks</span></div>
</div>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown('<div style="background:white;padding:1.2rem;border-radius:12px;text-align:center;box-shadow:0 2px 8px rgba(0,0,0,0.05);border-top:3px solid #29B5E8;"><h2 style="color:#29B5E8;margin:0;">May 14</h2><p style="color:#666;margin:0;font-size:0.85rem;">PILOT START</p></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div style="background:white;padding:1.2rem;border-radius:12px;text-align:center;box-shadow:0 2px 8px rgba(0,0,0,0.05);border-top:3px solid #f39c12;"><h2 style="color:#f39c12;margin:0;">May 28</h2><p style="color:#666;margin:0;font-size:0.85rem;">MID-POINT CHECK</p></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div style="background:white;padding:1.2rem;border-radius:12px;text-align:center;box-shadow:0 2px 8px rgba(0,0,0,0.05);border-top:3px solid #27ae60;"><h2 style="color:#27ae60;margin:0;">June 14</h2><p style="color:#666;margin:0;font-size:0.85rem;">PILOT COMPLETE</p></div>', unsafe_allow_html=True)
with col4:
    st.markdown('<div style="background:white;padding:1.2rem;border-radius:12px;text-align:center;box-shadow:0 2px 8px rgba(0,0,0,0.05);border-top:3px solid #003366;"><h2 style="color:#003366;margin:0;">June 21</h2><p style="color:#666;margin:0;font-size:0.85rem;">GO / NO-GO DECISION</p></div>', unsafe_allow_html=True)

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

st.markdown("## 📋 What's Needed to Get Started")
st.markdown("*Pre-work that must be completed before or during Week 1 of the pilot.*")

col_l, col_r = st.columns(2)
with col_l:
    st.markdown("""
    <div class="checklist-card">
    <h4 style="color:#003366;">From Diebold Nixdorf</h4>
    <ul>
    <li><strong>Kafka access credentials</strong> — connection to Transaction Assist Kafka streams (Zoom/Twilio call metadata, ~5KB JSON per call)</li>
    <li><strong>Sample data extract</strong> — 30 days of historical call data for initial model training & dashboard prototyping</li>
    <li><strong>3–5 banking clients identified</strong> for pilot (mix of heavy/medium/light call volume)</li>
    <li><strong>Technical point of contact</strong> — Kirubel Legasion confirmed; need backup contact for Kafka/infrastructure access</li>
    <li><strong>Security review sign-off</strong> — PCI documentation provided; Tanya Gill's team to approve data flow</li>
    <li><strong>Banking client data mapping</strong> — schema for call metadata, ATM identifiers, client tenant IDs</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

with col_r:
    st.markdown("""
    <div class="checklist-card">
    <h4 style="color:#003366;">From Snowflake + Anblicks</h4>
    <ul>
    <li><strong>Snowflake evaluation account</strong> — provisioned with $10K eval credits (approved)</li>
    <li><strong>Kafka Connector configuration</strong> — Snowflake Kafka Connector for sub-second ingestion</li>
    <li><strong>Cortex AI environment</strong> — LLM functions enabled (sentiment analysis, classification, NLP)</li>
    <li><strong>Dynamic Tables setup</strong> — real-time data transformation pipeline</li>
    <li><strong>Anblicks implementation team</strong> — assigned engineers for build, integration, and dashboard delivery</li>
    <li><strong>Multi-tenant security architecture</strong> — row-level security policies for banking client isolation</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

st.markdown("## 📅 Mutual Success Timeline")

timeline = pd.DataFrame({
    "Week": ["Pre-Pilot", "Pre-Pilot", "Week 1 (May 14–18)", "Week 1 (May 14–18)", "Week 1 (May 14–18)", 
             "Week 2 (May 19–25)", "Week 2 (May 19–25)", "Week 2 (May 19–25)",
             "Week 3 (May 26–Jun 1)", "Week 3 (May 26–Jun 1)", "Week 3 (May 26–Jun 1)",
             "Week 4 (Jun 2–8)", "Week 4 (Jun 2–8)", "Week 4 (Jun 2–8)",
             "Week 5 (Jun 9–14)", "Week 5 (Jun 9–14)", "Week 5 (Jun 9–14)",
             "Post-Pilot (Jun 16–21)"],
    "Milestone": [
        "Snowflake eval account provisioned & Anblicks team onboarded",
        "Kafka credentials and sample data delivered by DN",
        "Kafka Connector configured — live streaming into Snowflake",
        "Dynamic Tables built — real-time transformation of call data",
        "Initial data quality validation with Kirubel",
        "Cortex AI sentiment analysis deployed on call transcripts",
        "Call classification & topic detection models activated",
        "First multi-tenant dashboard prototype (1 banking client)",
        "Mid-point review with stakeholders (May 28)",
        "Expand to 3–5 banking clients with row-level security",
        "Natural language query layer (Cortex Analyst) enabled",
        "Cross-client benchmarking analytics (anonymized)",
        "Teller performance scoring & coaching insights live",
        "Anomaly detection & fraud pattern alerting active",
        "Final dashboard polish & stakeholder demo prep",
        "Pilot results report compiled with ROI metrics",
        "Executive presentation delivered to Bruce, Tanya, Michael",
        "Go / No-Go decision meeting — move-forward plan presented"
    ],
    "Target Date": [
        "May 12", "May 13", "May 15", "May 16", "May 18",
        "May 20", "May 22", "May 25",
        "May 28", "May 30", "Jun 1",
        "Jun 3", "Jun 5", "Jun 8",
        "Jun 10", "Jun 12", "Jun 14",
        "Jun 21"
    ],
    "Owner": [
        "Snowflake (Kala)", "Kirubel / DN IT", "Anblicks", "Anblicks", "Kirubel + Anblicks",
        "Anblicks + Snowflake", "Anblicks + Snowflake", "Anblicks",
        "Kala + Kirubel", "Anblicks", "Snowflake PS",
        "Anblicks", "Anblicks + Snowflake", "Anblicks + Snowflake",
        "Anblicks", "Kala + Anblicks", "Kala",
        "Kala + Kirubel + Execs"
    ],
    "Status": [
        "✅ Done", "⏳ In Progress", "🔜 Upcoming", "🔜 Upcoming", "🔜 Upcoming",
        "🔜 Upcoming", "🔜 Upcoming", "🔜 Upcoming",
        "🔜 Upcoming", "🔜 Upcoming", "🔜 Upcoming",
        "🔜 Upcoming", "🔜 Upcoming", "🔜 Upcoming",
        "🔜 Upcoming", "🔜 Upcoming", "🔜 Upcoming",
        "🔜 Upcoming"
    ]
})

st.dataframe(timeline, use_container_width=True, hide_index=True, height=650)

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

st.markdown("## 🎯 Action Plan & Assignments")

tab_snow, tab_dn, tab_anblicks = st.tabs(["**Snowflake Team**", "**Diebold Nixdorf Team**", "**Anblicks (Implementation Partner)**"])

with tab_snow:
    actions_snow = pd.DataFrame({
        "Action Item": [
            "Provision Snowflake eval account with $10K credits",
            "Configure Cortex AI functions (sentiment, classification, translate)",
            "Set up Cortex Analyst for natural language queries",
            "Coordinate mid-point review (May 28)",
            "Compile pilot results report & ROI analysis",
            "Deliver executive presentation (June 14)",
            "Prepare enterprise agreement proposal for go/no-go (June 21)"
        ],
        "Owner": ["Kala Boudreaux", "Snowflake PS", "Snowflake PS", "Kala Boudreaux", "Kala + Anblicks", "Kala Boudreaux", "Kala + Sales Leadership"],
        "Due Date": ["May 12 ✅", "May 20", "Jun 1", "May 28", "Jun 12", "Jun 14", "Jun 21"],
        "Priority": ["Complete", "High", "Medium", "High", "High", "Critical", "Critical"]
    })
    st.dataframe(actions_snow, use_container_width=True, hide_index=True)

with tab_dn:
    actions_dn = pd.DataFrame({
        "Action Item": [
            "Provide Kafka access credentials for Transaction Assist streams",
            "Deliver 30-day historical call data sample",
            "Identify 3–5 banking clients for pilot",
            "Security review sign-off (Tanya Gill's team)",
            "Provide banking client data schema & tenant IDs",
            "Assign Kirubel as full-time technical POC during pilot",
            "Schedule mid-point exec review (May 28)",
            "Brief Michael Engel on pilot progress (ongoing)",
            "Attend final pilot presentation (June 14)",
            "Participate in go/no-go decision meeting (June 21)"
        ],
        "Owner": ["Kirubel Legasion", "Kirubel / IT Team", "Kirubel + Product", "Tanya Gill", "Kirubel", "Michael Engel (approval)", "Bruce Diesel / Michael Engel", "Kirubel → Michael", "Bruce, Tanya, Michael", "Bruce, Tanya, Michael, Kirubel"],
        "Due Date": ["May 13", "May 13", "May 14", "May 16", "May 14", "May 14", "May 22 (schedule)", "Weekly", "Jun 14", "Jun 21"],
        "Priority": ["Critical", "Critical", "High", "High", "High", "High", "Medium", "Ongoing", "Critical", "Critical"]
    })
    st.dataframe(actions_dn, use_container_width=True, hide_index=True)

with tab_anblicks:
    actions_partner = pd.DataFrame({
        "Action Item": [
            "Onboard to Snowflake eval environment",
            "Configure Snowflake Kafka Connector for live streaming",
            "Build Dynamic Tables for call data transformation",
            "Implement Cortex AI pipeline (sentiment, classification, topics)",
            "Build multi-tenant dashboard with row-level security",
            "Deploy cross-client benchmarking analytics",
            "Implement teller performance scoring model",
            "Build anomaly detection & fraud alerting",
            "Final dashboard polish & UX refinement",
            "Support pilot results report compilation"
        ],
        "Owner": ["Anblicks Lead", "Anblicks Engineer", "Anblicks Engineer", "Anblicks + Snowflake PS", "Anblicks Engineer", "Anblicks Engineer", "Anblicks + Snowflake", "Anblicks + Snowflake", "Anblicks", "Anblicks + Kala"],
        "Due Date": ["May 13", "May 15", "May 16", "May 22", "May 25", "Jun 3", "Jun 5", "Jun 8", "Jun 10", "Jun 12"],
        "Priority": ["Critical", "Critical", "Critical", "High", "High", "Medium", "Medium", "Medium", "High", "High"]
    })
    st.dataframe(actions_partner, use_container_width=True, hide_index=True)

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

st.markdown("## 📏 What We're Measuring & Why")

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div class="phase-card">
    <h4>Technical Metrics</h4>
    
    | Metric | Why It Matters | Target |
    |--------|---------------|--------|
    | **Data ingestion latency** | Proves real-time capability vs. batch CSV | < 5 seconds |
    | **Cortex AI accuracy** (sentiment) | Validates AI quality on call transcripts | > 90% agreement with manual labels |
    | **Dashboard load time** | User experience for banking clients | < 3 seconds |
    | **Multi-tenant data isolation** | Security requirement — zero data leakage | 100% isolation verified |
    | **Kafka throughput** | Handle peak call volumes (500 calls/day heavy client) | Zero dropped messages |
    | **Dynamic Table refresh** | Always-fresh data for dashboards | < 60 second lag |
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="phase-card">
    <h4>Business Metrics</h4>
    
    | Metric | Why It Matters | Target |
    |--------|---------------|--------|
    | **Time to insight** | How fast banking clients get actionable data | Hours → Seconds |
    | **Report creation effort** | Manual CSV + Power BI vs. automated | 80% reduction |
    | **New insights discovered** | AI finds patterns humans miss | 5+ per banking client |
    | **Stakeholder satisfaction** | Do banking clients want this as a product? | Positive feedback from 3+ clients |
    | **Teller coaching actionability** | Can managers act on AI recommendations? | Validated by 2+ pilot managers |
    | **Competitive differentiation** | Feature gap vs. NCR Atleos / Hyosung | Confirmed unique capability |
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

st.markdown("## ✅ Success Criteria")
st.markdown("*The pilot is successful if the following criteria are met by June 14:*")

st.markdown("""
<div class="success-card">
<h4 style="color: #27ae60; margin-top: 0;">Must-Have (All Required for Success)</h4>
<ol>
<li><strong>Live Kafka streaming into Snowflake</strong> — Transaction Assist call data flowing in real-time (sub-5-second latency)</li>
<li><strong>Cortex AI sentiment analysis operational</strong> — Automated sentiment scoring on call transcripts with >90% accuracy</li>
<li><strong>Multi-tenant dashboards delivered</strong> — At least 3 banking clients viewing their own secure, isolated analytics</li>
<li><strong>Security validated</strong> — Row-level security confirmed; zero cross-tenant data leakage; PCI-compliant architecture</li>
<li><strong>Stakeholder sign-off</strong> — Kirubel, Bruce, Tanya, or Michael confirm the pilot met expectations</li>
</ol>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="checklist-card">
<h4 style="color: #003366; margin-top: 0;">Nice-to-Have (Demonstrates Upside)</h4>
<ol>
<li><strong>Natural language queries</strong> — Banking client execs can ask questions in English via Cortex Analyst</li>
<li><strong>Cross-client benchmarking</strong> — Anonymized benchmarking data demonstrates data-as-a-product potential</li>
<li><strong>Teller performance scoring</strong> — AI-driven coaching recommendations validated by a pilot manager</li>
<li><strong>Anomaly/fraud detection</strong> — At least 1 real anomaly identified that would have been missed manually</li>
<li><strong>Quantified ROI</strong> — Clear $ value articulated for cost savings, revenue opportunity, or risk mitigation</li>
</ol>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

st.markdown("## 🚀 Move-Forward Plan: Pilot → Enterprise Agreement")

st.markdown("""
<div class="move-forward-card">
<h3 style="color: white; margin-top: 0;">If the pilot succeeds, here is the path to an enterprise agreement:</h3>
</div>
""", unsafe_allow_html=True)

move_forward = pd.DataFrame({
    "Phase": [
        "1. Pilot Complete",
        "2. Go / No-Go Decision",
        "3. Commercial Proposal",
        "4. Procurement & Legal",
        "5. Enterprise Agreement Signed",
        "6. Production Deployment",
        "7. Scale to Year 1 Use Cases"
    ],
    "Timeline": [
        "June 14, 2026",
        "June 21, 2026",
        "June 21–28, 2026",
        "July 2026",
        "July / August 2026",
        "August 2026",
        "Q3–Q4 FY2027"
    ],
    "Description": [
        "Pilot results report delivered. Executive presentation to Bruce, Tanya, Michael, Kirubel.",
        "Stakeholders review results vs. success criteria. Decision: proceed to commercial or stop.",
        "Snowflake delivers enterprise pricing proposal. Scope: Transaction Assist (10–20 banking clients) + Supply Chain. Est. Year 1 ACV: $250K–$425K.",
        "DN procurement and legal review. Snowflake provides PCI/SOC2 documentation, DPA, security questionnaire responses.",
        "Enterprise agreement executed. Production Snowflake account provisioned. Anblicks engaged for production build.",
        "Migrate pilot environment to production. Onboard first 10 banking clients. Go-live with AI-powered analytics.",
        "Expand to Supply Chain Demand Planning (Aamir/Sangeeta), begin RFP Tool evaluation, scale Transaction Assist to 20+ clients."
    ],
    "Key Decision-Makers": [
        "Kirubel (technical validation)",
        "Bruce, Tanya, Michael (leadership alignment)",
        "Michael Engel (budget), Tyler Wise (finance review)",
        "DN Legal & Procurement",
        "Michael Engel / Jerome Amara (EVP Banking)",
        "Kirubel + Anblicks",
        "Cross-functional (Product, Supply Chain, Finance)"
    ]
})

st.dataframe(move_forward, use_container_width=True, hide_index=True, height=300)

st.markdown("""
<div style="background: #f0f7ff; padding: 1.5rem; border-radius: 12px; border: 1px solid #29B5E820; margin: 1rem 0;">
<h4 style="color: #003366; margin-top: 0;">💡 Key Principle: Low Risk, High Learning</h4>
<p style="color: #333; margin: 0;">
The pilot is designed so that <strong>Diebold Nixdorf invests $0 upfront</strong>. Snowflake provides $10K in eval credits. 
Anblicks provides implementation services. If the pilot doesn't meet success criteria, DN walks away with zero financial exposure 
and valuable learnings about their data architecture. If it succeeds, DN has a production-ready platform and a clear commercial path.
</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="footer-bar">
<h3 style="margin: 0;">Pilot Kickoff: Thursday, May 14, 2026</h3>
<p style="margin: 0.5rem 0 0 0; opacity: 0.8;">Implementation Partner: Anblicks · Snowflake Account Team: Kala Boudreaux<br>
Technical Champion: Kirubel Legasion, Chief Architect</p>
</div>
""", unsafe_allow_html=True)

render_section_notes("pilot_prep", "Pre-Work & Requirements")
render_section_notes("pilot_timeline", "Timeline & Milestones")
render_section_notes("pilot_actions", "Action Plan & Assignments")
render_section_notes("pilot_success", "Success Criteria & Move-Forward Plan")
render_section_notes("pilot_general", "General Notes — Pilot Evaluation")
