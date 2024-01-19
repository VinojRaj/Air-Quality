# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 18:55:53 2024

@author: Vinoj
"""
import pandas as pd
import os

def get_missing_values(city):
    # Construct the file path for the CSV file
    file_path = os.path.join(r'C:\Users\Vinoj\OneDrive\Desktop\Ashoka_PEDP\Assignments\Assignment 7.3\Data', f'{city}.csv')

    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(file_path, parse_dates=['datetime'], dayfirst=True)

    # Filter rows with missing (null) values in pm25 column
    missing_values_df = df[df['pm25'].isnull()]

    return missing_values_df[['datetime', 'pm25']]

def print_and_export_to_excel(cities_data):
    with pd.ExcelWriter(r'C:\Users\Vinoj\OneDrive\Desktop\Ashoka_PEDP\Assignments\Assignment 7.3\missing_values_per_city.xlsx', engine='xlsxwriter') as writer:
        for city, missing_values_df in cities_data.items():
            print(f"City: {city}")
            print("Dates with Missing Values for pm25 column:")
            print(missing_values_df[['datetime', 'pm25']])
            print("\n")

            # Export to Excel
            missing_values_df.to_excel(writer, sheet_name=city, index=False)

# List of cities
cities = ['Mumbai', 'Bengaluru', 'Chennai', 'Delhi', 'Kolkata']

# Dictionary to store dataframes for each city
cities_data = {}

# Get missing values for each city
for city in cities:
    cities_data[city] = get_missing_values(city)

# Print and export data to Excel
print_and_export_to_excel(cities_data)
