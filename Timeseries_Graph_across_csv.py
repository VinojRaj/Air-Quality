# -*- coding: utf-8 -*-
"""
@author: Vinoj
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Define the list of cities
cities = ['Bengaluru', 'Chennai', 'Delhi', 'Kolkata', 'Mumbai']

# Define custom colors for each city
custom_colors = {
    'Bengaluru': 'green',
    'Delhi': 'red',
    'Chennai': 'blue',
    'Kolkata': 'yellow',
    'Mumbai': 'Silver',
}

# Set the style for the plot
sns.set(style="whitegrid")
plt.figure(figsize=(12, 6), dpi=300)  # Set the dpi parameter for increased resolution

# Iterate through each city
for city in cities:
    # Construct the file path
    file_path = f'C:\\Users\\Vinoj\\OneDrive\\Desktop\\Ashoka_PEDP\\Assignments\\Assignment 7.3\\Data\\{city}.csv'

    # Check if the file exists
    if os.path.exists(file_path):
        # Load data from CSV file
        df = pd.read_csv(file_path)

        # Convert the 'datetime' column to datetime format with the correct format
        df['datetime'] = pd.to_datetime(df['datetime'], format='%d-%m-%Y')

        # Plot the time series data for each city with a different color, line style, and without markers
        sns.lineplot(x='datetime', y='pm25', data=df, label=city, color=custom_colors[city], marker=None, linestyle='-')

# Set labels and title
plt.xlabel('Time')
plt.ylabel('PM 2.5 Values')
plt.title('Time Series of PM 2.5 Values in Different Cities')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Show legend
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

# Display the plot
plt.tight_layout()
plt.show()
