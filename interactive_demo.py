import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import time
from notes_utils import render_section_notes

st.set_page_config(page_title="Art of Possible | Snowflake Demo", page_icon="❄️", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    .stApp {font-family: 'Inter', sans-serif;}
    .demo-header {background: linear-gradient(135deg, #003366 0%, #004d99 50%, #29B5E8 100%); padding: 2.5rem 2rem; border-radius: 0 0 20px 20px; margin: -1rem -1rem 2rem -1rem; text-align: center;}
    .demo-title {font-size: 2.4rem; font-weight: 800; color: white; margin: 0;}
    .demo-subtitle {font-size: 1rem; color: #b3d9ff; margin-top: 0.5rem;}
    .call-card {background: white; padding: 1.2rem; border-radius: 12px; border-left: 4px solid #29B5E8; box-shadow: 0 2px 8px rgba(0,0,0,0.05); margin: 0.6rem 0;}
    .ai-insight {background: linear-gradient(135deg, #f0f7ff 0%, #e8f4fd 100%); padding: 1.5rem; border-radius: 12px; border: 1px solid #29B5E820; margin: 1rem 0;}
    .section-divider {height: 2px; background: linear-gradient(90deg, #003366, #29B5E8, #003366); margin: 2rem 0; border-radius: 2px; opacity: 0.2;}
    .multi-tenant-banner {background: #003366; color: white; padding: 0.8rem 1.5rem; border-radius: 8px; font-size: 0.9rem; margin: 1rem 0;}
    .transcript-box {background: #f8f9fa; padding: 1.5rem; border-radius: 10px; border: 1px solid #e0e0e0; font-family: monospace; font-size: 0.85rem; line-height: 1.8; max-height: 300px; overflow-y: auto;}
    .cortex-label {background: #29B5E8; color: white; padding: 2px 8px; border-radius: 4px; font-size: 0.7rem; font-weight: 600; margin-left: 0.5rem;}
    .si-chat-msg {background: white; padding: 1rem 1.5rem; border-radius: 12px; box-shadow: 0 1px 4px rgba(0,0,0,0.06); margin: 0.5rem 0; border-left: 3px solid #29B5E8;}
    .si-chat-user {background: #e8f4fd; padding: 1rem 1.5rem; border-radius: 12px; margin: 0.5rem 0; border-left: 3px solid #003366;}
    .summary-card {background: white; padding: 1.5rem; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.05); border-top: 3px solid #29B5E8; text-align: center;}
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
    teller_names = ["Maria S.", "James T.", "Priya K.", "Carlos R.", "Aisha M.", "David L.", "Sofia G.", "Wei C.", "Fatima H.", "Robert J."]
    calls = []
    now = datetime.now()
    for i in range(800):
        ts = now - timedelta(minutes=random.randint(0, 1440*14))
        duration = round(np.random.lognormal(4.5, 0.6))
        sentiment = random.choice(sentiments)
        bank = random.choice(banks)
        city = random.choice(cities)
        calls.append({
            "call_id": f"TA-{str(10000+i)}",
            "timestamp": ts,
            "date": ts.date(),
            "hour": ts.hour,
            "bank_client": bank,
            "atm_id": f"DN-ATM-{str(random.randint(1001, 1200)).zfill(4)}",
            "city": city,
            "state": {"New York": "NY", "Chicago": "IL", "Los Angeles": "CA", "Houston": "TX", "Phoenix": "AZ", "Philadelphia": "PA", "Dallas": "TX", "Atlanta": "GA", "Miami": "FL", "Denver": "CO"}[city],
            "call_type": random.choice(call_types),
            "duration_sec": min(duration, 900),
            "sentiment": sentiment,
            "sentiment_score": round(np.random.uniform(0.7, 0.98) if sentiment == "Positive" else np.random.uniform(0.2, 0.45) if sentiment == "Negative" else np.random.uniform(0.45, 0.65), 2),
            "resolution": random.choice(resolutions),
            "teller_name": random.choice(teller_names),
            "language": random.choices(["English", "Spanish", "Mandarin", "French"], weights=[70, 15, 10, 5])[0],
            "wait_time_sec": int(np.random.exponential(30)),
            "customer_effort_score": round(np.random.uniform(1, 5), 1),
            "topics_detected": ", ".join(random.sample(["PIN reset", "balance check", "card replacement", "transfer help", "receipt request", "account lock", "fraud report", "deposit issue", "fee dispute", "new account"], k=random.randint(1, 3))),
            "anomaly_flag": random.random() < 0.04,
            "coaching_opportunity": random.random() < 0.15,
            "cortex_summary": random.choice([
                "Customer needed help with a deposit. Teller resolved quickly with clear instructions.",
                "Card reader issue at ATM. Teller guided customer through alternative insertion method.",
                "Customer reported suspicious activity. Teller escalated to fraud team immediately.",
                "Balance inquiry — customer confused by pending transactions. Teller explained hold policy.",
                "Withdrawal assistance for visually impaired customer. Teller provided step-by-step audio guidance.",
                "Customer frustrated with wait time. Teller de-escalated and resolved account transfer.",
                "PIN reset requested. Teller verified identity and completed reset in under 2 minutes.",
                "Customer attempted multiple rapid transfers to unfamiliar accounts. Flagged for fraud review."
            ])
        })
    return pd.DataFrame(calls).sort_values("timestamp", ascending=False).reset_index(drop=True)

calls_df = generate_call_data()

st.markdown("""
<div class="demo-header">
    <div class="demo-title">❄️ Art of Possible — Interactive Demo</div>
    <div class="demo-subtitle">ATM Audio Intelligence Platform · Powered by Snowflake Cortex AI + Snowflake Intelligence<br>
    <span style="opacity: 0.7;">Experience what Transaction Assist analytics looks like with Snowflake</span></div>
</div>
""", unsafe_allow_html=True)

bank_filter = st.selectbox("🏦 **Banking Client View** (Secure Data Sharing — Each bank sees only their data)",
    ["All Banks (Diebold Nixdorf Admin)", "JPMorgan Chase", "Bank of America", "Wells Fargo", "Citibank", "US Bank"])

if bank_filter != "All Banks (Diebold Nixdorf Admin)":
    filtered_df = calls_df[calls_df["bank_client"] == bank_filter].copy()
    st.markdown(f'<div class="multi-tenant-banner">🔒 Secure Data Sharing Active — Showing only <strong>{bank_filter}</strong> ATM call data. Other bank data is cryptographically isolated via Snowflake row-level security.</div>', unsafe_allow_html=True)
else:
    filtered_df = calls_df.copy()

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "📞 Live Call Analytics",
    "🧠 Cortex AI Insights",
    "🔍 Snowflake Intelligence",
    "📊 Data Explorer",
    "📈 Teller Performance",
    "🏦 Banking Client Reports"
])

with tab1:
    col1, col2, col3, col4, col5 = st.columns(5)
    total_calls = len(filtered_df)
    avg_duration = filtered_df["duration_sec"].mean()
    positive_pct = len(filtered_df[filtered_df["sentiment"] == "Positive"]) / max(total_calls, 1) * 100
    resolved_pct = len(filtered_df[filtered_df["resolution"].str.contains("Resolved")]) / max(total_calls, 1) * 100
    avg_wait = filtered_df["wait_time_sec"].mean()
    with col1:
        st.metric("Total Calls (14d)", f"{total_calls:,}", "+12% vs prior period")
    with col2:
        st.metric("Avg Duration", f"{avg_duration:.0f}s", "-8s vs target")
    with col3:
        st.metric("Positive Sentiment", f"{positive_pct:.0f}%", "+3%")
    with col4:
        st.metric("First Contact Resolution", f"{resolved_pct:.0f}%", "Above 85% target")
    with col5:
        st.metric("Avg Wait Time", f"{avg_wait:.0f}s", "Below 45s SLA")

    col_chart, col_filters = st.columns([3, 1])
    with col_filters:
        st.markdown("#### Filters")
        date_range = st.date_input("Date range", value=(filtered_df["timestamp"].min().date(), filtered_df["timestamp"].max().date()), key="date_range_live")
        city_filter = st.multiselect("City", options=sorted(filtered_df["city"].unique()), default=[], key="city_live")
        type_filter = st.multiselect("Call Type", options=sorted(filtered_df["call_type"].unique()), default=[], key="type_live")

    view_df = filtered_df.copy()
    if len(date_range) == 2:
        view_df = view_df[(view_df["date"] >= date_range[0]) & (view_df["date"] <= date_range[1])]
    if city_filter:
        view_df = view_df[view_df["city"].isin(city_filter)]
    if type_filter:
        view_df = view_df[view_df["call_type"].isin(type_filter)]

    with col_chart:
        daily = view_df.groupby("date").size().reset_index(name="calls")
        fig_vol = px.area(daily, x="date", y="calls", title=f"Call Volume Over Time ({len(view_df):,} calls)", color_discrete_sequence=["#29B5E8"])
        fig_vol.update_layout(template="plotly_white", height=300, font=dict(family="Inter"))
        st.plotly_chart(fig_vol, use_container_width=True)

    col_a, col_b = st.columns(2)
    with col_a:
        type_counts = view_df["call_type"].value_counts().reset_index()
        type_counts.columns = ["Call Type", "Count"]
        fig_types = px.pie(type_counts, values="Count", names="Call Type", hole=0.4, color_discrete_sequence=["#003366", "#29B5E8", "#66ccff", "#004d99", "#0077b6", "#48cae4"], title="Call Type Distribution")
        fig_types.update_layout(template="plotly_white", height=320, font=dict(family="Inter"))
        st.plotly_chart(fig_types, use_container_width=True)
    with col_b:
        hourly = view_df.groupby("hour").size().reset_index(name="calls")
        fig_hr = px.bar(hourly, x="hour", y="calls", title="Calls by Hour of Day", color_discrete_sequence=["#29B5E8"])
        fig_hr.add_hline(y=hourly["calls"].quantile(0.85), line_dash="dash", line_color="#e74c3c", annotation_text="Peak Threshold")
        fig_hr.update_layout(template="plotly_white", height=320, font=dict(family="Inter"), xaxis_title="Hour")
        st.plotly_chart(fig_hr, use_container_width=True)

    st.markdown("#### Recent Calls (Live Feed)")
    st.dataframe(
        view_df.head(15)[["call_id", "timestamp", "bank_client", "city", "call_type", "duration_sec", "sentiment", "sentiment_score", "resolution", "teller_name"]],
        use_container_width=True, hide_index=True
    )

with tab2:
    st.markdown("### 🧠 Cortex AI — Real-Time Intelligence on ATM Calls")
    st.markdown("""
    <div class="ai-insight">
    <strong>How it works:</strong> Every ATM call streams through Kafka into Snowflake in sub-second latency.
    Cortex AI automatically processes each call — analyzing sentiment, detecting topics, classifying issues,
    summarizing transcripts, and identifying coaching opportunities. All via SQL functions. No separate ML infrastructure.
    </div>
    """, unsafe_allow_html=True)

    ai_tab1, ai_tab2, ai_tab3, ai_tab4 = st.tabs(["Sentiment Analysis", "AI Call Summaries", "Anomaly Detection", "Topic Clustering"])

    with ai_tab1:
        st.markdown("#### Cortex AI Sentiment — Every Call Scored Automatically")
        sent_col1, sent_col2 = st.columns([2, 1])
        with sent_col1:
            daily_sent = filtered_df.groupby(["date", "sentiment"]).size().reset_index(name="count")
            fig_s = px.area(daily_sent, x="date", y="count", color="sentiment", color_discrete_map={"Positive": "#27ae60", "Neutral": "#f39c12", "Negative": "#e74c3c"}, title="Sentiment Trend (14 Days)")
            fig_s.update_layout(template="plotly_white", height=350, font=dict(family="Inter"))
            st.plotly_chart(fig_s, use_container_width=True)
        with sent_col2:
            pos = len(filtered_df[filtered_df["sentiment"] == "Positive"])
            neu = len(filtered_df[filtered_df["sentiment"] == "Neutral"])
            neg = len(filtered_df[filtered_df["sentiment"] == "Negative"])
            fig_donut = go.Figure(go.Pie(values=[pos, neu, neg], labels=["Positive", "Neutral", "Negative"], marker_colors=["#27ae60", "#f39c12", "#e74c3c"], hole=0.5))
            fig_donut.update_layout(template="plotly_white", height=350, font=dict(family="Inter"), title="Overall Sentiment Split")
            st.plotly_chart(fig_donut, use_container_width=True)

        st.markdown("#### Drill Into Negative Sentiment Calls")
        neg_calls = filtered_df[filtered_df["sentiment"] == "Negative"].sort_values("sentiment_score").head(10)
        st.dataframe(neg_calls[["call_id", "timestamp", "bank_client", "city", "call_type", "sentiment_score", "duration_sec", "teller_name", "cortex_summary"]], use_container_width=True, hide_index=True)

    with ai_tab2:
        st.markdown("#### Cortex AI — Automatic Call Summarization")
        st.markdown("*Every call transcript is automatically summarized by Cortex AI. Managers review summaries instead of listening to hours of recordings.*")
        st.code("-- Snowflake SQL:\nSELECT call_id, SNOWFLAKE.CORTEX.SUMMARIZE(transcript) AS ai_summary\nFROM transaction_assist.call_transcripts\nWHERE timestamp > DATEADD(hour, -24, CURRENT_TIMESTAMP());", language="sql")

        for _, row in filtered_df.head(8).iterrows():
            sentiment_color = "#27ae60" if row["sentiment"] == "Positive" else "#e74c3c" if row["sentiment"] == "Negative" else "#f39c12"
            st.markdown(f"""
            <div class="call-card">
                <strong>{row['call_id']}</strong> · {row['bank_client']} · {row['city']} · {row['teller_name']} · <span style="color:{sentiment_color}; font-weight:600;">{row['sentiment']} ({row['sentiment_score']})</span>
                <span class="cortex-label">CORTEX SUMMARIZE</span>
                <br><span style="color:#555; font-size: 0.95rem;">{row['cortex_summary']}</span>
                <br><span style="color:#999; font-size: 0.8rem;">Topics: {row['topics_detected']} · Duration: {row['duration_sec']}s · {row['resolution']}</span>
            </div>
            """, unsafe_allow_html=True)

    with ai_tab3:
        st.markdown("#### Cortex AI — Anomaly & Fraud Detection")
        anomalies = filtered_df[filtered_df["anomaly_flag"] == True]
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Anomalies Detected (14d)", len(anomalies))
        with col2:
            st.metric("Fraud Patterns Flagged", len(anomalies[anomalies["call_type"] == "Account Transfer"]))
        with col3:
            st.metric("Auto-Escalated", int(len(anomalies) * 0.7))

        if len(anomalies) > 0:
            st.dataframe(anomalies[["call_id", "timestamp", "bank_client", "city", "call_type", "duration_sec", "sentiment_score", "teller_name", "cortex_summary"]].head(10), use_container_width=True, hide_index=True)

        st.code("-- Snowflake SQL (Anomaly Detection):\nSELECT call_id, city, call_type, duration_sec,\n  SNOWFLAKE.CORTEX.ANOMALY_DETECTION(duration_sec) \n    OVER (PARTITION BY city ORDER BY timestamp) AS anomaly_score\nFROM transaction_assist.calls\nWHERE anomaly_score > 0.85;", language="sql")

    with ai_tab4:
        st.markdown("#### Cortex AI — Automatic Topic Clustering")
        all_topics = filtered_df["topics_detected"].str.split(", ").explode()
        topic_counts = all_topics.value_counts().reset_index()
        topic_counts.columns = ["Topic", "Frequency"]
        fig_topics = px.bar(topic_counts, x="Frequency", y="Topic", orientation="h", color="Frequency", color_continuous_scale=["#b3d9ff", "#003366"], title="AI-Detected Topics Across All Calls")
        fig_topics.update_layout(template="plotly_white", height=400, font=dict(family="Inter"), yaxis=dict(categoryorder="total ascending"))
        st.plotly_chart(fig_topics, use_container_width=True)

        st.markdown("#### Topic × Sentiment Cross-Analysis")
        topic_sent = filtered_df.copy()
        topic_sent["topic_list"] = topic_sent["topics_detected"].str.split(", ")
        topic_sent = topic_sent.explode("topic_list")
        cross = topic_sent.groupby(["topic_list", "sentiment"]).size().reset_index(name="count")
        fig_cross = px.bar(cross, x="topic_list", y="count", color="sentiment", color_discrete_map={"Positive": "#27ae60", "Neutral": "#f39c12", "Negative": "#e74c3c"}, title="Topic Sentiment Breakdown", barmode="stack")
        fig_cross.update_layout(template="plotly_white", height=350, font=dict(family="Inter"), xaxis_title="Topic")
        st.plotly_chart(fig_cross, use_container_width=True)

with tab3:
    st.markdown("### 🔍 Snowflake Intelligence — Ask Your Data Anything")
    st.markdown("""
    <div class="ai-insight">
    <strong>Snowflake Intelligence</strong> is Snowflake's natural language interface. Banking client executives, 
    operations managers, and teller supervisors can ask questions in plain English and get instant answers — 
    no SQL, no dashboard navigation, no analyst requests. Just type a question and get data.
    </div>
    """, unsafe_allow_html=True)

    if "si_history" not in st.session_state:
        st.session_state.si_history = []

    preset = st.selectbox("Try a preset question or type your own below:", [
        "(Select a question...)",
        "What was our busiest day last week?",
        "Show me the top 5 cities by call volume",
        "Which tellers have the lowest sentiment scores?",
        "How many calls were flagged as anomalies?",
        "What's the average wait time by bank client?",
        "Compare call resolution rates across cities",
        "What topics appear most in negative sentiment calls?",
        "Show me all calls longer than 5 minutes from Miami"
    ], key="si_preset")

    user_q = st.chat_input("Ask Snowflake Intelligence a question about your ATM call data...")

    query = user_q if user_q else (preset if preset != "(Select a question...)" else None)

    if query and (not st.session_state.si_history or st.session_state.si_history[-1].get("q") != query):
        with st.spinner("Snowflake Intelligence is analyzing your data..."):
            time.sleep(1.2)

        answer = ""
        chart = None
        table = None
        sql = ""

        q_lower = query.lower()
        if "busiest" in q_lower or "busy" in q_lower:
            daily = filtered_df.groupby("date").size().reset_index(name="calls")
            top_day = daily.loc[daily["calls"].idxmax()]
            answer = f"The busiest day was **{top_day['date']}** with **{top_day['calls']} calls**."
            chart = px.bar(daily.sort_values("date"), x="date", y="calls", color_discrete_sequence=["#29B5E8"], title="Daily Call Volume")
            sql = "SELECT DATE(timestamp) as call_date, COUNT(*) as calls\nFROM transaction_assist.calls\nGROUP BY call_date ORDER BY calls DESC LIMIT 1;"
        elif "top" in q_lower and "city" in q_lower or "cities" in q_lower:
            city_vol = filtered_df.groupby("city").size().reset_index(name="calls").sort_values("calls", ascending=False).head(5)
            answer = f"Top 5 cities by call volume:"
            table = city_vol
            chart = px.bar(city_vol, x="city", y="calls", color_discrete_sequence=["#003366"], title="Top 5 Cities")
            sql = "SELECT city, COUNT(*) as calls\nFROM transaction_assist.calls\nGROUP BY city ORDER BY calls DESC LIMIT 5;"
        elif "lowest sentiment" in q_lower or "teller" in q_lower and "sentiment" in q_lower:
            tperf = filtered_df.groupby("teller_name").agg({"sentiment_score": "mean", "call_id": "count"}).reset_index()
            tperf.columns = ["Teller", "Avg Sentiment", "Total Calls"]
            tperf = tperf.sort_values("Avg Sentiment").head(5)
            answer = "Tellers with lowest average sentiment scores (may need coaching):"
            table = tperf
            sql = "SELECT teller_name, AVG(sentiment_score) as avg_sentiment, COUNT(*) as calls\nFROM transaction_assist.calls\nGROUP BY teller_name ORDER BY avg_sentiment ASC LIMIT 5;"
        elif "anomal" in q_lower or "flag" in q_lower:
            anom_count = len(filtered_df[filtered_df["anomaly_flag"]])
            answer = f"**{anom_count} calls** were flagged as anomalies in the current dataset. {int(anom_count*0.7)} were auto-escalated to the fraud review team."
            table = filtered_df[filtered_df["anomaly_flag"]][["call_id", "timestamp", "bank_client", "city", "call_type", "cortex_summary"]].head(8)
            sql = "SELECT * FROM transaction_assist.calls\nWHERE anomaly_flag = TRUE\nORDER BY timestamp DESC;"
        elif "wait time" in q_lower:
            wt = filtered_df.groupby("bank_client")["wait_time_sec"].mean().reset_index()
            wt.columns = ["Bank Client", "Avg Wait Time (sec)"]
            wt = wt.sort_values("Avg Wait Time (sec)", ascending=False)
            answer = "Average wait time by banking client:"
            table = wt
            chart = px.bar(wt, x="Bank Client", y="Avg Wait Time (sec)", color_discrete_sequence=["#29B5E8"], title="Wait Time by Client")
            sql = "SELECT bank_client, AVG(wait_time_sec) as avg_wait\nFROM transaction_assist.calls\nGROUP BY bank_client ORDER BY avg_wait DESC;"
        elif "resolution" in q_lower and "city" in q_lower or "cities" in q_lower:
            res = filtered_df.groupby("city").apply(lambda x: round((x["resolution"].str.contains("Resolved")).sum() / len(x) * 100, 1)).reset_index(name="Resolution Rate %")
            answer = "Call resolution rates by city:"
            table = res.sort_values("Resolution Rate %", ascending=False)
            chart = px.bar(res.sort_values("Resolution Rate %"), x="city", y="Resolution Rate %", color="Resolution Rate %", color_continuous_scale=["#e74c3c", "#f39c12", "#27ae60"], title="Resolution Rate by City")
            sql = "SELECT city,\n  ROUND(SUM(CASE WHEN resolution LIKE '%Resolved%' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 1) as resolution_pct\nFROM transaction_assist.calls\nGROUP BY city ORDER BY resolution_pct DESC;"
        elif "negative" in q_lower and "topic" in q_lower:
            neg = filtered_df[filtered_df["sentiment"] == "Negative"]
            neg_topics = neg["topics_detected"].str.split(", ").explode().value_counts().reset_index()
            neg_topics.columns = ["Topic", "Count"]
            answer = "Most common topics in negative sentiment calls:"
            table = neg_topics
            chart = px.bar(neg_topics, x="Count", y="Topic", orientation="h", color_discrete_sequence=["#e74c3c"], title="Topics in Negative Calls")
            sql = "SELECT topic, COUNT(*) as count\nFROM transaction_assist.calls, LATERAL FLATTEN(input => topics_detected)\nWHERE sentiment = 'Negative'\nGROUP BY topic ORDER BY count DESC;"
        elif "longer than" in q_lower or "more than" in q_lower or "5 min" in q_lower:
            long_calls = filtered_df[filtered_df["duration_sec"] > 300]
            if "miami" in q_lower:
                long_calls = long_calls[long_calls["city"] == "Miami"]
            answer = f"Found **{len(long_calls)} calls** longer than 5 minutes{' from Miami' if 'miami' in q_lower else ''}:"
            table = long_calls[["call_id", "timestamp", "bank_client", "city", "duration_sec", "sentiment", "call_type", "teller_name"]].head(10)
            sql = f"SELECT * FROM transaction_assist.calls\nWHERE duration_sec > 300{' AND city = ''Miami''' if 'miami' in q_lower else ''}\nORDER BY duration_sec DESC;"
        else:
            answer = f"Based on the current dataset ({len(filtered_df):,} calls across {filtered_df['bank_client'].nunique()} banking clients), the average call duration is **{filtered_df['duration_sec'].mean():.0f}s**, positive sentiment is **{positive_pct:.0f}%**, and **{len(filtered_df[filtered_df['anomaly_flag']])} anomalies** have been detected. Try asking about specific cities, tellers, topics, or time periods."
            sql = "SELECT COUNT(*) as total_calls,\n  AVG(duration_sec) as avg_duration,\n  AVG(sentiment_score) as avg_sentiment\nFROM transaction_assist.calls;"

        st.session_state.si_history.append({"q": query, "a": answer, "chart": chart, "table": table, "sql": sql})

    for item in st.session_state.si_history:
        st.markdown(f'<div class="si-chat-user"><strong>You:</strong> {item["q"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="si-chat-msg"><strong>❄️ Snowflake Intelligence:</strong><br>{item["a"]}</div>', unsafe_allow_html=True)
        if item.get("table") is not None:
            st.dataframe(item["table"], use_container_width=True, hide_index=True)
        if item.get("chart") is not None:
            item["chart"].update_layout(template="plotly_white", height=300, font=dict(family="Inter"))
            st.plotly_chart(item["chart"], use_container_width=True)
        if item.get("sql"):
            with st.expander("View generated SQL"):
                st.code(item["sql"], language="sql")

    if st.button("Clear conversation", key="clear_si"):
        st.session_state.si_history = []
        st.rerun()

with tab4:
    st.markdown("### 📊 Data Explorer — Slice & Dice Your Call Data")
    st.markdown("*Interactive exploration — filter, group, and visualize any dimension of your ATM call data.*")

    col_f1, col_f2, col_f3, col_f4 = st.columns(4)
    with col_f1:
        x_axis = st.selectbox("X-Axis", ["city", "bank_client", "call_type", "language", "teller_name", "hour", "sentiment", "state"], key="x_explorer")
    with col_f2:
        y_metric = st.selectbox("Metric", ["Count of Calls", "Avg Duration (sec)", "Avg Sentiment Score", "Avg Wait Time (sec)", "Avg Customer Effort Score"], key="y_explorer")
    with col_f3:
        color_by = st.selectbox("Color By", ["(None)", "sentiment", "call_type", "bank_client", "language", "resolution"], key="color_explorer")
    with col_f4:
        chart_type = st.selectbox("Chart Type", ["Bar", "Scatter", "Heatmap", "Box Plot"], key="chart_explorer")

    metric_map = {"Count of Calls": "count", "Avg Duration (sec)": "duration_sec", "Avg Sentiment Score": "sentiment_score", "Avg Wait Time (sec)": "wait_time_sec", "Avg Customer Effort Score": "customer_effort_score"}
    metric_col = metric_map[y_metric]

    if metric_col == "count":
        explorer_data = filtered_df.groupby(x_axis).size().reset_index(name="value")
    else:
        explorer_data = filtered_df.groupby(x_axis)[metric_col].mean().reset_index(name="value")

    color_arg = color_by if color_by != "(None)" else None

    if chart_type == "Bar":
        if color_arg:
            if metric_col == "count":
                grp = filtered_df.groupby([x_axis, color_arg]).size().reset_index(name="value")
            else:
                grp = filtered_df.groupby([x_axis, color_arg])[metric_col].mean().reset_index(name="value")
            fig_ex = px.bar(grp, x=x_axis, y="value", color=color_arg, barmode="group", title=f"{y_metric} by {x_axis}")
        else:
            fig_ex = px.bar(explorer_data.sort_values("value", ascending=False), x=x_axis, y="value", color_discrete_sequence=["#29B5E8"], title=f"{y_metric} by {x_axis}")
    elif chart_type == "Scatter":
        fig_ex = px.scatter(filtered_df, x="duration_sec", y="sentiment_score", color=color_arg or "sentiment", size="wait_time_sec", hover_data=["call_id", "city", "teller_name"], title="Duration vs Sentiment", color_discrete_map={"Positive": "#27ae60", "Neutral": "#f39c12", "Negative": "#e74c3c"})
    elif chart_type == "Heatmap":
        heat = filtered_df.groupby([x_axis, "sentiment"]).size().reset_index(name="count")
        heat_pivot = heat.pivot(index=x_axis, columns="sentiment", values="count").fillna(0)
        fig_ex = px.imshow(heat_pivot, title=f"Sentiment Heatmap by {x_axis}", color_continuous_scale="Blues", aspect="auto")
    else:
        fig_ex = px.box(filtered_df, x=x_axis, y="duration_sec", color=color_arg, title=f"Call Duration Distribution by {x_axis}")

    fig_ex.update_layout(template="plotly_white", height=450, font=dict(family="Inter"))
    st.plotly_chart(fig_ex, use_container_width=True)

    st.markdown("#### Raw Data View")
    show_cols = st.multiselect("Select columns to display", options=filtered_df.columns.tolist(), default=["call_id", "timestamp", "bank_client", "city", "call_type", "duration_sec", "sentiment", "sentiment_score", "teller_name"], key="col_select")
    st.dataframe(filtered_df[show_cols].head(50), use_container_width=True, hide_index=True)
    st.caption(f"Showing first 50 of {len(filtered_df):,} rows. In production, Snowflake handles billions of rows with sub-second query times.")

with tab5:
    st.markdown("### 📈 Remote Teller Performance Analytics")
    st.markdown("*Cortex AI scores every teller on every call — replacing manual random sampling with complete coverage.*")

    teller_stats = filtered_df.groupby("teller_name").agg({
        "call_id": "count", "sentiment_score": "mean", "duration_sec": "mean",
        "coaching_opportunity": "sum", "wait_time_sec": "mean"
    }).reset_index()
    teller_stats.columns = ["Teller", "Total Calls", "Avg Sentiment", "Avg Duration (s)", "Coaching Flags", "Avg Wait (s)"]
    teller_stats["Performance Score"] = ((teller_stats["Avg Sentiment"] * 50) + (1 - teller_stats["Avg Duration (s)"] / max(teller_stats["Avg Duration (s)"].max(), 1)) * 30 + (1 - teller_stats["Coaching Flags"] / max(teller_stats["Coaching Flags"].max(), 1)) * 20).round(1)
    teller_stats = teller_stats.sort_values("Performance Score", ascending=False)

    selected_teller = st.selectbox("Select a teller to drill into:", ["All Tellers"] + sorted(filtered_df["teller_name"].unique().tolist()), key="teller_select")

    if selected_teller == "All Tellers":
        fig_perf = px.scatter(teller_stats, x="Avg Duration (s)", y="Avg Sentiment", size="Total Calls", color="Performance Score", color_continuous_scale=["#e74c3c", "#f39c12", "#27ae60"], hover_name="Teller", title="Teller Performance Map (size = call volume)")
        fig_perf.update_layout(template="plotly_white", height=400, font=dict(family="Inter"))
        st.plotly_chart(fig_perf, use_container_width=True)
        st.dataframe(teller_stats, use_container_width=True, hide_index=True)
    else:
        teller_calls = filtered_df[filtered_df["teller_name"] == selected_teller]
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Calls", len(teller_calls))
        with col2:
            st.metric("Avg Sentiment", f"{teller_calls['sentiment_score'].mean():.2f}")
        with col3:
            st.metric("Avg Duration", f"{teller_calls['duration_sec'].mean():.0f}s")
        with col4:
            st.metric("Coaching Flags", int(teller_calls["coaching_opportunity"].sum()))

        daily_teller = teller_calls.groupby("date")["sentiment_score"].mean().reset_index()
        fig_t = px.line(daily_teller, x="date", y="sentiment_score", title=f"{selected_teller} — Sentiment Over Time", markers=True, color_discrete_sequence=["#29B5E8"])
        fig_t.update_layout(template="plotly_white", height=300, font=dict(family="Inter"))
        st.plotly_chart(fig_t, use_container_width=True)
        st.dataframe(teller_calls[["call_id", "timestamp", "bank_client", "city", "call_type", "duration_sec", "sentiment", "sentiment_score", "cortex_summary"]].head(10), use_container_width=True, hide_index=True)

with tab6:
    st.markdown("### 🏦 Banking Client Reports (Multi-Tenant)")
    st.markdown("*Each banking client receives their own secure analytics. One platform, 50+ clients, zero data leakage.*")

    bank_summary = filtered_df.groupby("bank_client").agg({
        "call_id": "count", "duration_sec": "mean", "sentiment_score": "mean",
        "wait_time_sec": "mean", "anomaly_flag": "sum"
    }).reset_index()
    bank_summary.columns = ["Bank Client", "Total Calls", "Avg Duration (s)", "Avg Sentiment", "Avg Wait (s)", "Security Alerts"]
    st.dataframe(bank_summary.sort_values("Total Calls", ascending=False), use_container_width=True, hide_index=True)

    col1, col2 = st.columns(2)
    with col1:
        fig_bank = px.bar(bank_summary.sort_values("Total Calls", ascending=False), x="Bank Client", y="Total Calls", color="Avg Sentiment", color_continuous_scale=["#e74c3c", "#f39c12", "#27ae60"], title="Call Volume by Client")
        fig_bank.update_layout(template="plotly_white", height=300, font=dict(family="Inter"))
        st.plotly_chart(fig_bank, use_container_width=True)
    with col2:
        bench_metrics = ["Avg Duration (s)", "Avg Sentiment", "Avg Wait (s)"]
        selected_bank = st.selectbox("Compare client to benchmark:", bank_summary["Bank Client"].tolist(), key="bench_bank")
        client_row = bank_summary[bank_summary["Bank Client"] == selected_bank].iloc[0]
        bench_vals = [bank_summary["Avg Duration (s)"].mean(), bank_summary["Avg Sentiment"].mean(), bank_summary["Avg Wait (s)"].mean()]
        client_vals = [client_row["Avg Duration (s)"], client_row["Avg Sentiment"], client_row["Avg Wait (s)"]]
        fig_bench = go.Figure()
        fig_bench.add_trace(go.Bar(name=selected_bank, x=bench_metrics, y=client_vals, marker_color="#29B5E8"))
        fig_bench.add_trace(go.Bar(name="All-Client Average", x=bench_metrics, y=bench_vals, marker_color="#003366"))
        fig_bench.update_layout(title=f"{selected_bank} vs. Benchmark", template="plotly_white", height=300, barmode="group", font=dict(family="Inter"))
        st.plotly_chart(fig_bench, use_container_width=True)

    st.markdown("""
    <div class="ai-insight">
    <strong>💰 Revenue Model:</strong> This cross-client benchmarking and AI-powered analytics is the premium tier
    that Diebold Nixdorf sells to banking clients. Today you deliver CSV exports. With Snowflake, you deliver intelligence
    that clients pay a premium for — creating a new recurring revenue stream.
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
st.markdown("""
<div style="background: linear-gradient(135deg, #003366 0%, #004d99 100%); padding: 2rem; border-radius: 16px; text-align: center; color: white;">
    <h3 style="margin: 0; color: white;">This Is What Transaction Assist Becomes with Snowflake</h3>
    <p style="margin: 0.5rem 0 0 0; opacity: 0.9;">Real-time call analytics · AI sentiment & summarization · Snowflake Intelligence (natural language) · Interactive data exploration · Multi-tenant secure sharing</p>
    <p style="margin: 1rem 0 0 0; opacity: 0.7; font-size: 0.9rem;">Architecture: Kafka (Zoom/Twilio) → Snowflake Kafka Connector → Dynamic Tables → Cortex AI → Streamlit / Snowflake Intelligence</p>
</div>
""", unsafe_allow_html=True)

render_section_notes("demo_call_analytics", "Call Analytics Dashboard")
render_section_notes("demo_cortex_ai", "Cortex AI Insights")
render_section_notes("demo_snowflake_intelligence", "Snowflake Intelligence")
render_section_notes("demo_general", "General Notes — Art of Possible Demo")
