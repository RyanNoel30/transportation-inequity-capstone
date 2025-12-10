import plotly.express as px
import streamlit as st

def commute_time_chart(df):
    fig = px.box(
        df,
        x="transportation_mode",
        y="commute_time",
        color="transportation_mode",
        title="Commute Time by Transportation Mode",
    )
    st.plotly_chart(fig, width='stretch')

def cost_burden_bar(df):
    fig = px.bar(
        df.groupby("region")["transportation_cost_burden"].mean().reset_index(),
        x="region",
        y="transportation_cost_burden",
        title="Average Transportation Cost Burden by Region",
        labels={"transportation_cost_burden": "Cost Burden (%)"}
    )
    st.plotly_chart(fig, width='stretch')
