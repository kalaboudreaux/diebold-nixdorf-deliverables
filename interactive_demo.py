import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import json
import time

st.set_page_config(page_title="Snowflake ATM Intelligence Hub | Diebold Nixdorf", page_icon="❄️", layout="wide")

st.markdown("""
<style>
    .main-title {font-size: 2.2rem; font-weight: 700; color: #29B5E8;}
    .kpi-card {background: linear-gradient(135deg, #0d1b2e 0%, #1a2744 100%); padding: 1.5rem; border-radius: 12px; border: 1px solid #29B5E833; text-align: center;}
    .kpi-value {font-size: 2.2rem; font-weight: 700; color: #29B5E8;}
    .kpi-label {font-size: 0.85rem; color: #a0a0a0; text-transform: uppercase;}
    .kpi-delta {font-size: 0.9rem; color: #4CAF50;}
    .alert-critical {background: #2d1b1b; border-left: 4px solid #ff4444; padding: 1rem; border-radius: 8px; margin: 0.5rem 0;}
    .alert-warning {background: #2d2a1b; border-left: 4px solid #FF9800; padding: 1rem; border-radius: 8px; margin: 0.5rem 0;}
    .alert-info {background: #1b2d2d; border-left: 4px solid #29B5E8; padding: 1rem; border-radius: 8px; margin: 0.5rem 0;}
    .ai-response {background: #1a2332; padding: 1.5rem; border-radius: 10px; border-left: 4px solid #29B5E8; margin: 1rem 0;}
    .demo-badge {background: #29B5E8; color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.8rem; font-weight: 600;}
    .tenant-selector {background: #162447; padding: 1rem; border-radius: 10px; margin: 1rem 0;}
    .anomaly-card {background: linear-gradient(135deg, #1a0a0a 0%, #2d1515 100%); padding: 1.5rem; border-radius: 10px; border: 1px solid #ff444444;}
    .prediction-card {background: linear-gradient(135deg, #0a1a0a 0%, #152d15 100%); padding: 1.5rem; border-radius: 10px; border: 1px solid #4CAF5044;}
    .stTabs [data-baseweb="tab-list"] {gap: 8px;}
    .stTabs [data-baseweb="tab"] {background-color: #162447; border-radius: 8px; padding: 8px 16px;}
</style>
""", unsafe_allow_html=True)

np.random.seed(42)

@st.cache_data
def generate_atm_data():
    cities = ["New York", "Chicago", "Los Angeles", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose",
              "Austin", "Jacksonville", "Fort Worth", "Columbus", "Charlotte", "Indianapolis", "San Francisco", "Seattle", "Denver", "Nashville"]
    lats = [40.71, 41.88, 34.05, 29.76, 33.45, 39.95, 29.42, 32.72, 32.78, 37.34,
            30.27, 30.33, 32.75, 39.96, 35.23, 39.77, 37.77, 47.61, 39.74, 36.16]
    lons = [-74.01, -87.63, -118.24, -95.37, -112.07, -75.17, -98.49, -117.16, -96.80, -121.89,
            -97.74, -81.66, -97.33, -82.99, -80.84, -86.16, -122.42, -122.33, -104.99, -86.78]
    
    atms = []
    for i in range(200):
        city_idx = i % len(cities)
        atms.append({
            "atm_id": f"DN-ATM-{str(i+1).zfill(4)}",
            "city": cities[city_idx],
            "lat": lats[city_idx] + np.random.uniform(-0.05, 0.05),
            "lon": lons[city_idx] + np.random.uniform(-0.05, 0.05),
            "bank_client": random.choice(["JPMorgan Chase", "Bank of America", "Wells Fargo", "Citibank", "US Bank"]),
            "model": random.choice(["DN Series 400", "DN Series 200", "DN Vynamic"]),
            "status": random.choices(["Online", "Online", "Online", "Online", "Warning", "Critical", "Maintenance"], weights=[40, 35, 30, 25, 8, 4, 3])[0],
            "uptime_pct": round(np.random.uniform(92, 99.9), 1),
            "daily_transactions": int(np.random.uniform(80, 450)),
            "cash_level_pct": int(np.random.uniform(15, 95)),
            "last_service": (datetime.now() - timedelta(days=int(np.random.uniform(1, 90)))).strftime("%Y-%m-%d"),
            "predicted_failure_days": int(np.random.uniform(5, 180))
        })
    return pd.DataFrame(atms)

@st.cache_data
def generate_transaction_stream():
    now = datetime.now()
    transactions = []
    for i in range(500):
        ts = now - timedelta(minutes=random.randint(0, 1440))
        tx_type = random.choices(["Withdrawal", "Balance Inquiry", "Deposit", "Transfer", "Bill Pay"], weights=[45, 25, 15, 10, 5])[0]
        amount = round(random.choice([20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 250, 300, 400, 500]) if tx_type == "Withdrawal" else random.uniform(0, 5000), 2)
        is_anomaly = random.random() < 0.03
        transactions.append({
            "timestamp": ts,
            "atm_id": f"DN-ATM-{str(random.randint(1, 200)).zfill(4)}",
            "transaction_type": tx_type,
            "amount": amount,
            "duration_sec": round(np.random.uniform(15, 120) if not is_anomaly else np.random.uniform(180, 600), 1),
            "status": "Completed" if random.random() > 0.05 else random.choice(["Failed", "Timeout", "Cancelled"]),
            "anomaly_flag": is_anomaly,
            "anomaly_type": random.choice(["Unusual Amount", "Rapid Succession", "Off-hours Activity", "Card Skimming Pattern"]) if is_anomaly else None,
            "risk_score": round(np.random.uniform(0.7, 0.99), 2) if is_anomaly else round(np.random.uniform(0.01, 0.3), 2),
            "customer_segment": random.choice(["Retail", "Commercial", "Premium", "Student"])
        })
    df = pd.DataFrame(transactions)
    df = df.sort_values("timestamp", ascending=False).reset_index(drop=True)
    return df

@st.cache_data
def generate_hourly_volume():
    hours = list(range(24))
    base_volume = [120, 80, 45, 30, 25, 35, 85, 250, 420, 380, 350, 390, 410, 370, 340, 360, 400, 450, 380, 320, 280, 240, 200, 160]
    data = []
    for h in hours:
        vol = base_volume[h] + int(np.random.uniform(-30, 30))
        data.append({"hour": h, "volume": max(vol, 10), "avg_amount": round(np.random.uniform(80, 220), 2)})
    return pd.DataFrame(data)

atm_df = generate_atm_data()
tx_df = generate_transaction_stream()
hourly_df = generate_hourly_volume()

st.markdown('<p class="main-title">❄️ Snowflake ATM Intelligence Hub</p>', unsafe_allow_html=True)
st.markdown("**Powered by Snowflake Cortex AI** | Diebold Nixdorf — Future State Demo Experience")

bank_filter = st.selectbox("🏦 Bank Client View (Multi-Tenant Secure Sharing)", 
    ["All Banks (DN Admin View)", "JPMorgan Chase", "Bank of America", "Wells Fargo", "Citibank", "US Bank"])

if bank_filter != "All Banks (DN Admin View)":
    atm_df = atm_df[atm_df["bank_client"] == bank_filter]
    tx_df_filtered = tx_df[tx_df["atm_id"].isin(atm_df["atm_id"])]
    st.info(f"🔒 **Secure Data Sharing Active** — Showing only {bank_filter}'s ATM network. Other bank data is cryptographically isolated.")
else:
    tx_df_filtered = tx_df

st.markdown("---")

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Real-Time Operations", 
    "🤖 Cortex AI Anomaly Detection",
    "💬 Ask Questions (Cortex Analyst)", 
    "🔮 Predictive Maintenance",
    "📈 Executive Analytics"
])

with tab1:
    col1, col2, col3, col4, col5 = st.columns(5)
    online = len(atm_df[atm_df["status"] == "Online"])
    warning = len(atm_df[atm_df["status"] == "Warning"])
    critical = len(atm_df[atm_df["status"] == "Critical"])
    total_tx = tx_df_filtered["amount"].sum()
    avg_uptime = atm_df["uptime_pct"].mean()
    
    with col1:
        st.metric("ATMs Online", f"{online}/{len(atm_df)}", f"{round(online/len(atm_df)*100, 1)}%")
    with col2:
        st.metric("Warnings", warning, "Needs attention" if warning > 0 else "All clear")
    with col3:
        st.metric("Critical", critical, "Immediate action" if critical > 0 else "None")
    with col4:
        st.metric("24h Volume", f"${total_tx:,.0f}", f"{len(tx_df_filtered)} transactions")
    with col5:
        st.metric("Avg Uptime", f"{avg_uptime:.1f}%", "+0.3% vs last week")
    
    st.markdown("### ATM Network Map — Live Status")
    
    color_map = {"Online": "#4CAF50", "Warning": "#FF9800", "Critical": "#ff4444", "Maintenance": "#9E9E9E"}
    atm_df["color"] = atm_df["status"].map(color_map)
    atm_df["size"] = atm_df["status"].map({"Online": 8, "Warning": 14, "Critical": 18, "Maintenance": 6})
    
    fig_map = px.scatter_mapbox(
        atm_df, lat="lat", lon="lon", 
        color="status",
        color_discrete_map=color_map,
        size="size",
        hover_name="atm_id",
        hover_data=["city", "bank_client", "model", "uptime_pct", "daily_transactions", "cash_level_pct"],
        mapbox_style="carto-darkmatter",
        zoom=3, center={"lat": 39.0, "lon": -98.0},
        height=500
    )
    fig_map.update_layout(margin=dict(l=0, r=0, t=0, b=0))
    st.plotly_chart(fig_map, use_container_width=True)
    
    st.markdown("### Live Transaction Feed")
    col_a, col_b = st.columns([2, 1])
    with col_a:
        fig_hourly = go.Figure()
        fig_hourly.add_trace(go.Bar(x=hourly_df["hour"], y=hourly_df["volume"], marker_color="#29B5E8", name="Transaction Volume"))
        fig_hourly.update_layout(title="Today's Transaction Volume by Hour", template="plotly_dark", height=300, xaxis_title="Hour", yaxis_title="Transactions")
        st.plotly_chart(fig_hourly, use_container_width=True)
    
    with col_b:
        st.markdown("#### Recent Transactions")
        recent = tx_df_filtered.head(8)[["timestamp", "atm_id", "transaction_type", "amount", "status"]]
        recent["timestamp"] = recent["timestamp"].dt.strftime("%H:%M:%S")
        recent["amount"] = recent["amount"].apply(lambda x: f"${x:,.2f}")
        st.dataframe(recent, use_container_width=True, hide_index=True)

with tab2:
    st.markdown("### 🤖 Cortex AI — Real-Time Anomaly Detection")
    st.markdown("*Snowflake Cortex AI continuously monitors transaction patterns and flags suspicious activity in real-time.*")
    
    anomalies = tx_df_filtered[tx_df_filtered["anomaly_flag"] == True].head(10)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Anomalies Detected (24h)", len(anomalies), "AI-flagged")
    with col2:
        st.metric("Avg Risk Score", f"{anomalies['risk_score'].mean():.2f}" if len(anomalies) > 0 else "0.00", "High confidence")
    with col3:
        st.metric("False Positive Rate", "2.3%", "-0.8% vs. last month")
    
    st.markdown("---")
    
    if len(anomalies) > 0:
        for _, row in anomalies.iterrows():
            severity_color = "#ff4444" if row["risk_score"] > 0.9 else "#FF9800" if row["risk_score"] > 0.8 else "#29B5E8"
            st.markdown(f"""
            <div class="anomaly-card">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div>
                        <strong style="color: {severity_color};">⚠️ {row['anomaly_type']}</strong> — {row['atm_id']}
                        <br><span style="color: #a0a0a0;">Transaction: {row['transaction_type']} | ${row['amount']:,.2f} | Duration: {row['duration_sec']}s</span>
                    </div>
                    <div style="text-align: right;">
                        <span style="color: {severity_color}; font-size: 1.5rem; font-weight: 700;">{row['risk_score']:.0%}</span>
                        <br><span style="color: #a0a0a0; font-size: 0.8rem;">Risk Score</span>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### AI Detection Models Active")
    models_data = pd.DataFrame({
        "Model": ["Transaction Anomaly Detection", "Card Skimming Pattern Recognition", "Cash Dispensing Fraud", "Off-Hours Behavioral Analysis", "Rapid Succession Detection"],
        "Type": ["Cortex AI (Unsupervised)", "Cortex AI (Supervised)", "Cortex AI (Rules + ML)", "Cortex AI (Time Series)", "Cortex AI (Streaming)"],
        "Accuracy": ["97.7%", "99.2%", "98.4%", "96.8%", "99.5%"],
        "Alerts (24h)": [4, 1, 2, 3, 2],
        "Status": ["✅ Active", "✅ Active", "✅ Active", "✅ Active", "✅ Active"]
    })
    st.dataframe(models_data, use_container_width=True, hide_index=True)

with tab3:
    st.markdown("### 💬 Ask Questions About Your ATM Data")
    st.markdown("*Powered by Cortex Analyst — Ask any question in plain English. No SQL required.*")
    
    sample_questions = [
        "Which ATMs have the lowest uptime this week?",
        "What's the average transaction volume by city?",
        "Show me anomaly trends over the last 30 days",
        "Which bank client has the highest transaction failure rate?",
        "Predict which ATMs will need service in the next 7 days",
        "What's the total cash dispensed today vs. yesterday?"
    ]
    
    st.markdown("**Try these example questions:**")
    question_cols = st.columns(3)
    for i, q in enumerate(sample_questions):
        with question_cols[i % 3]:
            if st.button(q, key=f"q_{i}"):
                st.session_state["selected_question"] = q
    
    user_question = st.text_input("Or type your own question:", value=st.session_state.get("selected_question", ""), placeholder="e.g., Which ATMs are running low on cash?")
    
    if user_question:
        with st.spinner("Cortex Analyst generating answer..."):
            time.sleep(1.5)
        
        st.markdown("""<div class="ai-response">""", unsafe_allow_html=True)
        st.markdown(f"**🤖 Cortex Analyst Response:**")
        
        if "lowest uptime" in user_question.lower():
            low_uptime = atm_df.nsmallest(5, "uptime_pct")[["atm_id", "city", "bank_client", "uptime_pct", "status", "last_service"]]
            st.markdown("Here are the 5 ATMs with the lowest uptime this week:")
            st.dataframe(low_uptime, use_container_width=True, hide_index=True)
            st.markdown("**Insight:** 3 of these ATMs are in high-traffic locations and should be prioritized for preventive maintenance within the next 48 hours.")
            st.code("-- Generated SQL:\nSELECT atm_id, city, bank_client, uptime_pct, status, last_service_date\nFROM atm_network.live_status\nWHERE uptime_pct < 95\nORDER BY uptime_pct ASC\nLIMIT 5;", language="sql")
        
        elif "transaction volume" in user_question.lower() or "by city" in user_question.lower():
            city_vol = atm_df.groupby("city").agg({"daily_transactions": "sum", "atm_id": "count"}).reset_index()
            city_vol.columns = ["City", "Total Daily Transactions", "ATM Count"]
            city_vol = city_vol.sort_values("Total Daily Transactions", ascending=False).head(10)
            st.markdown("Top 10 cities by transaction volume:")
            fig = px.bar(city_vol, x="City", y="Total Daily Transactions", color="ATM Count", color_continuous_scale="Blues", template="plotly_dark")
            st.plotly_chart(fig, use_container_width=True)
            st.code("-- Generated SQL:\nSELECT city, SUM(daily_transactions) as total_volume, COUNT(*) as atm_count\nFROM atm_network.live_status\nGROUP BY city\nORDER BY total_volume DESC\nLIMIT 10;", language="sql")
        
        elif "anomaly" in user_question.lower() or "trend" in user_question.lower():
            days = pd.date_range(end=datetime.now(), periods=30)
            anomaly_trend = pd.DataFrame({"date": days, "anomalies": np.random.poisson(4, 30), "resolved": np.random.poisson(3, 30)})
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=anomaly_trend["date"], y=anomaly_trend["anomalies"], name="Detected", line=dict(color="#ff4444")))
            fig.add_trace(go.Scatter(x=anomaly_trend["date"], y=anomaly_trend["resolved"], name="Resolved", line=dict(color="#4CAF50")))
            fig.update_layout(title="Anomaly Detection Trend (30 Days)", template="plotly_dark", height=350)
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Insight:** Anomaly detection rate is stable. Resolution time has improved by 22% since AI-powered classification was enabled.")
        
        elif "failure rate" in user_question.lower() or "bank client" in user_question.lower():
            bank_stats = tx_df_filtered.groupby(atm_df.set_index("atm_id").loc[tx_df_filtered["atm_id"]]["bank_client"].values if len(tx_df_filtered) > 0 else []).agg({"status": lambda x: (x != "Completed").sum() / len(x) * 100}).reset_index()
            st.markdown("Transaction failure rates vary by network load and ATM age:")
            failure_data = pd.DataFrame({
                "Bank Client": ["JPMorgan Chase", "Bank of America", "Wells Fargo", "Citibank", "US Bank"],
                "Failure Rate": [2.1, 3.4, 2.8, 4.1, 1.9],
                "Primary Cause": ["Timeout", "Card Read Error", "Network", "Cash Jam", "Timeout"]
            })
            st.dataframe(failure_data, use_container_width=True, hide_index=True)
        
        elif "predict" in user_question.lower() or "service" in user_question.lower() or "maintenance" in user_question.lower():
            urgent = atm_df[atm_df["predicted_failure_days"] < 14].sort_values("predicted_failure_days")[["atm_id", "city", "bank_client", "predicted_failure_days", "last_service", "model"]]
            st.markdown(f"**{len(urgent)} ATMs** predicted to need service within 14 days:")
            st.dataframe(urgent.head(10), use_container_width=True, hide_index=True)
            st.markdown("**Recommendation:** Schedule preventive maintenance for these units to avoid unplanned downtime.")
        
        elif "cash" in user_question.lower():
            low_cash = atm_df[atm_df["cash_level_pct"] < 30].sort_values("cash_level_pct")[["atm_id", "city", "bank_client", "cash_level_pct", "daily_transactions"]]
            st.markdown(f"**{len(low_cash)} ATMs** currently below 30% cash capacity:")
            st.dataframe(low_cash.head(10), use_container_width=True, hide_index=True)
            total_today = tx_df_filtered[tx_df_filtered["transaction_type"] == "Withdrawal"]["amount"].sum()
            st.metric("Total Cash Dispensed Today", f"${total_today:,.0f}")
        
        else:
            st.markdown(f"""
            Based on the current data, here's what I found for: **"{user_question}"**
            
            - Total ATMs in network: **{len(atm_df)}**
            - Online rate: **{len(atm_df[atm_df['status'] == 'Online'])/len(atm_df)*100:.1f}%**
            - Average daily transactions per ATM: **{atm_df['daily_transactions'].mean():.0f}**
            - ATMs needing attention: **{len(atm_df[atm_df['status'].isin(['Warning', 'Critical'])])}**
            
            *I can answer more specific questions about uptime, transactions, anomalies, predictions, and cash levels.*
            """)
        
        st.markdown("</div>", unsafe_allow_html=True)

with tab4:
    st.markdown("### 🔮 Predictive Maintenance — Powered by Cortex AI")
    st.markdown("*AI models analyze sensor data, transaction patterns, and service history to predict failures before they happen.*")
    
    col1, col2, col3, col4 = st.columns(4)
    urgent_count = len(atm_df[atm_df["predicted_failure_days"] < 7])
    warning_count = len(atm_df[(atm_df["predicted_failure_days"] >= 7) & (atm_df["predicted_failure_days"] < 30)])
    healthy_count = len(atm_df[atm_df["predicted_failure_days"] >= 30])
    
    with col1:
        st.metric("🔴 Critical (< 7 days)", urgent_count, "Schedule NOW")
    with col2:
        st.metric("🟡 Warning (7-30 days)", warning_count, "Plan service")
    with col3:
        st.metric("🟢 Healthy (30+ days)", healthy_count, "No action needed")
    with col4:
        est_savings = urgent_count * 2500
        st.metric("Est. Downtime Prevented", f"${est_savings:,.0f}", "This month")
    
    st.markdown("---")
    
    col_l, col_r = st.columns([2, 1])
    with col_l:
        fig_pred = go.Figure()
        bins = [0, 7, 14, 30, 60, 90, 180]
        labels = ["0-7d", "7-14d", "14-30d", "30-60d", "60-90d", "90+d"]
        atm_df["failure_bucket"] = pd.cut(atm_df["predicted_failure_days"], bins=bins, labels=labels)
        bucket_counts = atm_df["failure_bucket"].value_counts().sort_index()
        
        colors = ["#ff4444", "#FF9800", "#FFC107", "#8BC34A", "#4CAF50", "#2E7D32"]
        fig_pred.add_trace(go.Bar(x=bucket_counts.index.astype(str), y=bucket_counts.values, marker_color=colors))
        fig_pred.update_layout(title="Predicted Failure Timeline — ATM Distribution", template="plotly_dark", height=350, xaxis_title="Predicted Failure Window", yaxis_title="Number of ATMs")
        st.plotly_chart(fig_pred, use_container_width=True)
    
    with col_r:
        st.markdown("#### Top Risk Factors")
        risk_factors = pd.DataFrame({
            "Factor": ["Days Since Service", "Transaction Volume Spike", "Error Rate Increase", "Cash Jam Frequency", "Environmental (Temp/Humidity)"],
            "Weight": [0.35, 0.25, 0.20, 0.12, 0.08]
        })
        fig_pie = px.pie(risk_factors, names="Factor", values="Weight", color_discrete_sequence=px.colors.sequential.Blues_r, hole=0.4)
        fig_pie.update_layout(template="plotly_dark", height=350, showlegend=True)
        st.plotly_chart(fig_pie, use_container_width=True)
    
    st.markdown("### Service Recommendations")
    urgent_atms = atm_df[atm_df["predicted_failure_days"] < 14].sort_values("predicted_failure_days").head(10)
    for _, atm in urgent_atms.iterrows():
        color = "#ff4444" if atm["predicted_failure_days"] < 7 else "#FF9800"
        st.markdown(f"""
        <div class="prediction-card">
            <strong style="color: {color};">{atm['atm_id']}</strong> — {atm['city']} ({atm['bank_client']})
            <br>Model: {atm['model']} | Last Service: {atm['last_service']} | 
            <strong style="color: {color};">Predicted failure in {atm['predicted_failure_days']} days</strong>
        </div>
        """, unsafe_allow_html=True)

with tab5:
    st.markdown("### 📈 Executive Analytics Dashboard")
    st.markdown("*Self-service analytics for leadership — no SQL required.*")
    
    time_range = st.selectbox("Time Range", ["Last 24 Hours", "Last 7 Days", "Last 30 Days", "Last Quarter"], index=1)
    
    col1, col2 = st.columns(2)
    with col1:
        fig_revenue = go.Figure()
        days = pd.date_range(end=datetime.now(), periods=30)
        daily_vol = np.cumsum(np.random.uniform(150000, 250000, 30))
        fig_revenue.add_trace(go.Scatter(x=days, y=daily_vol, fill="tozeroy", fillcolor="rgba(41,181,232,0.2)", line=dict(color="#29B5E8", width=2)))
        fig_revenue.update_layout(title="Cumulative Transaction Volume (30 Days)", template="plotly_dark", height=300, yaxis_title="$ Volume")
        st.plotly_chart(fig_revenue, use_container_width=True)
    
    with col2:
        fig_uptime = go.Figure()
        uptime_trend = [97.2, 97.5, 97.8, 97.4, 98.0, 98.2, 97.9, 98.1, 98.4, 98.3, 98.5, 98.6, 98.4, 98.7, 98.5, 98.8, 98.6, 98.9, 98.7, 99.0, 98.8, 99.1, 98.9, 99.0, 99.1, 99.2, 99.0, 99.1, 99.2, 99.3]
        fig_uptime.add_trace(go.Scatter(x=days, y=uptime_trend, line=dict(color="#4CAF50", width=2), fill="tozeroy", fillcolor="rgba(76,175,80,0.1)"))
        fig_uptime.add_hline(y=99.0, line_dash="dash", line_color="#FF9800", annotation_text="SLA Target: 99%")
        fig_uptime.update_layout(title="Network Uptime Trend (30 Days)", template="plotly_dark", height=300, yaxis_title="Uptime %", yaxis_range=[96, 100])
        st.plotly_chart(fig_uptime, use_container_width=True)
    
    col1, col2 = st.columns(2)
    with col1:
        bank_summary = atm_df.groupby("bank_client").agg({
            "atm_id": "count",
            "daily_transactions": "sum",
            "uptime_pct": "mean",
            "cash_level_pct": "mean"
        }).reset_index()
        bank_summary.columns = ["Bank Client", "ATMs", "Daily Transactions", "Avg Uptime %", "Avg Cash Level %"]
        bank_summary = bank_summary.sort_values("Daily Transactions", ascending=False)
        st.markdown("#### Performance by Bank Client")
        st.dataframe(bank_summary, use_container_width=True, hide_index=True)
    
    with col2:
        model_perf = atm_df.groupby("model").agg({
            "uptime_pct": "mean",
            "predicted_failure_days": "mean",
            "daily_transactions": "mean"
        }).reset_index()
        model_perf.columns = ["Model", "Avg Uptime %", "Avg Days to Failure", "Avg Daily Tx"]
        st.markdown("#### Performance by ATM Model")
        st.dataframe(model_perf, use_container_width=True, hide_index=True)
        
        fig_model = px.scatter(atm_df, x="uptime_pct", y="daily_transactions", color="model", 
                               template="plotly_dark", height=300, title="Uptime vs. Transaction Volume by Model",
                               color_discrete_sequence=["#29B5E8", "#4CAF50", "#FF9800"])
        st.plotly_chart(fig_model, use_container_width=True)

st.markdown("---")
st.markdown("""
<div style="background: linear-gradient(135deg, #0d1b2e 0%, #1a2744 100%); padding: 2rem; border-radius: 12px; text-align: center; border: 1px solid #29B5E8;">
    <h3 style="color: #29B5E8;">This is what's possible with Snowflake.</h3>
    <p style="color: #e0e0e0; font-size: 1.1rem;">Real-time monitoring • AI anomaly detection • Natural language queries • Predictive maintenance • Multi-tenant sharing</p>
    <p style="color: #a0a0a0;">All from a single platform. No additional infrastructure. Production-ready in 8 weeks.</p>
</div>
""", unsafe_allow_html=True)
st.caption("Interactive Demo | Snowflake ATM Intelligence Hub | Prepared for Diebold Nixdorf | May 2026")
