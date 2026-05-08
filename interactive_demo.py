import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import time

st.set_page_config(page_title="ATM Audio Intelligence | Snowflake Demo", page_icon="❄️", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    .stApp {font-family: 'Inter', sans-serif;}
    .demo-header {background: linear-gradient(135deg, #003366 0%, #004d99 50%, #29B5E8 100%); padding: 2.5rem 2rem; border-radius: 0 0 20px 20px; margin: -1rem -1rem 2rem -1rem; text-align: center;}
    .demo-title {font-size: 2.4rem; font-weight: 800; color: white; margin: 0;}
    .demo-subtitle {font-size: 1rem; color: #b3d9ff; margin-top: 0.5rem;}
    .kpi-row {display: flex; gap: 1rem; margin: 1rem 0;}
    .call-card {background: white; padding: 1.2rem; border-radius: 12px; border-left: 4px solid #29B5E8; box-shadow: 0 2px 8px rgba(0,0,0,0.05); margin: 0.6rem 0;}
    .call-card-negative {background: white; padding: 1.2rem; border-radius: 12px; border-left: 4px solid #e74c3c; box-shadow: 0 2px 8px rgba(0,0,0,0.05); margin: 0.6rem 0;}
    .sentiment-positive {color: #27ae60; font-weight: 600;}
    .sentiment-negative {color: #e74c3c; font-weight: 600;}
    .sentiment-neutral {color: #f39c12; font-weight: 600;}
    .ai-insight {background: linear-gradient(135deg, #f0f7ff 0%, #e8f4fd 100%); padding: 1.5rem; border-radius: 12px; border: 1px solid #29B5E820; margin: 1rem 0;}
    .demo-badge {background: #003366; color: white; padding: 3px 10px; border-radius: 12px; font-size: 0.75rem; font-weight: 600; letter-spacing: 0.5px;}
    .section-divider {height: 2px; background: linear-gradient(90deg, #003366, #29B5E8, #003366); margin: 2rem 0; border-radius: 2px; opacity: 0.2;}
    .multi-tenant-banner {background: #003366; color: white; padding: 0.8rem 1.5rem; border-radius: 8px; font-size: 0.9rem; margin: 1rem 0;}
    .transcript-box {background: #f8f9fa; padding: 1.5rem; border-radius: 10px; border: 1px solid #e0e0e0; font-family: monospace; font-size: 0.85rem; line-height: 1.8; max-height: 300px; overflow-y: auto;}
    .cortex-label {background: #29B5E8; color: white; padding: 2px 8px; border-radius: 4px; font-size: 0.7rem; font-weight: 600; margin-left: 0.5rem;}
</style>
""", unsafe_allow_html=True)

np.random.seed(42)

@st.cache_data
def generate_call_data():
    banks = ["JPMorgan Chase", "Bank of America", "Wells Fargo", "Citibank", "US Bank"]
    call_types = ["Balance Inquiry", "Withdrawal Assistance", "Deposit Help", "Account Transfer", "Card Issue", "General Inquiry"]
    sentiments = ["Positive", "Positive", "Positive", "Neutral", "Neutral", "Negative"]
    resolutions = ["Resolved - First Contact", "Resolved - Escalation", "Unresolved - Callback Required", "Resolved - First Contact", "Resolved - First Contact"]
    cities = ["New York", "Chicago", "Los Angeles", "Houston", "Phoenix", "Philadelphia", "Dallas", "Atlanta", "Miami", "Denver"]
    
    calls = []
    now = datetime.now()
    for i in range(500):
        ts = now - timedelta(minutes=random.randint(0, 1440*7))
        duration = round(np.random.lognormal(4.5, 0.6))
        sentiment = random.choice(sentiments)
        calls.append({
            "call_id": f"TA-{str(10000+i)}",
            "timestamp": ts,
            "bank_client": random.choice(banks),
            "atm_id": f"DN-ATM-{str(random.randint(1001, 1200)).zfill(4)}",
            "city": random.choice(cities),
            "call_type": random.choice(call_types),
            "duration_sec": min(duration, 900),
            "sentiment": sentiment,
            "sentiment_score": round(np.random.uniform(0.7, 0.95) if sentiment == "Positive" else np.random.uniform(0.3, 0.5) if sentiment == "Negative" else np.random.uniform(0.45, 0.65), 2),
            "resolution": random.choice(resolutions),
            "teller_id": f"T-{random.randint(100, 150)}",
            "language": random.choices(["English", "Spanish", "Mandarin", "French"], weights=[70, 15, 10, 5])[0],
            "wait_time_sec": int(np.random.exponential(30)),
            "customer_effort_score": round(np.random.uniform(1, 5), 1),
            "topics_detected": random.sample(["PIN reset", "balance check", "card replacement", "transfer help", "receipt request", "account lock", "fraud report", "deposit issue"], k=random.randint(1, 3)),
            "anomaly_flag": random.random() < 0.04,
            "coaching_opportunity": random.random() < 0.15
        })
    return pd.DataFrame(calls).sort_values("timestamp", ascending=False).reset_index(drop=True)

@st.cache_data
def generate_hourly_calls():
    hours = list(range(24))
    base = [8, 5, 3, 2, 2, 4, 12, 35, 55, 48, 42, 45, 50, 44, 40, 42, 48, 52, 45, 38, 30, 22, 15, 10]
    return pd.DataFrame({"hour": hours, "calls": [b + int(np.random.uniform(-5, 5)) for b in base]})

calls_df = generate_call_data()
hourly_df = generate_hourly_calls()

st.markdown("""
<div class="demo-header">
    <div class="demo-title">❄️ ATM Audio Intelligence Platform</div>
    <div class="demo-subtitle">Transaction Assist Analytics · Powered by Snowflake Cortex AI<br>
    <span style="opacity: 0.7;">Kafka → Snowflake → Cortex AI → Multi-Tenant Banking Client Dashboards</span></div>
</div>
""", unsafe_allow_html=True)

bank_filter = st.selectbox("🏦 **Banking Client View** (Secure Data Sharing — Each bank sees only their data)", 
    ["All Banks (Diebold Nixdorf Admin)", "JPMorgan Chase", "Bank of America", "Wells Fargo", "Citibank", "US Bank"])

if bank_filter != "All Banks (Diebold Nixdorf Admin)":
    filtered_df = calls_df[calls_df["bank_client"] == bank_filter]
    st.markdown(f'<div class="multi-tenant-banner">🔒 Secure Data Sharing Active — Showing only <strong>{bank_filter}</strong> ATM call data. Other bank data is cryptographically isolated via Snowflake row-level security.</div>', unsafe_allow_html=True)
else:
    filtered_df = calls_df

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📞 Live Call Analytics",
    "🧠 Cortex AI Insights",
    "💬 Ask Questions (Cortex Analyst)",
    "📊 Teller Performance",
    "🏦 Banking Client Reports"
])

with tab1:
    col1, col2, col3, col4, col5 = st.columns(5)
    total_calls = len(filtered_df)
    avg_duration = filtered_df["duration_sec"].mean()
    positive_pct = len(filtered_df[filtered_df["sentiment"] == "Positive"]) / total_calls * 100
    resolved_pct = len(filtered_df[filtered_df["resolution"].str.contains("Resolved")]) / total_calls * 100
    avg_wait = filtered_df["wait_time_sec"].mean()
    
    with col1:
        st.metric("Total Calls (7d)", f"{total_calls:,}", "+12% vs last week")
    with col2:
        st.metric("Avg Duration", f"{avg_duration:.0f}s", "-8s vs target")
    with col3:
        st.metric("Positive Sentiment", f"{positive_pct:.0f}%", "+3% improvement")
    with col4:
        st.metric("First Contact Resolution", f"{resolved_pct:.0f}%", "Above 85% target")
    with col5:
        st.metric("Avg Wait Time", f"{avg_wait:.0f}s", "Below 45s SLA")
    
    st.markdown("### Call Volume — Real-Time (Today)")
    fig_hourly = go.Figure()
    fig_hourly.add_trace(go.Bar(x=hourly_df["hour"], y=hourly_df["calls"], marker_color="#29B5E8", name="Calls"))
    fig_hourly.add_hline(y=40, line_dash="dash", line_color="#e74c3c", annotation_text="Staffing Threshold")
    fig_hourly.update_layout(template="plotly_white", height=280, xaxis_title="Hour of Day", yaxis_title="Call Volume", font=dict(family="Inter"), margin=dict(t=30))
    st.plotly_chart(fig_hourly, use_container_width=True)
    
    col_l, col_r = st.columns([1, 1])
    with col_l:
        st.markdown("### Call Type Distribution")
        type_counts = filtered_df["call_type"].value_counts()
        fig_types = px.pie(values=type_counts.values, names=type_counts.index, hole=0.4, color_discrete_sequence=["#003366", "#29B5E8", "#66ccff", "#004d99", "#0077b6", "#48cae4"])
        fig_types.update_layout(template="plotly_white", height=300, font=dict(family="Inter"))
        st.plotly_chart(fig_types, use_container_width=True)
    
    with col_r:
        st.markdown("### Sentiment Trend (7 Days)")
        daily = filtered_df.copy()
        daily["date"] = daily["timestamp"].dt.date
        sentiment_daily = daily.groupby(["date", "sentiment"]).size().reset_index(name="count")
        fig_sent = px.area(sentiment_daily, x="date", y="count", color="sentiment", color_discrete_map={"Positive": "#27ae60", "Neutral": "#f39c12", "Negative": "#e74c3c"})
        fig_sent.update_layout(template="plotly_white", height=300, font=dict(family="Inter"))
        st.plotly_chart(fig_sent, use_container_width=True)

with tab2:
    st.markdown("### 🧠 Cortex AI — Real-Time Intelligence on ATM Calls")
    st.markdown("""
    <div class="ai-insight">
    <strong>How it works:</strong> Every ATM call streams through Kafka into Snowflake in sub-second latency. 
    Cortex AI automatically processes each call record — analyzing sentiment, detecting topics, classifying issues, 
    and identifying coaching opportunities. No separate ML infrastructure. No model training. Built into the platform.
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    anomalies = filtered_df[filtered_df["anomaly_flag"] == True]
    coaching = filtered_df[filtered_df["coaching_opportunity"] == True]
    negative = filtered_df[filtered_df["sentiment"] == "Negative"]
    
    with col1:
        st.metric("🚨 Anomalies Detected", len(anomalies), "AI-flagged patterns")
    with col2:
        st.metric("📚 Coaching Opportunities", len(coaching), "Teller improvement")
    with col3:
        st.metric("😠 Negative Sentiment Calls", len(negative), "Requires review")
    
    st.markdown("---")
    st.markdown("### AI-Detected Insights (Last 24 Hours)")
    
    insights = [
        {"type": "🚨 Anomaly", "detail": "Unusual spike in card issue calls from ATM DN-ATM-1045 (Philadelphia) — potential card reader malfunction", "action": "Dispatch maintenance team", "confidence": "94%"},
        {"type": "📊 Pattern", "detail": "Spanish-language calls increased 40% week-over-week in Houston/Phoenix markets — staffing gap for bilingual tellers", "action": "Increase bilingual teller allocation", "confidence": "91%"},
        {"type": "😠 Escalation Risk", "detail": "3 consecutive negative sentiment calls from Teller T-127 (avg call time 2x above normal) — possible training need", "action": "Schedule supervisor review", "confidence": "88%"},
        {"type": "⚡ Efficiency", "detail": "Balance inquiry calls averaging 180s — should be <90s. Cortex AI recommends adding IVR pre-screen for simple lookups", "action": "Implement IVR filter", "confidence": "92%"},
        {"type": "🔒 Security", "detail": "Call from ATM DN-ATM-1089 flagged: customer requested 3 rapid transfers to unfamiliar accounts — fraud pattern match", "action": "Flag for compliance review", "confidence": "96%"},
    ]
    
    for insight in insights:
        st.markdown(f"""
        <div class="call-card">
            <strong>{insight['type']}</strong> <span class="cortex-label">CORTEX AI</span> <span style="float: right; color: #666; font-size: 0.85rem;">Confidence: {insight['confidence']}</span>
            <br><span style="color: #333;">{insight['detail']}</span>
            <br><span style="color: #29B5E8; font-weight: 500;">→ Recommended Action: {insight['action']}</span>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### Sample Call Transcript + AI Analysis")
    
    st.markdown("""
    <div class="transcript-box">
    <strong>Call ID:</strong> TA-10042 | <strong>ATM:</strong> DN-ATM-1023 (Chicago) | <strong>Bank:</strong> JPMorgan Chase | <strong>Duration:</strong> 4:23<br><br>
    <strong>[00:00]</strong> Teller: "Thank you for calling Transaction Assist. How can I help you today?"<br>
    <strong>[00:05]</strong> Customer: "Hi, I'm trying to deposit a check but the machine keeps rejecting it."<br>
    <strong>[00:12]</strong> Teller: "I'm sorry to hear that. Let me help you with that. Can you tell me if the check is endorsed on the back?"<br>
    <strong>[00:20]</strong> Customer: "Oh... let me check. No, I don't think I signed it."<br>
    <strong>[00:25]</strong> Teller: "No problem! Please endorse the check — sign the back — and try inserting it again."<br>
    <strong>[00:35]</strong> Customer: "Okay, let me try... It worked! Thank you so much."<br>
    <strong>[00:40]</strong> Teller: "You're welcome! Is there anything else I can help with?"<br>
    <strong>[00:44]</strong> Customer: "No, that's all. Thank you!"<br>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("**Sentiment**")
        st.markdown('<span class="sentiment-positive">Positive (0.91)</span>', unsafe_allow_html=True)
    with col2:
        st.markdown("**Topics Detected**")
        st.markdown("`deposit issue` `check endorsement`")
    with col3:
        st.markdown("**Resolution**")
        st.markdown("✅ First Contact")
    with col4:
        st.markdown("**Coaching Flag**")
        st.markdown("None — excellent handling")

with tab3:
    st.markdown("### 💬 Ask Questions About Your ATM Call Data")
    st.markdown("*Powered by Cortex Analyst — Natural language queries on Transaction Assist data. No SQL required.*")
    
    sample_questions = [
        "Which ATMs have the longest average call times?",
        "Show me sentiment trends for Bank of America this week",
        "What are the top reasons customers call during peak hours?",
        "Which tellers need coaching based on sentiment scores?",
        "How many fraud-flagged calls happened in the last 7 days?",
        "Compare call resolution rates across banking clients"
    ]
    
    st.markdown("**Example questions:**")
    q_cols = st.columns(3)
    for i, q in enumerate(sample_questions):
        with q_cols[i % 3]:
            if st.button(q, key=f"q_{i}"):
                st.session_state["question"] = q
    
    user_q = st.text_input("Or type your own:", value=st.session_state.get("question", ""), placeholder="e.g., What's the average call duration by bank client?")
    
    if user_q:
        with st.spinner("Cortex Analyst generating answer..."):
            time.sleep(1)
        
        st.markdown('<div class="ai-insight">', unsafe_allow_html=True)
        st.markdown("**🤖 Cortex Analyst Response:**")
        
        if "longest" in user_q.lower() or "call time" in user_q.lower():
            atm_dur = filtered_df.groupby("atm_id")["duration_sec"].mean().sort_values(ascending=False).head(8).reset_index()
            atm_dur.columns = ["ATM ID", "Avg Duration (sec)"]
            st.dataframe(atm_dur, use_container_width=True, hide_index=True)
            st.markdown("**Insight:** ATMs with longest call times correlate with older hardware models that have more user-interface issues.")
            st.code("-- Generated SQL:\nSELECT atm_id, AVG(duration_sec) as avg_duration\nFROM transaction_assist.calls\nWHERE timestamp > DATEADD(day, -7, CURRENT_TIMESTAMP())\nGROUP BY atm_id\nORDER BY avg_duration DESC\nLIMIT 8;", language="sql")
        
        elif "sentiment" in user_q.lower() or "trend" in user_q.lower():
            daily = filtered_df.copy()
            daily["date"] = daily["timestamp"].dt.date
            sent_trend = daily.groupby("date")["sentiment_score"].mean().reset_index()
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=sent_trend["date"], y=sent_trend["sentiment_score"], line=dict(color="#29B5E8", width=3), fill="tozeroy", fillcolor="rgba(41,181,232,0.1)"))
            fig.update_layout(template="plotly_white", height=250, yaxis_title="Avg Sentiment Score", title="Sentiment Trend")
            st.plotly_chart(fig, use_container_width=True)
        
        elif "reason" in user_q.lower() or "why" in user_q.lower() or "top" in user_q.lower():
            type_counts = filtered_df["call_type"].value_counts().reset_index()
            type_counts.columns = ["Call Reason", "Count"]
            st.dataframe(type_counts, use_container_width=True, hide_index=True)
        
        elif "coaching" in user_q.lower() or "teller" in user_q.lower():
            teller_perf = filtered_df.groupby("teller_id").agg({"sentiment_score": "mean", "duration_sec": "mean", "call_id": "count"}).reset_index()
            teller_perf.columns = ["Teller", "Avg Sentiment", "Avg Duration (s)", "Total Calls"]
            needs_coaching = teller_perf[teller_perf["Avg Sentiment"] < 0.55].sort_values("Avg Sentiment")
            st.markdown(f"**{len(needs_coaching)} tellers** below sentiment threshold (0.55):")
            st.dataframe(needs_coaching, use_container_width=True, hide_index=True)
        
        elif "fraud" in user_q.lower() or "anomal" in user_q.lower():
            fraud_calls = filtered_df[filtered_df["anomaly_flag"] == True][["call_id", "timestamp", "atm_id", "bank_client", "city", "call_type"]].head(10)
            st.markdown(f"**{len(filtered_df[filtered_df['anomaly_flag']])} fraud-flagged calls** in the last 7 days:")
            st.dataframe(fraud_calls, use_container_width=True, hide_index=True)
        
        elif "resolution" in user_q.lower() or "compare" in user_q.lower():
            res_by_bank = filtered_df.groupby("bank_client").apply(lambda x: (x["resolution"].str.contains("Resolved")).sum() / len(x) * 100).reset_index()
            res_by_bank.columns = ["Bank Client", "Resolution Rate %"]
            fig = px.bar(res_by_bank.sort_values("Resolution Rate %", ascending=False), x="Bank Client", y="Resolution Rate %", color="Resolution Rate %", color_continuous_scale=["#e74c3c", "#f39c12", "#27ae60"])
            fig.update_layout(template="plotly_white", height=300)
            st.plotly_chart(fig, use_container_width=True)
        
        else:
            avg_dur = filtered_df.groupby("bank_client")["duration_sec"].mean().reset_index()
            avg_dur.columns = ["Bank Client", "Avg Duration (sec)"]
            st.dataframe(avg_dur.sort_values("Avg Duration (sec)", ascending=False), use_container_width=True, hide_index=True)
        
        st.markdown('</div>', unsafe_allow_html=True)

with tab4:
    st.markdown("### 📊 Remote Teller Performance Analytics")
    st.markdown("*Cortex AI automatically scores teller performance based on sentiment, resolution rate, and call efficiency.*")
    
    teller_stats = filtered_df.groupby("teller_id").agg({
        "call_id": "count",
        "sentiment_score": "mean",
        "duration_sec": "mean",
        "coaching_opportunity": "sum"
    }).reset_index()
    teller_stats.columns = ["Teller ID", "Total Calls", "Avg Sentiment", "Avg Duration (s)", "Coaching Flags"]
    teller_stats["Performance Score"] = ((teller_stats["Avg Sentiment"] * 50) + (1 - teller_stats["Avg Duration (s)"] / teller_stats["Avg Duration (s)"].max()) * 30 + (1 - teller_stats["Coaching Flags"] / max(teller_stats["Coaching Flags"].max(), 1)) * 20).round(1)
    teller_stats = teller_stats.sort_values("Performance Score", ascending=False)
    
    col1, col2 = st.columns([2, 1])
    with col1:
        fig_perf = px.scatter(teller_stats, x="Avg Duration (s)", y="Avg Sentiment", size="Total Calls", color="Performance Score",
                              color_continuous_scale=["#e74c3c", "#f39c12", "#27ae60"], hover_name="Teller ID",
                              title="Teller Performance Map (size = call volume)")
        fig_perf.update_layout(template="plotly_white", height=400, font=dict(family="Inter"))
        st.plotly_chart(fig_perf, use_container_width=True)
    
    with col2:
        st.markdown("#### Top Performers")
        st.dataframe(teller_stats.head(5)[["Teller ID", "Total Calls", "Avg Sentiment", "Performance Score"]], use_container_width=True, hide_index=True)
        st.markdown("#### Needs Coaching")
        st.dataframe(teller_stats.tail(3)[["Teller ID", "Total Calls", "Avg Sentiment", "Coaching Flags"]], use_container_width=True, hide_index=True)
    
    st.markdown("""
    <div class="ai-insight">
    <strong>💡 Cortex AI Staffing Recommendation:</strong> Based on call volume patterns and language distribution, 
    add 2 bilingual (Spanish) tellers during 5–7 PM shift for Houston/Phoenix ATMs. 
    Estimated impact: 25% reduction in wait time for Spanish-speaking customers.
    </div>
    """, unsafe_allow_html=True)

with tab5:
    st.markdown("### 🏦 Banking Client Reporting (Multi-Tenant)")
    st.markdown("*Each banking client receives their own secure analytics dashboard. This is what Snowflake Secure Data Sharing enables — one platform, 50+ clients, zero data leakage.*")
    
    bank_summary = filtered_df.groupby("bank_client").agg({
        "call_id": "count",
        "duration_sec": "mean",
        "sentiment_score": "mean",
        "wait_time_sec": "mean",
        "anomaly_flag": "sum"
    }).reset_index()
    bank_summary.columns = ["Bank Client", "Total Calls", "Avg Duration (s)", "Avg Sentiment", "Avg Wait (s)", "Security Alerts"]
    bank_summary = bank_summary.sort_values("Total Calls", ascending=False)
    
    st.dataframe(bank_summary, use_container_width=True, hide_index=True)
    
    col1, col2 = st.columns(2)
    with col1:
        fig_bank = px.bar(bank_summary, x="Bank Client", y="Total Calls", color="Avg Sentiment", 
                          color_continuous_scale=["#e74c3c", "#f39c12", "#27ae60"], title="Call Volume by Bank Client")
        fig_bank.update_layout(template="plotly_white", height=300, font=dict(family="Inter"))
        st.plotly_chart(fig_bank, use_container_width=True)
    
    with col2:
        fig_bench = go.Figure()
        fig_bench.add_trace(go.Bar(name="This Client", x=["Avg Duration", "Sentiment", "Resolution %", "Wait Time"], y=[135, 0.72, 87, 28], marker_color="#29B5E8"))
        fig_bench.add_trace(go.Bar(name="Industry Benchmark", x=["Avg Duration", "Sentiment", "Resolution %", "Wait Time"], y=[160, 0.65, 80, 35], marker_color="#003366"))
        fig_bench.update_layout(title="Client vs. Industry Benchmark (Anonymized)", template="plotly_white", height=300, barmode="group", font=dict(family="Inter"))
        st.plotly_chart(fig_bench, use_container_width=True)
    
    st.markdown("""
    <div class="ai-insight">
    <strong>💰 Revenue Model:</strong> This cross-client benchmarking is the premium analytics tier that Diebold Nixdorf 
    sells to banking clients. Today you deliver CSV exports. With Snowflake, you deliver AI-powered intelligence that 
    clients pay a premium for — creating a new recurring revenue stream.
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

st.markdown("""
<div style="background: linear-gradient(135deg, #003366 0%, #004d99 100%); padding: 2rem; border-radius: 16px; text-align: center; color: white;">
    <h3 style="margin: 0; color: white;">This Is What Transaction Assist Becomes with Snowflake</h3>
    <p style="margin: 0.5rem 0 0 0; opacity: 0.9;">Real-time call analytics · AI sentiment & classification · Natural language queries · Multi-tenant secure sharing · Premium analytics as revenue</p>
    <p style="margin: 1rem 0 0 0; opacity: 0.7; font-size: 0.9rem;">Architecture: Kafka (Zoom/Twilio) → Snowflake Kafka Connector → Dynamic Tables → Cortex AI → Streamlit/Power BI</p>
</div>
""", unsafe_allow_html=True)
