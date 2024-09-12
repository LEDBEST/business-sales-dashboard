import streamlit as st
from src.data_generator import generate_data
from src.visualizations import plot_sales_forecast, plot_sales_by_region, plot_sales_trend, plot_sales_by_product, plot_pie_chart
from src.analysis import analyze_sales_by_region, analyze_forecast, analyze_kpi
import pandas as pd

# Установка конфигурации страницы
st.set_page_config(page_title="Business Sales Dashboard", layout="wide")

# Подключение CSS
with open("assets/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Генерация синтетических данных
df = generate_data()

# Водяной знак
st.markdown('<div class="watermark">Created by Maksym Shapovalov for portfolio website</div>', unsafe_allow_html=True)

st.title("Business Sales Dashboard")
st.write("The data is generated automatically with random variations.")

# Интерактивные фильтры
st.markdown("### Filters")

# Фильтр по продуктам (выпадающий список)
selected_product = st.selectbox("Select Product", options=df['Product'].unique())

# Фильтр по регионам (кнопки-срезы)
regions = df['Region'].unique()
selected_region = st.radio("Filter by Region", options=["All"] + list(regions))

# Фильтр по диапазону лет (ползунок)
years = df['Year'].unique()
selected_year_range = st.slider("Select Year Range", min_value=int(years.min()), max_value=int(years.max()), value=(int(years.min()), int(years.max())))

# Применение фильтров
filtered_df = df[df['Product'] == selected_product]
if selected_region != "All":
    filtered_df = filtered_df[filtered_df['Region'] == selected_region]
filtered_df = filtered_df[(filtered_df['Year'] >= selected_year_range[0]) & (filtered_df['Year'] <= selected_year_range[1])]

# KPI Calculation
kpi_metrics = analyze_kpi(filtered_df)

# Основная панель для графиков
st.markdown("## Key Metrics")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Total Sales", value=f"${kpi_metrics['Total Sales']:,}")
with col2:
    st.metric(label="Average Sales per Order", value=f"${kpi_metrics['Average Sales per Order']:.2f}")
with col3:
    st.metric(label="Total Orders", value=kpi_metrics['Total Orders'])

# Компоновка графиков по сетке с дополнительными стилями
st.markdown("## Sales Visualizations")
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.markdown("### Sales Forecast")
    forecast_df = analyze_forecast(filtered_df)
    plot_sales_forecast(forecast_df)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.markdown("### Sales by Region")
    plot_sales_by_region(filtered_df)
    st.markdown('</div>', unsafe_allow_html=True)

# Вторая строка графиков
col3, col4 = st.columns(2)

with col3:
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.markdown("### Sales Trend")
    plot_sales_trend(filtered_df)
    st.markdown('</div>', unsafe_allow_html=True)

with col4:
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.markdown("### Sales by Product")
    plot_sales_by_product(filtered_df)
    st.markdown('</div>', unsafe_allow_html=True)

# Третья строка графиков
col5, col6 = st.columns(2)

with col5:
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.markdown("### Product Sales Distribution")
    plot_pie_chart(filtered_df, 'Product', 'Product Sales Distribution')
    st.markdown('</div>', unsafe_allow_html=True)

with col6:
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.markdown("### Region Sales Distribution")
    plot_pie_chart(filtered_df, 'Region', 'Region Sales Distribution')
    st.markdown('</div>', unsafe_allow_html=True)
