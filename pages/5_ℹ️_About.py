import streamlit as st
import pandas as pd

st.title("ℹ️ About the Project")

st.markdown("""
## Medical Appointment Demand Forecasting

This project analyzes historical medical appointment data to understand
appointment demand patterns and develop time-series forecasting models
for predicting future appointment demand.
""")

st.subheader("🎯 Project Objective")

st.markdown("""
The main objectives of this project are:

- Analyze historical medical appointment demand.
- Identify trends, seasonality and recurring demand patterns.
- Examine the stationarity of the appointment time series.
- Establish baseline forecasting models.
- Develop and evaluate SARIMA-based forecasting models.
- Compare forecasting models using multiple evaluation metrics.
- Generate future appointment demand forecasts.
- Provide an interactive Streamlit application for exploring the analysis and forecasts.
""")

st.subheader("📊 Dataset")

st.markdown("""
The dataset contains medical appointment records along with patient,
appointment and environmental attributes.

The available variables include:

- Patient demographic information
- Appointment date and time
- Medical and patient-related characteristics
- Appointment-related features
- No-show information
- Weather-related variables such as temperature and rainfall
- Calendar features such as month and weekday
""")

st.markdown("""
### Forecasting Target

For time-series forecasting, individual appointment records were
aggregated by `appointment_date_continuous`.

This produced the daily demand series:

**appointment_count = number of appointments recorded on each day**
""")

st.subheader("🔧 Data Preparation")

st.markdown("""
The original appointment-level dataset was transformed into a daily
time-series dataset.

The main steps were:

1. Clean and prepare the appointment data.
2. Convert the appointment date into datetime format.
3. Group appointment records by appointment date.
4. Calculate the number of appointments for each date.
5. Create a continuous daily time index.
6. Use the resulting `appointment_count` as the forecasting target.
7. Create calendar-based features for exploratory analysis.
8. Aggregate demand by month and year to examine recurring patterns.
""")

st.subheader("🔎 Exploratory Data Analysis")

st.markdown("""
The exploratory analysis examined:

- Daily appointment demand over time
- Monthly appointment demand
- Year-over-year monthly patterns
- Rolling mean and rolling standard deviation
- Weekly patterns
- Seasonal behavior
- Periods of unusually high or low demand
""")

st.subheader("📈 Stationarity Analysis")

st.markdown("""
Stationarity was examined using rolling statistics and time-series
diagnostics.

The rolling mean and rolling standard deviation were compared over
different window sizes to understand whether the statistical properties
of the series changed over time.

Differencing was then considered as part of the SARIMA modelling process
where required.
""")

st.subheader("🔮 Forecasting Methodology")
st.markdown("""
The forecasting workflow follows a time-series modelling approach:

1. Historical appointment records were aggregated into daily demand.
2. The resulting time series was divided into training and testing periods.
3. Baseline forecasting methods were established for comparison.
4. ARIMA and SARIMA models were evaluated.
5. Walk-forward validation was used to evaluate forecasting performance
   while respecting the chronological order of the observations.
6. Models were compared using multiple error metrics.
7. Residual diagnostics were performed on the selected SARIMA approach.
8. The final model was used to generate future appointment demand forecasts.
""")

st.subheader("🤖 Models Evaluated")

model_data = {
    "Model": [
        "Naive Forecast",
        "Seasonal Naive",        
        "7-Day Moving Average",
        "ARIMA",
        "SARIMA",
        "SARIMA + Exogenous Variables",
        "SARIMA Walk-Forward"
    ],
    "Purpose": [
        "Uses the most recent observed demand",
        "Uses demand from a previous seasonal period",
        "Uses the recent 7-day average",
        "Models non-seasonal time-series patterns",
        "Models trend and seasonal time-series patterns",
        "Adds external variables to SARIMA",
        "Evaluates SARIMA through sequential forecasting"
    ]
}

st.dataframe(
    pd.DataFrame(model_data),
    hide_index=True,
    use_container_width=True
)

st.markdown("""
### Why SARIMA?

SARIMA was considered because the appointment demand series exhibits
recurring temporal patterns. Unlike a standard ARIMA model, SARIMA can
explicitly represent seasonal behavior through its seasonal components.

The seasonal period was selected based on the observed characteristics
of the daily appointment series.
""")

st.subheader("📏 Model Evaluation")

metrics = pd.DataFrame({
    "Metric": ["MAE", "RMSE", "WAPE", "sMAPE", "R²"],
    "Interpretation": [
        "Average absolute forecasting error",
        "Penalizes larger errors more strongly",
        "Absolute error relative to total actual demand",
        "Symmetric percentage-based error",
        "Explained variation between actual and predicted values"
    ]
})

st.dataframe(
    metrics,
    hide_index=True,
    use_container_width=True
)

st.subheader("🏆 Selected Forecasting Approach")

col1, col2, col3 = st.columns(3)

col1.metric("MAE", "168.6")
col2.metric("RMSE", "254.7")
col3.metric("WAPE", "81.6%")

st.subheader("🧪 Residual Diagnostics")

st.markdown("""
Residual diagnostics were performed to evaluate whether the forecasting
model adequately captured the systematic structure in the time series.

The residual analysis examined:

- Residuals over time
- Residual distribution
- Normal Q-Q plot
- Residual autocorrelation

A useful forecasting model should leave residuals with little remaining
systematic temporal structure.
""")

st.subheader("🌦️ External Variables")

st.markdown("""
Weather variables were also investigated as potential exogenous
variables for SARIMAX modelling.

The variables included:

- Average daily temperature
- Maximum daily temperature
- Average daily rainfall
- Maximum daily rainfall

These variables were aggregated at the daily level before being supplied
to the SARIMAX model.
""")

st.subheader("⚠️ Limitations")

st.markdown("""
The current forecasting system has several limitations:

- The forecasting target is based on historical appointment counts and
  does not directly model individual patient behavior.
- Forecast accuracy depends on the quality and consistency of historical
  appointment records.
- Sudden changes in healthcare demand may not be captured by historical
  time-series patterns.
- External variables such as weather may require future forecasts before
  they can be used operationally.
- The model does not account for every possible factor affecting
  appointment demand, such as changes in clinic capacity, staffing,
  public holidays, policy changes or unexpected events.
- Forecast uncertainty increases as the forecast horizon becomes longer.
""")

st.subheader("🛠️ Technologies Used")

st.markdown("""
### Programming & Analysis

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly

### Statistical Modelling

- Statsmodels
- pmdarima
- Scikit-learn

### Application

- Streamlit

### Development

- Jupyter Notebook
- VS Code
- Git / GitHub
""")

st.subheader("🖥️ Streamlit Application")

st.markdown("""
The Streamlit application is organized into the following sections:

**🏠 Home**
Provides an introduction to the project.

**📊 Overview**
Displays overall appointment demand, daily demand trends and
year-over-year monthly demand.

**📈 Demand Analysis**
Allows users to select a date range and explore appointment demand
for the selected period.

**🤖 Model Performance**
Compares the forecasting models using multiple evaluation metrics.

**🔮 Forecast**
Displays future appointment demand predictions, forecast KPIs,
confidence intervals and downloadable forecast results.

**ℹ️ About**
Provides information about the dataset, methodology, models,
evaluation process and project limitations.
""")

st.subheader("📌 Conclusion")

st.markdown("""
This project demonstrates an end-to-end time-series forecasting workflow
for medical appointment demand.

Historical appointment records were transformed into a daily demand
series, analyzed for temporal patterns and evaluated using multiple
forecasting approaches. SARIMA-based forecasting was then evaluated
through chronological validation and residual diagnostics.

The resulting Streamlit application provides an interactive interface
for exploring historical demand, comparing model performance and
viewing future appointment demand forecasts.
""")