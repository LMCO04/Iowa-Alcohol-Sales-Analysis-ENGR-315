import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Load csv

data = pd.read_csv("../Data/Processed Data/daily_totals_2021.csv")

# Get day of year from "ordered on" data

data["ordered_on"] = pd.to_datetime(data["ordered_on"])

# Converts date to the number for the day of the year (0-365)

data["day_of_the_year"] = data["ordered_on"].dt.dayofyear

# Making lists for the day of year and the amount of alcohol ordered (liters)

list_day = data["day_of_the_year"].tolist()

list_liters = data["sales_liters"].tolist()

fig, ax = plt.subplots(figsize=(8, 5))

ax.scatter(data["ordered_on"], data["sales_liters"])

ax.xaxis.set_major_locator(mdates.MonthLocator())

ax.xaxis.set_major_formatter(mdates.DateFormatter('%b'))

ax.set_xlabel('Month')

ax.set_ylabel('Sales Volume (Liters)')

ax.set_title('Iowa Alcohol Sales by Volume 2021')

plt.show()


