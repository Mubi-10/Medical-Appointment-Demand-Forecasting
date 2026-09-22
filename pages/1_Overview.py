import pandas as pd
import streamlit as st

daily_demand = pd.read_csv(
    "data/daily_demand.csv"
)

daily_demand['appointment_date_continuous'] = pd.to_datetime(
    daily_demand['appointment_date_continuous']
)

total_appointments = daily_demand['appointment_count'].sum()
average_daily = daily_demand['appointment_count'].mean()
peak_demand = daily_demand['appointment_count'].max()

results = pd.read_csv(
    "data/forecast_results.csv"
)

best_model = results.loc[
    results['MAE'].idxmin(),
    'Model'
]

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Appointments",
    f"{total_appointments:,.0f}"
)

col2.metric(
    "Average Daily Demand",
    f"{average_daily:,.0f}"
)

col3.metric(
    "Peak Daily Demand",
    f"{peak_demand:,.0f}"
)

col4.metric(
    "Best Model",
    best_model
)

st.subheader("Daily Appointment Demand")

st.line_chart(
    daily_demand.set_index(
        'appointment_date_continuous'
    )['appointment_count']
)


# Monthly Demand Section
monthly_demand = daily_demand.copy()

monthly_demand['Month'] = (
    monthly_demand['appointment_date_continuous']
    .dt.month
)

monthly_demand['Year'] = (
    monthly_demand['appointment_date_continuous']
    .dt.year
)

monthly = (
    monthly_demand
    .groupby(['Year', 'Month'])['appointment_count']
    .sum()
    .reset_index()
)

import plotly.express as px

fig = px.line(
    monthly,
    x='Month',
    y='appointment_count',
    color='Year',
    markers=True,
    title='Year-over-Year Monthly Appointment Demand'
)

st.plotly_chart(
    fig,
    use_container_width=True
)