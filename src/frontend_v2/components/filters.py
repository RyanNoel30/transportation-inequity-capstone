import streamlit as st

def filter_panel(df):
    st.sidebar.header("Filters")

    region = st.sidebar.selectbox(
        "Select Region:",
        options=["All"] + sorted(df["region"].unique())
    )
    
    income_range = st.sidebar.selectbox(
        "Income Level:",
        options=["All"] + sorted(df["income_category"].unique())
    )

    transport_mode = st.sidebar.multiselect(
        "Transportation Mode:",
        options=sorted(df["transportation_mode"].unique()),
        default=None
    )

    return region, income_range, transport_mode
