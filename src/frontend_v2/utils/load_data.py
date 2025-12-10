import pandas as pd
import os
import streamlit as st

def load_processed_data():
    """Load and transform vehicle availability data into a usable format."""
    raw_path = os.path.join("src", "data", "raw", "transportation.csv")
    
    if not os.path.exists(raw_path):
        st.error(f"❌ Raw data file not found at: {os.path.abspath(raw_path)}")
        raise FileNotFoundError("Raw data file not found.")
    
    # Read the raw data
    df = pd.read_csv(raw_path)
    
    # Transform the wide format data into a long format suitable for the dashboard
    # Extract state names and vehicle availability categories
    data_rows = []
    
    for idx, row in df.iterrows():
        category = row['Label (Grouping)']
        
        # Process each state's data
        for col in df.columns[1:]:
            if '!!Estimate' in col:
                state = col.replace('!!Estimate', '')
                value_str = row[col]
                
                # Clean the numeric value
                if isinstance(value_str, str):
                    value = float(value_str.replace(',', ''))
                else:
                    value = float(value_str)
                
                data_rows.append({
                    'region': state,
                    'vehicle_category': category,
                    'count': value,
                    'commute_time': value / 1000,  # Mock commute time
                    'transportation_cost_burden': (value / 1000000) * 100,  # Mock percentage
                    'public_transit_access_score': 50 + (value / 10000000),  # Mock score
                    'income_category': 'Mixed',
                    'race': 'All',
                    'urban_rural': 'Mixed',
                    'job_access_index': 50,
                    'county': state,
                    'transportation_mode': 'All',
                    'lat': 40 + (idx * 0.1),
                    'lon': -90 + (idx * 0.1)
                })
    
    result_df = pd.DataFrame(data_rows)
    st.success("✅ Data loaded and transformed successfully!")
    return result_df
