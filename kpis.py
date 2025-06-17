def compute_kpis(df):
    return {
        'Total Sales': df['Sales'].sum(),
        'Total Profit': df['Profit'].sum(),
        'Order Count': df['Order ID'].nunique(),
        'Avg Ship Days': df['Ship_Days'].mean()
    }
