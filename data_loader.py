import pandas as pd
import streamlit as st

@st.cache_data
def load_data(path='data/Superstore.csv'):
    df = pd.read_csv(path, encoding='ISO-8859-1', parse_dates=['Order Date', 'Ship Date'])
    df['Ship_Days'] = (df['Ship Date'] - df['Order Date']).dt.days
    df['Month'] = df['Order Date'].dt.to_period('M').astype(str)
    return df
