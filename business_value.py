import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from notes_utils import render_section_notes

st.set_page_config(page_title="Business Value Analysis | Diebold Nixdorf × Snowflake", page_icon="❄️", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    .stApp {font-family: 'Inter', sans-serif;}
    .dn-header {background: linear-gradient(135deg, #003366 0%, #004d99 50%, #29B5E8 100%); padding: 2.5rem 2rem; border-radius: 0 0 20px 20px; margin: -1rem -1rem 2rem -1rem; text-align: center;}
    .dn-title {font-size: 2.4rem; font-weight: 800; color: white; margin: 0;}
    .dn-subtitle {font-size: 1rem; color: #b3d9ff; margin-top: 0.5rem;}
    .section-divider {height: 2px; background: linear-gradient(90deg, #003366, #29B5E8, #003366); margin: 2.5rem 0; border-radius: 2px; opacity: 0.2;}
    .value-card {background: white; padding: 2rem; border-radius: 14px; box-shadow: 0 2px 12px rgba(0,0,0,0.06); margin: 0.8rem 0; border-top: 4px solid #29B5E8;}
    .revenue-card {background: white; padding: 2rem; border-radius: 14px; box-shadow: 0 2px 12px rgba(0,0,0,0.06); margin: 0.8rem 0; border-top: 4px solid #27ae60;}
    .cost-card {background: white; padding: 2rem; border-radius: 14px; box-shadow: 0 2px 12px rgba(0,0,0,0.06); margin: 0.8rem 0; border-top: 4px solid #29B5E8;}
    .risk-card {background: white; padding: 2rem; border-radius: 14px; box-shadow: 0 2px 12px rgba(0,0,0,0.06); margin: 0.8rem 0; border-top: 4px solid #e74c3c;}
    .exec-callout {background: linear-gradient(135deg, #f8fbff 0%, #e8f4fd 100%); padding: 2rem; border-radius: 14px; border: 1px solid #29B5E820; margin: 1rem 0;}
    .exec-callout h3 {color: #003366; margin-top: 0;}
    .client-value {background: #f0fff4; padding: 1.5rem; border-radius: 12px; border-left: 4px solid #27ae60; margin: 0.6rem 0;}
    .dn-value {background: #f0f7ff; padding: 1.5rem; border-radius: 12px; border-left: 4px solid #003366; margin: 0.6rem 0;}
    .unlock-card {background: white; padding: 1.5rem; border-radius: 12px; border-left: 4px solid #29B5E8; box-shadow: 0 2px 8px rgba(0,0,0,0.04); margin: 0.6rem 0;}
    .big-number {font-size: 2.2rem; font-weight: 800; color: #003366; margin: 0;}
    .big-label {font-size: 0.8rem; color: #666; text-transform: uppercase; letter-spacing: 0.5px; margin: 0;}
    .footer-bar {background: #003366; padding: 1.5rem; border-radius: 12px; text-align: center; color: white; margin-top: 2rem;}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="dn-header">
    <div class="dn-title">Business Value Analysis</div>
    <div class="dn-subtitle">Revenue · Cost Savings · Risk Mitigation · Business Outcomes<br>
    Why Snowflake Matters for Diebold Nixdorf — and for Your Banking Clients</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="exec-callout">
<h3>📌 Why Should Executives Care?</h3>
<p style="color:#333; font-size: 1.05rem; line-height: 1.8; margin-bottom: 0;">
Diebold Nixdorf's <strong>$2.5B Global Services business</strong> depends on delivering value to banking clients who operate ATM networks. 
Today, Transaction Assist — DN's remote teller product — delivers <strong>basic CSV exports and Power BI dashboards</strong>. 
There is no AI. No real-time analytics. No competitive differentiation vs. NCR Atleos or Hyosung.<br><br>
Snowflake doesn't just modernize DN's technology — it transforms <strong>Transaction Assist from a cost center into a revenue-generating, AI-powered analytics product</strong> 
that banking clients will pay a premium for. This is a <strong>product strategy decision</strong>, not just an IT project.
</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

st.markdown("## 💰 Financial Impact Summary")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown('<div style="background:white;padding:1.5rem;border-radius:12px;text-align:center;box-shadow:0 2px 8px rgba(0,0,0,0.05);border-top:4px solid #27ae60;"><p class="big-number" style="color:#27ae60;">$2M–$5M+</p><p class="big-label">New Revenue (3yr)</p></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div style="background:white;padding:1.5rem;border-radius:12px;text-align:center;box-shadow:0 2px 8px rgba(0,0,0,0.05);border-top:4px solid #29B5E8;"><p class="big-number" style="color:#29B5E8;">$1.5M–$3M</p><p class="big-label">Cost Savings (3yr)</p></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div style="background:white;padding:1.5rem;border-radius:12px;text-align:center;box-shadow:0 2px 8px rgba(0,0,0,0.05);border-top:4px solid #e74c3c;"><p class="big-number" style="color:#e74c3c;">7-Figure</p><p class="big-label">Fraud Risk Mitigated</p></div>', unsafe_allow_html=True)
with col4:
    st.markdown('<div style="background:white;padding:1.5rem;border-radius:12px;text-align:center;box-shadow:0 2px 8px rgba(0,0,0,0.05);border-top:4px solid #003366;"><p class="big-number" style="color:#003366;">20+</p><p class="big-label">Use Cases Enabled</p></div>', unsafe_allow_html=True)

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

tab_rev, tab_cost, tab_risk, tab_outcomes = st.tabs(["**💵 Revenue Impact**", "**📉 Cost Savings**", "**🛡️ Risk Mitigation**", "**📊 Business Outcomes**"])

with tab_rev:
    st.markdown("### New Revenue Streams Enabled by Snowflake")
    
    st.markdown("""
    <div class="revenue-card">
    <h4 style="color: #27ae60; margin-top: 0;">1. Premium Analytics Tier — Transaction Assist</h4>
    <p><strong>What:</strong> Today DN gives banking clients free CSV reports. With Snowflake, DN offers AI-powered analytics as a <strong>paid premium service tier</strong> — 
    sentiment analysis, call classification, benchmarking, natural language queries, and teller coaching insights.</p>
    <p><strong>Revenue Model:</strong> Per-client monthly subscription. 35–50 banking clients × $2K–$5K/month premium = <strong>$840K–$3M annual recurring revenue</strong>.</p>
    <p><strong>Why it works:</strong> No ATM competitor offers this today. Banking clients are already asking for better analytics. This is product differentiation that sells.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="revenue-card">
    <h4 style="color: #27ae60; margin-top: 0;">2. Data-as-a-Product — ATM Benchmarking</h4>
    <p><strong>What:</strong> Snowflake's Secure Data Sharing enables DN to sell anonymized, cross-client benchmarking data — 
    "How does your ATM call volume compare to the industry? How does your resolution rate rank?"</p>
    <p><strong>Revenue Model:</strong> Annual benchmarking subscription. <strong>$500K–$1M+ annual opportunity</strong> as the ATM network scales.</p>
    <p><strong>Why it works:</strong> Only DN has this data at scale. It becomes a competitive moat that increases client stickiness — banks can't get this from NCR Atleos.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="revenue-card">
    <h4 style="color: #27ae60; margin-top: 0;">3. Client Retention & Upsell</h4>
    <p><strong>What:</strong> AI-powered analytics makes banking clients <strong>harder to churn</strong>. Clients who receive intelligence — not just hardware — 
    have significantly higher lifetime value and lower switching propensity.</p>
    <p><strong>Impact:</strong> Reducing churn by even 5% across DN's $2.5B services business = <strong>$125M in protected revenue</strong>.</p>
    </div>
    """, unsafe_allow_html=True)
    
    fig_rev = go.Figure()
    years = ["Year 1", "Year 2", "Year 3"]
    premium_analytics = [200, 800, 1500]
    benchmarking = [0, 250, 750]
    retention = [100, 300, 500]
    fig_rev.add_trace(go.Bar(name="Premium Analytics Tier", x=years, y=premium_analytics, marker_color="#27ae60"))
    fig_rev.add_trace(go.Bar(name="Benchmarking Data Product", x=years, y=benchmarking, marker_color="#2ecc71"))
    fig_rev.add_trace(go.Bar(name="Retention / Upsell Value", x=years, y=retention, marker_color="#a8e6cf"))
    fig_rev.update_layout(title="Projected New Revenue ($K)", barmode="stack", template="plotly_white", height=350, font=dict(family="Inter"), yaxis_title="$ Thousands")
    st.plotly_chart(fig_rev, use_container_width=True)

with tab_cost:
    st.markdown("### Where Snowflake Saves Money")
    
    savings = pd.DataFrame({
        "Cost Category": [
            "Manual report generation (FTE labor)",
            "Alteryx licensing (Finance ETL workaround)",
            "Power BI per-user licensing (replaced by Streamlit)",
            "Oracle DB licensing (consolidated into Snowflake)",
            "Custom ETL maintenance (Informatica PowerCenter)",
            "Data center / on-prem infrastructure",
            "Translation outsourcing (RFP + product docs)",
            "Emergency ATM cash replenishment (with AI prediction)"
        ],
        "Current Annual Cost": [
            "$150K–$250K",
            "$80K–$120K",
            "$50K–$100K",
            "$200K–$350K",
            "$100K–$150K",
            "$200K–$400K",
            "$200K–$500K",
            "$500K–$1M+"
        ],
        "Savings with Snowflake": [
            "80% reduction — automated dashboards",
            "100% elimination — Snowflake replaces Alteryx",
            "70% reduction — Streamlit included",
            "Phased migration — 50% by Year 2",
            "60% reduction — native connectors",
            "Progressive — as workloads move to cloud",
            "90% — Cortex Translate built-in",
            "20–30% — AI cash demand prediction"
        ],
        "Year Realized": [
            "Year 1",
            "Year 1",
            "Year 1",
            "Year 2",
            "Year 1",
            "Year 2–3",
            "Year 2",
            "Year 2"
        ]
    })
    st.dataframe(savings, use_container_width=True, hide_index=True)
    
    fig_cost = go.Figure()
    years_c = ["Year 1", "Year 2", "Year 3"]
    current_cost = [1500, 1500, 1500]
    with_snowflake = [1200, 900, 650]
    fig_cost.add_trace(go.Scatter(x=years_c, y=current_cost, name="Current State (Annual)", line=dict(color="#e74c3c", width=3, dash="dash"), fill="tonexty"))
    fig_cost.add_trace(go.Scatter(x=years_c, y=with_snowflake, name="With Snowflake (Annual)", line=dict(color="#29B5E8", width=3), fill="tozeroy", fillcolor="rgba(41,181,232,0.1)"))
    fig_cost.update_layout(title="Total Data Infrastructure Cost ($K/Year)", template="plotly_white", height=300, yaxis_title="$ Thousands", font=dict(family="Inter"))
    st.plotly_chart(fig_cost, use_container_width=True)

with tab_risk:
    st.markdown("### Risks Mitigated by Snowflake")
    
    st.markdown("""
    <div class="risk-card">
    <h4 style="color: #e74c3c; margin-top: 0;">🔒 Fraud & Security Risk</h4>
    <p><strong>Current State:</strong> No AI-powered fraud detection on ATM transactions. Card skimming, shoulder surfing, and rapid-transfer fraud 
    patterns are identified <strong>after the fact</strong> — often days or weeks later.</p>
    <p><strong>With Snowflake:</strong> Cortex AI analyzes call patterns and transaction data in real-time. Anomalous behavior triggers instant alerts. 
    Banking clients like Citibank have reported <strong>7-figure fraud losses</strong> that AI detection could have prevented.</p>
    <p><strong>Risk Mitigated:</strong> <span style="color: #e74c3c; font-weight: 700;">$1M–$10M+ in annual fraud exposure per banking client</span></p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="risk-card">
    <h4 style="color: #e74c3c; margin-top: 0;">⚠️ Competitive Displacement Risk</h4>
    <p><strong>Current State:</strong> IBM WatsonX is actively approaching DN's AI teams. Microsoft Fabric PoC is underway (David Champagne). 
    NCR Atleos is investing in analytics capabilities. Every month DN waits, competitors close the gap.</p>
    <p><strong>With Snowflake:</strong> DN becomes the <strong>first ATM company to offer AI-powered call analytics</strong> as a product. 
    First-mover advantage in a market where no competitor has this capability today.</p>
    <p><strong>Risk Mitigated:</strong> <span style="color: #e74c3c; font-weight: 700;">Protect $2.5B services business from competitive erosion</span></p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="risk-card">
    <h4 style="color: #e74c3c; margin-top: 0;">📋 Compliance & Data Governance Risk</h4>
    <p><strong>Current State:</strong> ATM Balancing Reports transferred as CSV files through shared file locations. 
    Multiple disconnected databases with no unified audit trail. Banking client data co-mingled in reporting systems.</p>
    <p><strong>With Snowflake:</strong> Enterprise-grade governance — row-level security, dynamic data masking, complete audit trail, 
    PCI-DSS / SOC2 / HIPAA / FedRAMP compliance built in. Every query, every access, logged and auditable.</p>
    <p><strong>Risk Mitigated:</strong> <span style="color: #e74c3c; font-weight: 700;">Regulatory penalties, data breach liability, banking client trust</span></p>
    </div>
    """, unsafe_allow_html=True)

with tab_outcomes:
    st.markdown("### Business Outcomes: The Full Picture")
    
    st.markdown("#### What Snowflake Unlocks That DN Can't Do Today")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="unlock-card">
        <h4 style="color: #003366; margin-top: 0;">🆕 Net-New Capabilities</h4>
        <ul>
        <li><strong>Real-time AI on every ATM call</strong> — sentiment, classification, topic detection, coaching recommendations</li>
        <li><strong>Natural language analytics</strong> — banking execs ask "show me all calls over 5 minutes today" and get instant answers</li>
        <li><strong>Multi-tenant data sharing</strong> — 50+ banking clients, each seeing only their data, from one platform</li>
        <li><strong>Cross-client benchmarking</strong> — "How does Bank A compare to the industry?" — a product no competitor offers</li>
        <li><strong>Predictive staffing</strong> — AI forecasts call volume by hour, geography, and language to optimize teller scheduling</li>
        <li><strong>Fraud pattern detection</strong> — identify card skimming and rapid-transfer patterns in real-time</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="unlock-card">
        <h4 style="color: #003366; margin-top: 0;">⬆️ What Gets Dramatically Better</h4>
        <ul>
        <li><strong>Reporting speed:</strong> Days/weeks → Seconds (CSV export → real-time dashboard)</li>
        <li><strong>New client onboarding:</strong> Weeks of custom setup → Hours (multi-tenant platform)</li>
        <li><strong>Data freshness:</strong> Batch (end of day) → Real-time (sub-second Kafka streaming)</li>
        <li><strong>Dashboard creation:</strong> Weeks of Power BI development → Hours in Streamlit</li>
        <li><strong>Teller quality management:</strong> Manual review of random samples → AI scores every call</li>
        <li><strong>Security posture:</strong> 5+ systems to secure → 1 platform with built-in governance</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    
    st.markdown("#### Value to Banking Clients (DN's Customers)")
    st.markdown("""
    <div class="client-value">
    <h4 style="color: #27ae60; margin-top: 0;">What Banking Clients Receive</h4>
    <table style="width: 100%; border-collapse: collapse;">
    <tr><td style="padding: 8px; border-bottom: 1px solid #e0e0e0;"><strong>Today (CSV + Power BI)</strong></td><td style="padding: 8px; border-bottom: 1px solid #e0e0e0;"><strong>With Snowflake (AI-Powered Analytics)</strong></td></tr>
    <tr><td style="padding: 8px; border-bottom: 1px solid #e0e0e0;">Static reports delivered days after calls</td><td style="padding: 8px; border-bottom: 1px solid #e0e0e0;">Real-time dashboard with live call analytics</td></tr>
    <tr><td style="padding: 8px; border-bottom: 1px solid #e0e0e0;">Basic volume counts — "you had 500 calls"</td><td style="padding: 8px; border-bottom: 1px solid #e0e0e0;">AI-powered insights — sentiment, trends, anomalies, coaching</td></tr>
    <tr><td style="padding: 8px; border-bottom: 1px solid #e0e0e0;">No fraud detection</td><td style="padding: 8px; border-bottom: 1px solid #e0e0e0;">Real-time anomaly alerts on suspicious patterns</td></tr>
    <tr><td style="padding: 8px; border-bottom: 1px solid #e0e0e0;">No benchmarking</td><td style="padding: 8px; border-bottom: 1px solid #e0e0e0;">"How do we compare to the industry?" — instant answer</td></tr>
    <tr><td style="padding: 8px; border-bottom: 1px solid #e0e0e0;">One-size-fits-all reports</td><td style="padding: 8px; border-bottom: 1px solid #e0e0e0;">Ask questions in plain English — self-service analytics</td></tr>
    <tr><td style="padding: 8px;">No teller quality scoring</td><td style="padding: 8px;">AI-driven coaching recommendations — improve service quality</td></tr>
    </table>
    <p style="margin-top: 1rem; font-weight: 600; color: #27ae60;">→ Banking clients receive dramatically more value. This justifies premium pricing. This increases client retention.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("#### Value to Diebold Nixdorf")
    st.markdown("""
    <div class="dn-value">
    <h4 style="color: #003366; margin-top: 0;">What This Means for DN's Business</h4>
    
    | Impact Area | Specific Value | Estimated Impact |
    |-------------|---------------|-----------------|
    | **New Revenue** | Premium analytics tier sold to 35–50 banking clients | $840K–$3M/year ARR |
    | **Data Monetization** | Sell anonymized benchmarking data as a product | $500K–$1M/year |
    | **Client Retention** | AI analytics makes clients stickier — harder to switch to NCR | 5% churn reduction = $125M protected |
    | **RFP Win Rate** | AI-generated proposals (Year 2) win more contracts | 10–20% improvement |
    | **Operational Savings** | Eliminate manual reporting, Alteryx, redundant tools | $500K–$850K/year by Year 2 |
    | **Cash Management** | AI prediction reduces emergency ATM cash replenishment | $1M+/year at scale |
    | **Competitive Position** | First ATM company with AI-powered call analytics | Unassailable first-mover advantage |
    | **Speed to Market** | New features shipped in days, not quarters | 10x faster product iteration |
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

st.markdown("## 📊 Three-Year Value Summary")

fig_summary = go.Figure()
years = ["Year 1", "Year 2", "Year 3"]
revenue = [300, 1300, 2750]
savings = [300, 600, 850]
risk_avoided = [200, 500, 1000]

fig_summary.add_trace(go.Bar(name="New Revenue ($K)", x=years, y=revenue, marker_color="#27ae60"))
fig_summary.add_trace(go.Bar(name="Cost Savings ($K)", x=years, y=savings, marker_color="#29B5E8"))
fig_summary.add_trace(go.Bar(name="Risk Mitigated ($K)", x=years, y=risk_avoided, marker_color="#e74c3c", marker_opacity=0.7))

fig_summary.add_trace(go.Scatter(
    x=years, y=[r+s+ra for r, s, ra in zip(revenue, savings, risk_avoided)],
    name="Total Value ($K)", line=dict(color="#003366", width=3), mode="lines+markers+text",
    text=[f"${r+s+ra:,}K" for r, s, ra in zip(revenue, savings, risk_avoided)],
    textposition="top center", textfont=dict(size=14, color="#003366")
))

fig_summary.update_layout(
    title="Total Business Value Created with Snowflake",
    barmode="stack", template="plotly_white", height=400,
    yaxis_title="$ Thousands", font=dict(family="Inter"),
    legend=dict(orientation="h", yanchor="bottom", y=-0.2)
)
st.plotly_chart(fig_summary, use_container_width=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Year 1 Total Value", "$800K", "Revenue + Savings + Risk")
with col2:
    st.metric("Year 2 Total Value", "$2.4M", "+200% growth")
with col3:
    st.metric("Year 3 Total Value", "$4.6M", "Platform at scale")

st.markdown("""
<div class="footer-bar">
<h3 style="margin: 0;">Snowflake Doesn't Just Modernize IT — It Transforms the Business</h3>
<p style="margin: 0.5rem 0 0 0; opacity: 0.8;">New revenue streams · Lower costs · Reduced risk · Competitive differentiation<br>
The question isn't whether DN can afford to invest in Snowflake. It's whether DN can afford not to.</p>
</div>
""", unsafe_allow_html=True)

render_section_notes("bv_revenue", "Revenue Impact")
render_section_notes("bv_cost", "Cost Savings")
render_section_notes("bv_risk", "Risk Mitigation")
render_section_notes("bv_outcomes", "Business Outcomes")
render_section_notes("bv_general", "General Notes — Business Value Analysis")
