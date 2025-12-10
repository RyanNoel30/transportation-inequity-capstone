import requests
import pandas as pd

BASE_URL = "http://localhost:8000"

def get_commute_stats(params=None):
    r = requests.get(f"{BASE_URL}/commute_stats", params=params)
    r.raise_for_status()
    return pd.DataFrame(r.json())

def get_transportation_modes(params=None):
    r = requests.get(f"{BASE_URL}/transportation_modes", params=params)
    r.raise_for_status()
    return pd.DataFrame(r.json())

def get_cost_burden(params=None):
    r = requests.get(f"{BASE_URL}/cost_burden", params=params)
    r.raise_for_status()
    return pd.DataFrame(r.json())

def get_region_compare(params=None):
    r = requests.get(f"{BASE_URL}/region_compare", params=params)
    r.raise_for_status()
    return pd.DataFrame(r.json())
