import streamlit as st
import time

st.set_page_config(page_title="Stakeholder Briefing | Diebold Nixdorf", page_icon="🎬", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    .stApp {font-family: 'Inter', sans-serif;}
    .dn-header {background: linear-gradient(135deg, #003366 0%, #004d99 50%, #29B5E8 100%); padding: 2.5rem 2rem; border-radius: 0 0 20px 20px; margin: -1rem -1rem 2rem -1rem; text-align: center;}
    .dn-title {font-size: 2.4rem; font-weight: 800; color: white; margin: 0;}
    .dn-subtitle {font-size: 1rem; color: #b3d9ff; margin-top: 0.5rem;}
    .personal-greeting {font-size: 1.2rem; color: #333; text-align: center; margin-bottom: 2rem;}
    .slide-container {background: white; padding: 3rem; border-radius: 16px; min-height: 400px; display: flex; flex-direction: column; justify-content: center; box-shadow: 0 4px 20px rgba(0,0,0,0.08); border-top: 4px solid #29B5E8;}
    .slide-title {font-size: 1.8rem; font-weight: 700; color: #003366; margin-bottom: 1rem;}
    .slide-content {font-size: 1.05rem; color: #333; line-height: 1.8;}
    .narrator-box {background: #f0f7ff; padding: 1.5rem; border-radius: 10px; border-left: 4px solid #003366; margin-top: 1rem; font-style: italic; color: #003366;}
    .role-card {background: linear-gradient(135deg, #003366 0%, #004d99 100%); padding: 2rem; border-radius: 12px; border: 1px solid #29B5E8; margin: 1rem 0; color: white;}
    .role-name {font-size: 1.5rem; font-weight: 700; color: white;}
    .role-title {font-size: 0.95rem; color: #b3d9ff;}
    .wiifm {font-size: 1.2rem; color: #29B5E8; font-weight: 600; margin: 1rem 0;}
    .cta-box {background: linear-gradient(135deg, #003366 0%, #29B5E8 100%); padding: 2rem; border-radius: 12px; text-align: center; margin: 2rem 0; color: white;}
    .engagement-ref {background: #f0f7ff; padding: 1rem 1.5rem; border-radius: 8px; border-left: 3px solid #003366; margin: 0.5rem 0; font-size: 0.9rem; color: #003366;}
    .section-divider {height: 2px; background: linear-gradient(90deg, #003366, #29B5E8, #003366); margin: 2rem 0; border-radius: 2px; opacity: 0.2;}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="dn-header">
    <div class="dn-title">A Personal Message for DN Leadership</div>
    <div class="dn-subtitle">Tailored for Bruce Diesel · Tanya Gill · Michael Engel<br>From the Snowflake team working with Kirubel Legasion</div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

stakeholder = st.selectbox(
    "Select your personalized message:",
    ["All Stakeholders — Opening Message",
     "Bruce Diesel — Director, Product Management",
     "Tanya Gill — Global Director, Security Architecture",
     "Michael Engel — VP Software, Managed Services & R&D",
     "All Stakeholders — Closing & Next Steps"]
)

if stakeholder == "All Stakeholders — Opening Message":
    st.markdown("""
    <div class="slide-container">
        <div class="slide-title">Thank you for your time, Bruce, Tanya, and Michael.</div>
        <div class="slide-content">
            <p>We know your calendars are full and your teams are managing competing priorities. That's exactly why we're reaching out.</p>
            <br>
            <p>Kirubel Legasion and his team have been evaluating Snowflake for the ATM AI Assist initiative — and what they've found is that <strong>Snowflake doesn't add to your priority list. It consolidates it.</strong></p>
            <br>
            <p>This brief message is tailored to each of your roles. We want to answer one question:</p>
            <br>
            <p style="font-size: 1.4rem; color: #29B5E8; font-weight: 700; text-align: center;">"What does Snowflake mean for ME and MY team?"</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="narrator-box">
        <strong>🎙️ Narration:</strong> "We're not here to pitch another tool. We're here because your Chief Architect identified that 
        Snowflake can fundamentally simplify your data infrastructure while unlocking AI capabilities that don't exist in your current stack. 
        Let us show you what that means for each of your domains."
    </div>
    """, unsafe_allow_html=True)

elif stakeholder == "Bruce Diesel — Director, Product Management":
    st.markdown("""
    <div class="role-card">
        <div class="role-name">Bruce Diesel</div>
        <div class="role-title">Director of Product Management, Branch and Cash Automation</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="slide-container">
        <div class="slide-title">Bruce — Ship Smarter Products, Faster</div>
        <div class="slide-content">
            <p class="wiifm">What's In It For You:</p>
            <br>
            <p><strong>1. AI becomes a product feature, not a project.</strong></p>
            <p>Today, adding AI to ATM products requires months of infrastructure work. With Snowflake Cortex AI, your product team can embed intelligence — anomaly detection, predictive cash management, natural language interfaces — directly into products in <strong>days, not quarters</strong>.</p>
            <br>
            <p><strong>2. Customer-facing analytics as a differentiator.</strong></p>
            <p>Imagine offering each banking client their own AI-powered dashboard showing ATM performance, transaction patterns, and predictive insights — all from a single platform. That's Streamlit + Secure Data Sharing. It turns data into a <strong>product feature that sells.</strong></p>
            <br>
            <p><strong>3. Competitive moat against IBM WatsonX.</strong></p>
            <p>IBM is approaching your teams with AI solutions. Snowflake gives you AI that's <strong>integrated with your actual transaction data</strong> — not a separate system that requires complex integration. Your product roadmap stays in YOUR control.</p>
            <br>
            <p><strong>4. Reduce dependency on engineering for insights.</strong></p>
            <p>Cortex Analyst lets product managers query data in plain English. No SQL needed. Your team can validate product hypotheses in minutes, not sprint cycles.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="narrator-box">
        <strong>🎙️ Narration:</strong> "Bruce, your job is to ship products that win in the market. Every week you wait, IBM gets closer to locking in your competitors with WatsonX. 
        Snowflake lets you ship AI-powered product features at the speed of a startup — but with enterprise-grade security and scale. 
        The pilot is funded. Kirubel is ready. We just need your green light to start putting AI into your customers' hands."
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### Key Metrics That Matter to Product Management")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Feature Delivery", "10x Faster", "AI features")
    with col2:
        st.metric("Customer Analytics", "Self-Service", "Per-bank dashboards")
    with col3:
        st.metric("Product Differentiation", "AI-Native", "vs. competitors")
    with col4:
        st.metric("Data-to-Insight", "Minutes", "Not weeks")

elif stakeholder == "Tanya Gill — Global Director, Security Architecture":
    st.markdown("""
    <div class="role-card">
        <div class="role-name">Tanya Gill</div>
        <div class="role-title">Global Director, Security Architecture and Engineering</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="slide-container">
        <div class="slide-title">Tanya — Unified Security. Zero Compromise.</div>
        <div class="slide-content">
            <p class="wiifm">What's In It For You:</p>
            <br>
            <p><strong>1. Reduce your attack surface by consolidating data stores.</strong></p>
            <p>Today you're securing Oracle DB, SERAS warehouse, Loki, shared file locations, and multiple BI tools — each with their own access controls, vulnerabilities, and audit requirements. Snowflake consolidates these into <strong>one platform with one security model.</strong></p>
            <br>
            <p><strong>2. Enterprise-grade security built in, not bolted on.</strong></p>
            <ul style="margin-left: 1.5rem;">
                <li>End-to-end encryption (at rest + in transit + in use)</li>
                <li>Row-level security for multi-tenant data isolation</li>
                <li>Dynamic data masking (PII, PCI data automatically protected)</li>
                <li>Network policies and private connectivity (PrivateLink)</li>
                <li>SOC 2 Type II, HIPAA, PCI-DSS, FedRAMP compliant</li>
                <li>Complete audit trail — every query, every access, logged</li>
            </ul>
            <br>
            <p><strong>3. AI-powered threat detection on ATM telemetry.</strong></p>
            <p>Cortex AI can analyze transaction patterns and sensor data in real-time to detect tampering, skimming, and fraud — <strong>before damage is done</strong>. This is security that gets smarter over time.</p>
            <br>
            <p><strong>4. Eliminate CSV file transfers (your biggest data leak risk).</strong></p>
            <p>Those ATM Balancing Reports moving through shared file locations? That's uncontrolled data in motion. Snowflake replaces that with automated, encrypted, audited data flows.</p>
            <br>
            <p><strong>5. Governance that scales to 80 countries.</strong></p>
            <p>Tag-based policies, data classification, and role-based access that work globally. Set once, enforce everywhere.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="narrator-box">
        <strong>🎙️ Narration:</strong> "Tanya, I know security architecture means thinking about risk before thinking about features. 
        So here's the security case: today you have 5+ separate systems to secure, CSV files floating through shared drives, 
        and no unified audit trail. Snowflake doesn't just maintain your security posture — it dramatically improves it by reducing 
        complexity. Fewer systems = fewer vulnerabilities = better compliance. And the AI capabilities? They're your ally — 
        detecting threats that manual monitoring would miss."
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### Security Architecture Impact")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Systems to Secure", "5+ → 1", "Reduced attack surface")
    with col2:
        st.metric("Compliance", "Built-in", "SOC2, PCI, HIPAA")
    with col3:
        st.metric("Data Leak Risk", "Eliminated", "No more CSV transfers")
    with col4:
        st.metric("Audit Trail", "Complete", "Every access logged")

elif stakeholder == "Michael Engel — VP Software, Managed Services & R&D":
    st.markdown("""
    <div class="role-card">
        <div class="role-name">Michael Engel</div>
        <div class="role-title">VP Software, Managed Services and R&D</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="slide-container">
        <div class="slide-title">Michael — Less Maintenance, More Innovation</div>
        <div class="slide-content">
            <p class="wiifm">What's In It For You:</p>
            <br>
            <p><strong>1. Eliminate the infrastructure tax on your R&D team.</strong></p>
            <p>Your engineers are spending cycles maintaining Oracle, managing SERAS, debugging Loki scaling issues, and building custom ETL. 
            Snowflake is fully managed — <strong>zero infrastructure to maintain</strong>. Your team gets those cycles back for innovation.</p>
            <br>
            <p><strong>2. AI without an AI team.</strong></p>
            <p>Cortex AI gives your developers pre-built AI functions (NLP, anomaly detection, summarization, translation) callable with a single SQL function. 
            No ML engineers needed. No model training. No GPU management. <strong>AI becomes a feature call, not a team.</strong></p>
            <br>
            <p><strong>3. Managed Services becomes AI-powered.</strong></p>
            <p>Imagine managed services that predict issues before they happen, auto-resolve common problems, and provide customers 
            with AI-powered self-service. That's the future Snowflake enables — <strong>higher margins, fewer tickets, happier customers.</strong></p>
            <br>
            <p><strong>4. Cost structure that scales with value, not headcount.</strong></p>
            <p>Pay-per-query pricing means you're not paying for idle infrastructure. Scale to zero when not in use. 
            Scale massively during peak loads. <strong>Your cloud bill reflects actual business value delivered.</strong></p>
            <br>
            <p><strong>5. Kirubel's team is already aligned.</strong></p>
            <p>Your Chief Architect has evaluated the technology and is ready to execute. The pilot is scoped for 8 weeks. 
            Snowflake is investing $10K in credits + Professional Services at no cost. <strong>The risk is near zero. The upside is transformational.</strong></p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="narrator-box">
        <strong>🎙️ Narration:</strong> "Michael, as VP of Software and R&D, you're responsible for both keeping the lights on AND driving innovation. 
        Today, those are competing priorities — maintenance consumes cycles that should go to R&D. Snowflake flips that equation. 
        By consolidating 5+ data systems into one fully-managed platform, you give your team back hundreds of engineering hours per quarter. 
        And with Cortex AI, adding intelligence to products becomes a function call, not a project. Kirubel has already done the technical evaluation. 
        He needs your support to launch a pilot that could fundamentally transform how your team delivers value."
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### R&D and Managed Services Impact")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Engineering Time Freed", "30-40%", "From maintenance → innovation")
    with col2:
        st.metric("AI Development", "10x Faster", "Cortex AI functions")
    with col3:
        st.metric("Infrastructure Cost", "-40-60%", "Pay-per-use model")
    with col4:
        st.metric("Pilot Risk", "Near Zero", "$10K funded + PS support")

elif stakeholder == "All Stakeholders — Closing & Next Steps":
    st.markdown("""
    <div class="slide-container">
        <div class="slide-title">The Ask Is Simple</div>
        <div class="slide-content">
            <p style="font-size: 1.3rem; text-align: center; margin: 2rem 0;">
                We're not asking you to commit to a multi-year transformation today.
            </p>
            <p style="font-size: 1.3rem; text-align: center; margin: 2rem 0;">
                We're asking for <strong style="color: #29B5E8;">8 weeks</strong> to prove value with a funded pilot.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        ### What's Already Done ✅
        - Technical evaluation complete (Kirubel)
        - Architecture designed
        - $10K evaluation credits approved
        - PS workshop funded (no cost)
        - 3-5 banking clients identified for pilot
        """)
    with col2:
        st.markdown("""
        ### What We Need From You
        - **Bruce**: Product alignment for pilot scope
        - **Tanya**: Security review sign-off
        - **Michael**: Resource allocation (Kirubel's team)
        - **Timeline**: 30-minute alignment call
        """)
    with col3:
        st.markdown("""
        ### What You Get in 8 Weeks
        - Live AI on ATM transaction data
        - Multi-tenant customer dashboard
        - Proof of consolidation value
        - Clear ROI for Phase 2 decision
        - Zero risk (funded by Snowflake)
        """)
    
    st.markdown("""
    <div class="cta-box">
        <h2 style="color: white; margin: 0;">Ready to align?</h2>
        <p style="color: #e0e0e0; font-size: 1.2rem;">Let's schedule a 30-minute call with Bruce, Tanya, Michael, and Kirubel to kick off the pilot.</p>
        <p style="color: #29B5E8; font-size: 1rem;">Contact: Your Snowflake Account Team</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="narrator-box">
        <strong>🎙️ Narration:</strong> "Bruce, Tanya, Michael — thank you for taking the time to review this. We know you're busy. 
        That's why we've done the homework. The technology is proven. The pilot is funded. Kirubel is ready. 
        All we need is your alignment to move forward. Let's schedule 30 minutes together and we'll show you exactly 
        what the first 8 weeks look like. No risk, maximum learning, and a clear decision point at the end. We look forward to connecting."
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.caption("Personal briefing prepared by Snowflake for Diebold Nixdorf Leadership | May 2026")
