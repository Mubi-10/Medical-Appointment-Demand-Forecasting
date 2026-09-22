import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Medical Appointment Demand Forecasting",
    page_icon="🏥",
    layout="wide"
)

# Main title
st.title("🏥 Medical Appointment Demand Forecasting")

# Project introduction
st.markdown("""
This application analyzes historical medical appointment demand
and evaluates forecasting models to support future demand planning.
""")

st.divider()

# Project overview
st.subheader("📌 Project Overview")

st.markdown("""
The project focuses on understanding historical appointment demand
and forecasting future demand using time-series forecasting techniques.

### Key areas of analysis

- 📊 **Demand Analysis** – Explore historical appointment patterns
- 🤖 **Model Performance** – Compare forecasting models using evaluation metrics
- 📈 **Forecast** – View future appointment demand forecasts
- ℹ️ **About** – Project methodology, dataset, and limitations
""")

st.divider()

# Navigation instruction
st.info(
    "Use the sidebar to navigate through the different sections of the application."
)