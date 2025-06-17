import plotly.express as px

def sales_by_category_chart(df):
    chart = px.bar(
        df.groupby('Category')['Sales'].sum().reset_index(),
        x='Category', y='Sales',
        title='Sales by Category',
        color='Category'
    )
    return chart

def sales_by_region_chart(df):
    chart = px.pie(
        df, names='Region', values='Sales',
        title='Sales Distribution by Region'
    )
    return chart

def monthly_sales_chart(df):
    monthly = df.groupby('Month')['Sales'].sum().reset_index().sort_values('Month')
    chart = px.line(
        monthly, x='Month', y='Sales',
        title='Monthly Sales Trend'
    )
    return chart