import streamlit as st
from src.data_loader import load_data
from src.kpis import compute_kpis
from src.charts import (
    sales_by_category_chart,
    sales_by_region_chart,
    monthly_sales_chart,
)

st.set_page_config(layout='wide', page_title='Superstore Sales Dashboard')

st.title("📊 Superstore Sales Dashboard")

# Load and filter data
df = load_data('data/Superstore.csv')

# Sidebar filters
regions = st.sidebar.multiselect("Select Region(s):", df['Region'].unique(), default=df['Region'].unique())
df_filtered = df[df['Region'].isin(regions)]

# KPIs
kpis = compute_kpis(df_filtered)
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Sales", f"${kpis['Total Sales']:,.2f}")
col2.metric("Total Profit", f"${kpis['Total Profit']:,.2f}")
col3.metric("Order Count", kpis['Order Count'])
col4.metric("Avg Ship Days", f"{kpis['Avg Ship Days']:.1f}")

st.divider()

# Charts
st.plotly_chart(sales_by_category_chart(df_filtered), use_container_width=True)
st.plotly_chart(sales_by_region_chart(df_filtered), use_container_width=True)
st.plotly_chart(monthly_sales_chart(df_filtered), use_container_width=True)
