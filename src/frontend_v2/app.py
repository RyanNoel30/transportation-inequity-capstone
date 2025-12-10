import streamlit as st
import pandas as pd
import numpy as np

from utils.load_data import load_processed_data
from utils.theme import set_streamlit_theme
from components.filters import filter_panel
from components.charts import commute_time_chart, cost_burden_bar
from components.maps import commute_map

# ================================
#   ANALYSIS FUNCTIONS
# ================================

def get_longest_commute(df):
    grouped = df.groupby("region")["commute_time"].mean().sort_values(ascending=False)
    longest = grouped.head(5)
    return longest

def income_race_transportation_access(df):
    access = (
        df.groupby(["income_category", "race", "urban_rural"])["public_transit_access_score"]
        .mean()
        .reset_index()
        .sort_values("public_transit_access_score", ascending=False)
    )
    return access

def most_least_affordable(df):
    county_cost = (
        df.groupby("county")["transportation_cost_burden"]
        .mean()
        .sort_values()
    )
    most_affordable = county_cost.head(5)
    least_affordable = county_cost.tail(5)
    return most_affordable, least_affordable

def transit_vs_jobs(df):
    summary = df.groupby("region")[["public_transit_access_score", "job_access_index", "commute_time"]].mean()
    summary["job_access_rank"] = summary["job_access_index"].rank(ascending=False)
    summary["transit_rank"] = summary["public_transit_access_score"].rank(ascending=False)
    summary["commute_rank"] = summary["commute_time"].rank()
    return summary.sort_values("transit_rank")

def commute_trends(df):
    if "year" not in df.columns:
        return None
    return df.groupby("year")["commute_time"].mean().reset_index()


# ================================
#   STREAMLIT APP
# ================================

set_streamlit_theme()

st.title("🚦 Transportation Inequity & Commute Burden Dashboard")

# Load Data
df = load_processed_data()

# Sidebar filters
region, income_range, transport_mode = filter_panel(df)

# Apply filters
filtered_df = df.copy()

if region != "All":
    filtered_df = filtered_df[df["region"] == region]

if income_range != "All":
    filtered_df = filtered_df[df["income_category"] == income_range]

if transport_mode:
    filtered_df = filtered_df[filtered_df["transportation_mode"].isin(transport_mode)]

# Display metrics
st.header("Key Metrics")

col1, col2, col3 = st.columns(3)
col1.metric("Avg Commute Time", f"{filtered_df['commute_time'].mean():.1f} min")
col2.metric("Avg Cost Burden", f"{filtered_df['transportation_cost_burden'].mean():.1f}%")
col3.metric("Total Records", len(filtered_df))

st.divider()

# ====================================
#   MAIN CHARTS
# ====================================

st.subheader("Commute Time Across Transportation Modes")
commute_time_chart(filtered_df)

st.subheader("Transportation Cost Burden by Region")
cost_burden_bar(filtered_df)

commute_map(filtered_df)

st.divider()

# ====================================
#        INSIGHTS SECTION
# ====================================

st.header("📊 Data Insights & Answers to Key Questions")

# 1. Longest commute communities
st.subheader("1. Which communities experience the longest commute times?")
longest = get_longest_commute(df)
st.write("Regions with the longest average commute times:")
st.dataframe(longest)
st.write(f"**Top region with the longest commute:** {longest.index[0]} — {longest.iloc[0]:.1f} mins")

# 2. How do income, race, and urban/rural affect transportation access?
st.subheader("2. How do income, race/ethnicity, and urban–rural status affect transportation access?")
access = income_race_transportation_access(df)
st.write("Groups ranked by public transit access:")
st.dataframe(access.head(10))

# Narrative Insight
best_group = access.iloc[0]
st.write(
    f"➡️ **Highest transit access:** {best_group['income_category']} income, {best_group['race']} residents living in {best_group['urban_rural']} areas."
)

# 3. Most vs least affordable transportation counties
st.subheader("3. Which counties are most vs. least affordable?")
most_affordable, least_affordable = most_least_affordable(df)
colA, colB = st.columns(2)

with colA:
    st.write("### 🟢 Most Affordable (Lowest Cost Burden)")
    st.dataframe(most_affordable)

with colB:
    st.write("### 🔴 Least Affordable (Highest Cost Burden)")
    st.dataframe(least_affordable)

# 4. Impact of public transit on jobs & opportunity
st.subheader("4. How does transit access influence job reach & economic opportunity?")
transit_jobs = transit_vs_jobs(df)
st.dataframe(transit_jobs)

top_region = transit_jobs.index[0]
st.write(
    f"➡️ **Region with best public transit & job access alignment:** {top_region}"
)

# 5. Commute burden trends over time
st.subheader("5. Are commute burdens increasing or decreasing over time?")
trend = commute_trends(df)

if trend is not None:
    st.line_chart(trend.set_index("year"))
    trend_direction = "increasing 📈" if trend["commute_time"].iloc[-1] > trend["commute_time"].iloc[0] else "decreasing 📉"
    st.write(f"➡️ Overall commute burden is **{trend_direction}** over time.")
else:
    st.info("No 'year' column found — commute trends cannot be calculated.")

st.caption("Generated automatically from processed transportation inequality dataset.")
