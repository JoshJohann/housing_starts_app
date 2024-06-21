import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# Load the dataset
file_path = os.path.join(os.path.dirname(__file__), 'HOUST.csv')
df = pd.read_csv(file_path)

# Convert date column to datetime format
df['DATE'] = pd.to_datetime(df['DATE'])

# Streamlit app
st.title('Housing Starts Analysis')

# Display the dataset
st.write('Here is the dataset:')
st.write(df.head())

# Add a date range filter
st.write('Select a date range:')
min_date = df['DATE'].min()
max_date = df['DATE'].max()
start_date, end_date = st.date_input('Date range', [min_date, max_date])

# Filter the dataset based on the selected date range
filtered_df = df[(df['DATE'] >= pd.to_datetime(start_date)) & (df['DATE'] <= pd.to_datetime(end_date))]

# Calculate the moving average
filtered_df['Moving_Avg'] = filtered_df['HOUST'].rolling(window=12).mean()

# Plot the time series and moving average of housing starts
st.write('Housing Starts Over Time:')
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(filtered_df['DATE'], filtered_df['HOUST'], label='Housing Starts')
ax.plot(filtered_df['DATE'], filtered_df['Moving_Avg'], label='Moving Average (12 months)', color='orange')
ax.set_title('Housing Starts Over Time')
ax.set_xlabel('Date')
ax.set_ylabel('Housing Starts')
ax.legend()
st.pyplot(fig)
