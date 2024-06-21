import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = '/Users/josh/Downloads/HOUST.csv'
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

# Add a dropdown to select the column to plot
column_to_plot = st.selectbox('Select column to plot:', df.columns)

# Calculate the moving average
filtered_df['Moving_Avg'] = filtered_df['HOUST'].rolling(window=12).mean()

# Plot the selected column
st.write(f'{column_to_plot} Over Time:')
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(filtered_df['DATE'], filtered_df[column_to_plot], label=column_to_plot)
if column_to_plot == 'HOUST':
    ax.plot(filtered_df['DATE'], filtered_df['Moving_Avg'], label='Moving Average (12 months)', color='orange')
ax.set_title(f'{column_to_plot} Over Time')
ax.set_xlabel('Date')
ax.set_ylabel(column_to_plot)
ax.legend()
st.pyplot(fig)
