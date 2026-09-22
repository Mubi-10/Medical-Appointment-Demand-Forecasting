import pandas as pd
import streamlit as st
import plotly.express as px


st.title("🤖 Model Performance")

st.markdown(
    """
    Compare the forecasting models developed during the
    demand forecasting analysis.
    """
)


# Load model evaluation results

results = pd.read_csv(
    "data/forecast_results.csv"
)


st.subheader("Model Evaluation Results")

st.dataframe(
    results,
    use_container_width=True
)

st.subheader("MAE Comparison")

fig_mae = px.bar(
    results,
    x='Model',
    y='MAE',
    text='MAE',
    title='Mean Absolute Error'
)

st.plotly_chart(
    fig_mae,
    use_container_width=True
)

st.subheader("RMSE Comparison")

fig_rmse = px.bar(
    results,
    x='Model',
    y='RMSE',
    text='RMSE',
    title='Root Mean Squared Error'
)

st.plotly_chart(
    fig_rmse,
    use_container_width=True
)

st.subheader("WAPE Comparison")

fig_wape = px.bar(
    results,
    x='Model',
    y='WAPE',
    text='WAPE',
    title='Weighted Absolute Percentage Error'
)

st.plotly_chart(
    fig_wape,
    use_container_width=True
)