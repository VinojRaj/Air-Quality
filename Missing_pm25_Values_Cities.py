# -*- coding: utf-8 -*-
"""
@author: Vinoj
"""
import pandas as pd
import os

def check_missing_values(city):
    # Construct the file path for the CSV file
    file_path = os.path.join(r'C:\Users\Vinoj\OneDrive\Desktop\Ashoka_PEDP\Assignments\Assignment 7.3\Data', f'{city}.csv')

    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(file_path, parse_dates=['datetime'], dayfirst=True)

    # Count missing (null) values in pm25 column
    missing_values_count = df['pm25'].isnull().sum()

    # Print or use the missing values count as needed
    print(f"City: {city}")
    print("Total Number of Missing Values for pm25 column:", missing_values_count)
    print("\n")

# List of cities
cities = ['Mumbai', 'Bengaluru', 'Chennai', 'Delhi', 'Kolkata']

# Check missing values for each city
for city in cities:
    check_missing_values(city)
