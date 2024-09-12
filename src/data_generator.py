import pandas as pd
import numpy as np
from faker import Faker

def generate_data():
    fake = Faker()

    products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
    regions = ['North', 'South', 'East', 'West']
    months = list(range(1, 13))
    years = list(range(2018, 2024))

    data = []
    for year in years:
        for month in months:
            for product in products:
                for region in regions:
                    sales_base = np.random.uniform(5000, 30000)  # Base sales for each product/region combo
                    variability_factor = np.random.uniform(0.7, 1.3)  # Adding some randomness to sales
                    sales = sales_base * variability_factor
                    data.append([product, region, year, month, round(sales, 2)])

    df = pd.DataFrame(data, columns=['Product', 'Region', 'Year', 'Month', 'Sales'])
    return df
