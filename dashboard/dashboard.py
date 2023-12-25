import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
import streamlit as st
from babel.numbers import format_currency

# Setting seaborn style
sns.set(style='dark')

# Load the datasets
day_df = pd.read_csv('../data/day.csv')
hour_df = pd.read_csv('../data/hour.csv')

# Merge the datasets
bike_sharing = day_df.merge(hour_df, on='dteday', how='inner', suffixes=('_daily', '_hourly'))

# Set page title
st.title('Bike Sharing Data Analysis Dashboard')

# Sidebar for user inputs
st.sidebar.header('Explore the Questions')

# User input for question selection
question_selection = st.sidebar.selectbox('Select Question', ['Q1', 'Q2', 'Q3', 'Q4'])

# Data Preparation
bike_sharing['dteday'] = pd.to_datetime(bike_sharing['dteday'])
bike_sharing['day'] = bike_sharing['dteday'].dt.day_name()
bike_sharing['hour'] = bike_sharing['hr']
weather_labels = {1: 'Clear', 2: 'Mist', 3: 'Light Rain', 4: 'Heavy Rain'}
bike_sharing['weather_situation'] = bike_sharing['weathersit_daily'].map(weather_labels)
bike_sharing['day_type'] = bike_sharing['day'].apply(lambda x: 'Weekend' if x in ['Saturday', 'Sunday'] else 'Weekday')

# Dashboard for Question 1
if question_selection == 'Q1':
    st.header('Question 1: When is bike sharing consistently higher? On which day? At what hour?')
    
    # Group by day and hour, calculate mean demand
    demand_by_day_hour = bike_sharing.groupby(['day', 'hour'])['cnt_daily'].mean().unstack()
    
    # Define the order of days (Monday to Sunday)
    day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    # Plot the heatmap
    plt.figure(figsize=(12, 6))
    sns.heatmap(demand_by_day_hour, cmap='turbo', cbar_kws={'label': 'Average Bike Sharing Demand'})
    plt.xlabel('Hour of the Day')
    plt.ylabel('Day of the Week')
    st.pyplot()

# Dashboard for Question 2
elif question_selection == 'Q2':
    st.header('Question 2: Is there a difference in bike sharing demand according to weather?')
    
    # Group by weather situation and calculate mean demand
    demand_by_weather = bike_sharing.groupby('weather_situation')['cnt_daily'].mean()

    # Plot the bar chart
    plt.figure(figsize=(8, 6))
    demand_by_weather.plot(kind='bar', color='skyblue')
    plt.xlabel('Weather Condition')
    plt.ylabel('Average Bike Sharing Demand')
    st.pyplot()

# Dashboard for Question 3
elif question_selection == 'Q3':
    st.header('Question 3: How does bike sharing demand change each month? In which month does demand reach the highest level?')
    
    # Group by month and calculate mean demand
    demand_by_month = bike_sharing.groupby('mnth_daily')['cnt_daily'].mean()

    # Plot the bar chart
    plt.figure(figsize=(10, 6))
    demand_by_month.plot(kind='bar', color='lightcoral')
    plt.xlabel('Month')
    plt.ylabel('Average Bike Sharing Demand')
    st.pyplot()

# Dashboard for Question 4
elif question_selection == 'Q4':
    st.header('Question 4: Is there a difference in bike sharing usage between weekdays and weekends?')
    
    # Group by day type and calculate mean demand
    demand_by_day_type = bike_sharing.groupby('day_type')['cnt_daily'].mean()

    # Plot the bar chart
    plt.figure(figsize=(6, 4))
    demand_by_day_type.plot(kind='bar', color='lightgreen')
    plt.xlabel('Day Type')
    plt.ylabel('Average Bike Sharing Demand')
    st.pyplot()

# Additional sections can be added for more questions

# Data Exploration Section
st.sidebar.header('Data Exploration')

# Show the first few rows of the data
if st.sidebar.checkbox('Show Raw Data'):
    st.subheader('Raw Data')
    st.write(bike_sharing.head())

# Show the summary statistics
if st.sidebar.checkbox('Show Summary Statistics'):
    st.subheader('Summary Statistics')
    st.write(bike_sharing.describe())

# Show Data Types
if st.sidebar.checkbox('Show Data Types'):
    st.subheader('Data Types')
    st.write(bike_sharing.dtypes)

# Show Missing Values
if st.sidebar.checkbox('Show Missing Values'):
    st.subheader('Missing Values')
    st.write(bike_sharing.isnull().sum())

# Show Duplicates
if st.sidebar.checkbox('Show Duplicates'):
    st.subheader('Duplicate Rows')
    st.write(bike_sharing.duplicated().sum())
