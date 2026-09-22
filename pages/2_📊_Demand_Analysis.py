import pandas as pd
import streamlit as st
import plotly.express as px


# --------------------------------------------------
# PAGE TITLE
# --------------------------------------------------

st.title("📊 Demand Analysis")

st.markdown(
    """
    Analyze historical medical appointment demand
    across different time periods.
    """
)


# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

daily_demand = pd.read_csv(
    "data/daily_demand.csv"
)


# --------------------------------------------------
# DATA PREPARATION
# --------------------------------------------------

daily_demand['appointment_date_continuous'] = pd.to_datetime(
    daily_demand['appointment_date_continuous']
)


# --------------------------------------------------
# DATE RANGE FILTER
# --------------------------------------------------

min_date = daily_demand['appointment_date_continuous'].min()
max_date = daily_demand['appointment_date_continuous'].max()


date_range = st.date_input(
    "Select Date Range",
    [min_date.date(), max_date.date()],
    min_value=min_date.date(),
    max_value=max_date.date()
)


# Make sure user selected both dates
if len(date_range) == 2:

    start_date = pd.to_datetime(date_range[0])
    end_date = pd.to_datetime(date_range[1])

    filtered_data = daily_demand[
        (daily_demand['appointment_date_continuous'] >= start_date) &
        (daily_demand['appointment_date_continuous'] <= end_date)
    ].copy()

    st.subheader("Filtered Appointment Demand")

    st.line_chart(
    filtered_data.set_index(
        'appointment_date_continuous'
    )['appointment_count']
)

    # --------------------------------------------------
    # KPI SECTION
    # --------------------------------------------------

    total_appointments = filtered_data['appointment_count'].sum()

    average_daily = filtered_data['appointment_count'].mean()

    peak_demand = filtered_data['appointment_count'].max()

    days_analyzed = len(filtered_data)


    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
    "Total Appointments",
    f"{filtered_data['appointment_count'].sum():,.0f}"
    )

    col2.metric(
    "Average Daily Demand",
    f"{filtered_data['appointment_count'].mean():,.0f}"
    )

    col3.metric(
    "Peak Daily Demand",
    f"{filtered_data['appointment_count'].max():,.0f}"
    )

    col4.metric(
        "Days Analyzed",
        f"{days_analyzed:,}"
    )


    # --------------------------------------------------
    # DAILY DEMAND
    # --------------------------------------------------

    st.subheader("Daily Appointment Demand")


    fig_daily = px.line(
        filtered_data,
        x='appointment_date_continuous',
        y='appointment_count',
        markers=True,
        labels={
            'appointment_date_continuous': 'Date',
            'appointment_count': 'Appointments'
        }
    )

  
    fig_daily.update_layout(
        xaxis_title="Date",
        yaxis_title="Appointments"
    )


    st.plotly_chart(
        fig_daily,
        use_container_width=True
    )


    # --------------------------------------------------
    # MONTHLY DEMAND
    # --------------------------------------------------

    st.subheader("Monthly Appointment Demand")


    filtered_data['Month'] = (
        filtered_data['appointment_date_continuous'].dt.month
    )

    filtered_data['Year'] = (
        filtered_data['appointment_date_continuous'].dt.year
    )


    monthly = (
        filtered_data
        .groupby(['Year', 'Month'])['appointment_count']
        .sum()
        .reset_index()
    )


    monthly['Month_Name'] = pd.to_datetime(
        monthly['Month'],
        format='%m'
    ).dt.strftime('%b')


    fig_monthly = px.bar(
        monthly,
        x='Month_Name',
        y='appointment_count',
        color='Year',
        barmode='group',
        labels={
            'Month_Name': 'Month',
            'appointment_count': 'Appointments',
            'Year': 'Year'
        }
    )


    st.plotly_chart(
        fig_monthly,
        use_container_width=True
    )


    # --------------------------------------------------
    # DAY OF WEEK ANALYSIS
    # --------------------------------------------------

    st.subheader("Appointment Demand by Day of Week")


    filtered_data['Day_of_Week'] = (
        filtered_data['appointment_date_continuous']
        .dt.day_name()
    )


    weekday_order = [
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday',
        'Sunday'
    ]


    weekday_demand = (
        filtered_data
        .groupby('Day_of_Week')['appointment_count']
        .mean()
        .reindex(weekday_order)
        .reset_index()
    )


    fig_weekday = px.bar(
        weekday_demand,
        x='Day_of_Week',
        y='appointment_count',
        labels={
            'Day_of_Week': 'Day',
            'appointment_count': 'Average Appointments'
        }
    )


    st.plotly_chart(
        fig_weekday,
        use_container_width=True
    )


    # --------------------------------------------------
    # DATA TABLE
    # --------------------------------------------------

    st.subheader("Filtered Demand Data")

    st.dataframe(
        filtered_data[
            [
                'appointment_date_continuous',
                'appointment_count'
            ]
        ],
        use_container_width=True
    )

else:

    st.info("Please select both a start date and an end date.")  