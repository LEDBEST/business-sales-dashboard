from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd

def analyze_sales_by_region(df):
    return df.groupby(['Region', 'Product']).agg({'Sales': 'sum'}).reset_index()

def analyze_kpi(df):
    total_sales = df['Sales'].sum()
    avg_sales_per_order = df['Sales'].mean()
    total_orders = len(df)
    return {
        "Total Sales": total_sales,
        "Average Sales per Order": avg_sales_per_order,
        "Total Orders": total_orders
    }

def analyze_forecast(df):
    df['Year'] = pd.DatetimeIndex(df['Year']).year
    yearly_sales = df.groupby('Year').agg({'Sales': 'sum'}).reset_index()

    X = yearly_sales['Year'].values.reshape(-1, 1)
    y = yearly_sales['Sales'].values

    model = LinearRegression()
    model.fit(X, y)

    future_years = np.arange(df['Year'].max() + 1, df['Year'].max() + 6).reshape(-1, 1)
    future_sales = model.predict(future_years)

    forecast_df = pd.DataFrame({'Year': future_years.flatten(), 'Sales Forecast': future_sales})
    return forecast_df
