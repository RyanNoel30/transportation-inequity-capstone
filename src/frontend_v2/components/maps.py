import pydeck as pdk
import streamlit as st

def commute_map(df):
    st.subheader("Geographic Distribution of Commute Burden")
    
    # Check if lat/lon columns exist
    if "lat" not in df.columns or "lon" not in df.columns:
        st.info("Geographic data not available. Please load data with location information.")
        return
    
    # Handle missing values
    map_df = df.dropna(subset=["lat", "lon"])
    
    if len(map_df) == 0:
        st.warning("No valid geographic data found.")
        return

    view_state = pdk.ViewState(latitude=map_df["lat"].mean(), longitude=map_df["lon"].mean(), zoom=9)

    layer = pdk.Layer(
        "ScatterplotLayer",
        map_df,
        get_position=["lon", "lat"],
        get_radius=300,
        get_color="[200, 30, 0, 160]",
        pickable=True
    )

    deck = pdk.Deck(
        layers=[layer],
        initial_view_state=view_state,
        tooltip={"text": "{region}\nCommute Time: {commute_time} mins"}
    )

    st.pydeck_chart(deck)
