import pandas as pd
import streamlit as st
import plotly.graph_objects as go


# ==================================================
# PAGE TITLE
# ==================================================

st.title("📈 Medical Appointment Demand Forecast")

st.markdown(
    """
    This page presents future medical appointment demand
    predicted using the selected SARIMA forecasting model.
    """
)


# ==================================================
# LOAD HISTORICAL DATA
# ==================================================

daily_demand = pd.read_csv(
    "data/daily_demand.csv"
)

daily_demand['appointment_date_continuous'] = pd.to_datetime(
    daily_demand['appointment_date_continuous']
)


# ==================================================
# LOAD FUTURE FORECAST
# ==================================================

future_forecast = pd.read_csv(
    "data/future_forecast.csv"
)

future_forecast['forecast_date'] = pd.to_datetime(
    future_forecast['forecast_date']
)


# ==================================================
# FORECAST CONTROLS
# ==================================================

st.subheader("Forecast Controls")

max_forecast_days = len(future_forecast)

forecast_days = st.slider(
    "Select Forecast Horizon (days)",
    min_value=7,
    max_value=max_forecast_days,
    value=7,
    step=1
)


selected_forecast = future_forecast.head(
    forecast_days
)


# ==================================================
# KPI CALCULATIONS
# ==================================================

average_forecast = (
    selected_forecast['forecast'].mean()
)

peak_forecast = (
    selected_forecast['forecast'].max()
)

peak_date = selected_forecast.loc[
    selected_forecast['forecast'].idxmax(),
    'forecast_date'
]


# ==================================================
# KPI CARDS
# ==================================================

col1, col2, col3 = st.columns(3)

col1.metric(
    "Forecast Horizon",
    f"{forecast_days} days"
)

col2.metric(
    "Average Forecast",
    f"{average_forecast:,.0f}"
)

col3.metric(
    "Peak Forecast",
    f"{peak_forecast:,.0f}"
)


st.caption(
    f"Forecast period: "
    f"{selected_forecast['forecast_date'].min().strftime('%d %b %Y')} "
    f"to "
    f"{selected_forecast['forecast_date'].max().strftime('%d %b %Y')}"
)


# ==================================================
# HISTORICAL VS FORECAST
# ==================================================

st.subheader("Historical Demand vs Forecast")

fig = go.Figure()


# Historical demand

fig.add_trace(
    go.Scatter(
        x=daily_demand['appointment_date_continuous'],
        y=daily_demand['appointment_count'],
        mode='lines',
        name='Historical Demand'
    )
)


# Forecast

fig.add_trace(
    go.Scatter(
        x=selected_forecast['forecast_date'],
        y=selected_forecast['upper_ci'],
        mode='lines',
        line=dict(width=0),
        showlegend=False
    )
)

fig.add_trace(
    go.Scatter(
        x=selected_forecast['forecast_date'],
        y=selected_forecast['lower_ci'],
        mode='lines',
        line=dict(width=0),
        fill='tonexty',
        name='95% Confidence Interval'
    )
)


fig.update_layout(
    title="Medical Appointment Demand Forecast",
    xaxis_title="Date",
    yaxis_title="Appointments",
    hovermode="x unified"
)


st.plotly_chart(
    fig,
    use_container_width=True
)


# ==================================================
# FORECAST TABLE
# ==================================================

st.subheader("Forecast Details")

display_forecast = selected_forecast.copy()

display_forecast['forecast_date'] = (
    display_forecast['forecast_date']
    .dt.strftime('%Y-%m-%d')
)

display_forecast['forecast'] = (
    display_forecast['forecast']
    .round(0)
    .astype(int)
)

display_forecast = display_forecast.rename(
    columns={
        'forecast_date': 'Date',
        'forecast': 'Predicted Appointments'
    }
)


st.dataframe(
    display_forecast,
    use_container_width=True,
    hide_index=True
)


# ==================================================
# DOWNLOAD
# ==================================================

csv = display_forecast.to_csv(
    index=False
).encode('utf-8')


st.download_button(
    label="⬇️ Download Forecast",
    data=csv,
    file_name="appointment_forecast.csv",
    mime="text/csv"
)