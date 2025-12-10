import pandas as pd
import os
import streamlit as st

def load_processed_data():
    file_path = os.path.join("src", "data", "processed", "transportation_inequity.csv")
    
    st.write("🔍 Attempting to load:", os.path.abspath(file_path))

    if not os.path.exists(file_path):
        st.error(f"❌ File not found at: {os.path.abspath(file_path)}")
        raise FileNotFoundError("Processed data file not found.")
    
    st.success("✅ File loaded successfully!")
    return pd.read_csv(file_path)
