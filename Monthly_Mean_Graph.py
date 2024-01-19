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

# Create a new DataFrame to store all mean values
all_means = pd.DataFrame(columns=['datetime'])

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

        # Extract month and year from the 'datetime' column
        df['month'] = df['datetime'].dt.month
        df['year'] = df['datetime'].dt.year

        # Group by year and month, calculate the mean for each group
        monthly_means = df.groupby(['year', 'month'])['pm25'].mean().reset_index()

        # Create a new 'datetime' column using year and month
        monthly_means['datetime'] = pd.to_datetime(monthly_means[['year', 'month']].assign(day=1))
        
        # Add mean values to the all_means DataFrame with the city name as the column name
        all_means = pd.merge(all_means, monthly_means[['datetime', 'pm25']], how='outer', left_on='datetime', right_on='datetime', suffixes=('', f'_{city}'))

        # Plot the mean time series data for each city with a different color, line style, and without markers
        sns.lineplot(x='datetime', y='pm25', data=monthly_means, label=city, color=custom_colors[city], marker=None, linestyle='-')

# Export all mean values to a single Excel file
excel_file_path = 'C:\\Users\\Vinoj\\OneDrive\\Desktop\\Ashoka_PEDP\\Assignments\\Assignment 7.3\\all_cities_mean_pm25.xlsx'
all_means.to_excel(excel_file_path, index=False)

print(f"All mean values exported to {excel_file_path}")

# Set labels and title
plt.xlabel('Time')
plt.ylabel('Mean PM 2.5 Values')
plt.title('Mean Time Series of PM 2.5 Values in Different Cities')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Show legend
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

# Display the plot
plt.tight_layout()
plt.show()
