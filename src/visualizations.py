import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def plot_sales_forecast(forecast_df):
    fig, ax = plt.subplots(figsize=(5, 3))
    ax.plot(forecast_df['Year'], forecast_df['Sales Forecast'], marker='o', linestyle='--')
    ax.set_title('Sales Forecast', fontsize=12)
    ax.set_xlabel('Year')
    ax.set_ylabel('Sales Forecast')
    ax.grid(True)
    st.pyplot(fig)

def plot_sales_by_region(df):
    fig, ax = plt.subplots(figsize=(5, 3))
    sns.lineplot(x='Month', y='Sales', hue='Region', data=df, ci=None, marker='o', ax=ax)
    ax.set_title('Monthly Sales by Region', fontsize=12)
    ax.set_xlabel('Month')
    ax.set_ylabel('Sales')
    ax.grid(True)
    st.pyplot(fig)

def plot_sales_trend(df):
    fig, ax = plt.subplots(figsize=(5, 3))
    sns.lineplot(x='Year', y='Sales', data=df, ci=None, marker='o', ax=ax)
    ax.set_title('Yearly Sales Trend', fontsize=12)
    ax.set_xlabel('Year')
    ax.set_ylabel('Sales')
    ax.grid(True)
    st.pyplot(fig)

def plot_sales_by_product(df):
    fig, ax = plt.subplots(figsize=(5, 3))
    sns.barplot(x='Product', y='Sales', data=df, ci=None, ax=ax)
    ax.set_title('Total Sales by Product', fontsize=12)
    ax.set_xlabel('Product')
    ax.set_ylabel('Sales')
    ax.grid(True)
    st.pyplot(fig)

def plot_pie_chart(df, column, title):
    fig, ax = plt.subplots(figsize=(5, 3))
    counts = df[column].value_counts()
    ax.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
    ax.set_title(title, fontsize=12)
    st.pyplot(fig)
