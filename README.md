# 🏥 Medical Appointment Demand Forecasting

> Time-series analysis and forecasting of daily medical appointment demand using Python, SARIMA, and Streamlit.

---

## 📌 Project Overview

Healthcare facilities need to anticipate patient appointment demand
to support effective resource and capacity planning.

This project analyzes historical medical appointment data to identify
demand patterns, trends, seasonality, and variability, and applies
time-series forecasting techniques to estimate future appointment demand.

The project includes:

- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Feature engineering
- Time-series analysis
- Forecasting model development
- Model evaluation
- Future demand forecasting
- Interactive Streamlit dashboard

## 🎯 Problem Statement

The objective of this project is to analyze historical medical
appointment records and develop a time-series forecasting solution
that can estimate future daily appointment demand.

The analysis aims to identify:

- Historical demand trends
- Weekly and yearly seasonality
- Demand fluctuations
- High and low demand periods
- Forecasting performance of different models
- Future appointment demand

## 📊 Dataset

The project uses historical medical appointment records containing
information related to appointments, patients, appointment timing,
weather conditions, and other relevant attributes.

The appointment-level data was aggregated by appointment date
to create a daily time-series dataset, where each observation
represents the total number of appointments recorded on a given day.

### Target Variable

`appointment_count`

represents the total number of appointments recorded on each day.

### Important Features

- Appointment date
- Appointment time
- Specialty
- Gender
- Age
- Medical conditions
- Appointment shift
- Weather-related variables
- Month
- Weekday
- No-show information

### Time-Series Dataset

The forecasting dataset contains:

| Column | Description |
|---|---|
| `appointment_date_continuous` | Appointment date |
| `appointment_count` | Number of appointments on that date |

## 🔄 Project Workflow

1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis
4. Feature Engineering
5. Daily Demand Aggregation
6. Time-Series Analysis
7. Forecasting Model Development
8. Model Evaluation
9. Residual Diagnostics
10. Future Demand Forecasting
11. Streamlit Dashboard Development

## 🧹 Data Cleaning

The data preprocessing stage included:

- Handling missing values
- Converting date/time columns into appropriate formats
- Checking duplicate records
- Standardizing categorical variables
- Creating derived variables
- Encoding relevant categorical/target variables
- Preparing the dataset for analysis and modeling

## 🔍 Exploratory Data Analysis

EDA was performed to understand appointment demand patterns and
identify important trends and variations.

The analysis included:

- Daily appointment demand
- Monthly appointment demand
- Year-over-year demand patterns
- Day-of-week demand
- Appointment timing
- Specialty distribution
- No-show patterns
- Weather-related patterns
- Rolling mean and rolling standard deviation
- Demand variability

## 📈 Time-Series Analysis

Daily appointment demand was analyzed as a time series.

Rolling statistics were used to investigate changes in demand level
and variability over time.

The analysis identified a pronounced weekly pattern in daily
appointment demand.

A seasonal period of:

`m = 7`

was therefore used for models incorporating weekly seasonality.

### Train-Test Split

The time series was divided chronologically:

- Training period: January 2020 – February 2021
- Testing period: February 2021 – May 2021

The chronological split ensures that observations from the test
period are not used to fit the forecasting model.

## 🤖 Forecasting Models

Several forecasting approaches were evaluated:

- Naive Forecast
- Seasonal Naive Forecast
- 7-Day Moving Average
- ARIMA
- SARIMA
- SARIMAX with exogenous variables

### SARIMA

SARIMA was used to model both non-seasonal and seasonal patterns
in daily appointment demand.

The seasonal component was configured with a 7-day period to
capture weekly appointment-demand patterns.

## 📏 Model Evaluation

Forecasting models were evaluated using:

- MAE — Mean Absolute Error
- RMSE — Root Mean Squared Error
- WAPE — Weighted Absolute Percentage Error
- sMAPE — Symmetric Mean Absolute Percentage Error
- R² — Coefficient of Determination

## 🩺 Residual Diagnostics

Residual analysis was performed to assess whether the forecasting
model adequately captured the underlying time-series structure.

The diagnostics included:

- Residual time-series plot
- Residual distribution
- Q-Q plot
- Residual autocorrelation (ACF)
- Ljung-Box test
- Investigation of large residuals and variability

The diagnostics indicated that the model captured much of the
time-dependent structure, while some large errors and variability
remained during certain periods.

## 🔮 Future Forecast

The final forecasting workflow was used to generate future
appointment-demand estimates.

The forecast results are available in:

`data/future_forecast.csv`

The Streamlit application provides an interactive view of the
forecasted demand.

## 🖥️ Streamlit Dashboard

An interactive Streamlit dashboard was developed to present the
analysis and forecasting results.

### Dashboard Pages

| Page | Description |
|---|---|
| 🏠 Overview | Project summary and overall demand trends |
| 📊 Demand Analysis | Explore demand across selected date ranges |
| 📈 Forecast | View future appointment-demand forecasts |
| 🤖 Model Performance | Compare forecasting models |
| ℹ️ About | Project methodology and information |

## 📸 Dashboard Screenshots

### Overview

![Overview](overview.png)
![Overview](overview_1.png)

### Demand Analysis

![Demand Analysis](demand_analysis.png)

### Forecast

![Forecast](forecast.png)

### Model Performance

![Model Performance](model_performance.png)

---

## 🛠️ Technologies Used

### Programming
- Python

### Data Analysis
- Pandas
- NumPy

### Visualization
- Matplotlib
- Seaborn
- Plotly

### Machine Learning / Forecasting
- Scikit-learn
- Statsmodels
- pmdarima

### Dashboard
- Streamlit

### Development
- Jupyter Notebook
- VS Code
- Git
- GitHub

---

## 💡 Key Findings

- Medical appointment demand shows substantial variation over time.
- A pronounced weekly seasonal pattern is present in daily demand.
- Rolling statistics indicate periods of changing demand and variability.
- Seasonal models using a 7-day period are appropriate for capturing
  weekly demand patterns.
- Forecast errors increase during certain periods containing unusually
  high or low appointment demand.
- Residual diagnostics indicate that the forecasting model captures
  much of the time-dependent structure, although some irregular
  variation remains.

## ⚠️ Limitations

- Forecast accuracy depends on historical demand patterns remaining
  reasonably representative of future demand.
- Sudden external events may produce forecast errors.
- Some demand fluctuations are difficult to capture using statistical
  time-series models alone.
- Future forecasts are estimates and should not be treated as exact
  appointment counts.
- Weather-based forecasting requires availability of the relevant
  information at forecast time.
- The project is intended for analytical and planning purposes and
  is not a clinical decision-making system.

## 🚀 Future Improvements

Possible improvements include:

- Testing additional forecasting models
- Hyperparameter optimization
- Incorporating additional external variables
- Comparing statistical models with machine-learning approaches
- Adding prediction intervals to the dashboard
- Automated model retraining
- Automated forecast updates
- Deployment of the Streamlit application

## ▶️ How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/Mubi-10/Medical-Appointment-Demand-Forecasting.git
cd Medical-Appointment-Demand-Forecasting
