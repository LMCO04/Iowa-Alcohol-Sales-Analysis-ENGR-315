"""
Prepare smaller CSV files for the Iowa alcohol sales project.
The original files are too large to analyze all at once.
This program reads them in smaller sections and adds up the sales.
"""

import pandas as pd
from pathlib import Path

# These paths match the folders in our VS Code project.
folder = Path(__file__).resolve().parent
raw_folder = folder / 'Data' / 'Raw Data'
processed_folder = folder / 'Data' / 'Processed Data'
processed_folder.mkdir(exist_ok=True)

# Only load the columns needed for our three questions.
columns = ['ordered_on', 'county_name', 'category_name',
           'sales_dollars', 'sales_liters', 'sales_bottles']

# Store smaller summaries here instead of storing every original row.
parts = []

# Use files 1-4. File 5 repeats data already included in file 4.
for number in range(1, 5):
    filename = raw_folder / f'iowa_liquor_sales_2021_1258_rows_part_{number:04d}.csv'
    print('Reading:', filename.name)

    # Read 100,000 rows at a time so the program uses less memory.
    for data in pd.read_csv(filename, usecols=columns, chunksize=100000):
        data['ordered_on'] = pd.to_datetime(data['ordered_on'])
        data['county_name'] = data['county_name'].fillna('UNKNOWN')
        data['category_name'] = data['category_name'].fillna('UNKNOWN')
        data['record_count'] = 1

        # Add up sales from the same day, county, and category.
        summary = data.groupby(
            ['ordered_on', 'county_name', 'category_name'],
            as_index=False
        )[['sales_dollars', 'sales_liters', 'sales_bottles', 'record_count']].sum()
        parts.append(summary)

# Combine the smaller summaries and add up matching groups again.
all_data = pd.concat(parts, ignore_index=True)
daily = all_data.groupby(
    ['ordered_on', 'county_name', 'category_name'],
    as_index=False
)[['sales_dollars', 'sales_liters', 'sales_bottles', 'record_count']].sum()

# Save the tables that the three analysis programs will use.
daily.to_csv(processed_folder / 'daily_county_category_2021.csv', index=False)

county_category = daily.groupby(
    ['county_name', 'category_name'], as_index=False
)[['sales_dollars', 'sales_liters', 'sales_bottles', 'record_count']].sum()
county_category.to_csv(processed_folder / 'county_category_2021.csv', index=False)

county_totals = daily.groupby('county_name', as_index=False)[
    ['sales_dollars', 'sales_liters', 'sales_bottles', 'record_count']
].sum()
county_totals.to_csv(processed_folder / 'county_totals_2021.csv', index=False)

daily_category = daily.groupby(
    ['ordered_on', 'category_name'], as_index=False
)[['sales_dollars', 'sales_liters', 'sales_bottles', 'record_count']].sum()
daily_category.to_csv(processed_folder / 'daily_category_2021.csv', index=False)

daily_totals = daily.groupby('ordered_on', as_index=False)[
    ['sales_dollars', 'sales_liters', 'sales_bottles', 'record_count']
].sum()
daily_totals.to_csv(processed_folder / 'daily_totals_2021.csv', index=False)

print('Finished! The five smaller CSV files are in Data/Processed Data.')
