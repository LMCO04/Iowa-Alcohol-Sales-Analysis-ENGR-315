# Iowa-Alcohol-Sales-Analysis-ENGR-315
## Created by: Lucas Colonna, Abby Molloy, and Kevin Kabasele

## Motivation For This Analysis
The following is an analysis of a dataset containing alcohol purchases in stores with Class E liquor licenses in the state of Iowa. The link to the website containing the research is conducted is:
[State of Iowa - Iowa Liquor Sales, 2021](https://catalog.data.gov/dataset/iowa-liquor-sales-2021?from_hint=eyJxIjoiTGlxdW9yIn0%3D)
 This data was collected through inventory tracking and in-store record-keeping that is reported to the government. The contents of this file are every alcohol purchase that was made sorted by the day it was made, then by county. This information can be used to determine how citizens of Iowa spend their weekends or time celebrating, what they prefer to drink, and how much it costs them to do so. Using this information, we can answer the following questions:

### 1. What type of alcohol is the most popular in each region of Iowa and what volume/cost was purchased?
### 2. What county spends the most money on alcohol and how does region within the state affect the number of sales?
### 3. To what degree do celebrations/holidays affect alcohol sales in Iowa?

## Implementation Details
Each purchase that was recorded on the csv file contains the date of purchase, location data, sales data, and product information.
For the first question the location data and product information will be summed up for each county in Iowa. Then, each country will be sorted and talleyed into urban, suburban, or rural.
For the second question. We will use the data from question 1 and find the county and region type to determine how much money was spent and what region type spends the most.
The third question will focus mostly on the date of the data. A trend line will be created based on increase in sales per day across the entire year. Times of the year will be sorted by their holiday season associated (i.e. Christmas season in December and graduation season in June).


## Results of the Analysis
We discovered that the region with the highest alcohol purchases was in the central region of Iowa. Their drink of choice through how the citizens spend their money is Vodka with $21712199.19 spent throughout the year with a volume of 1930560.83 liters.


## Conclusions from the Analysis
The result of question one was partially surprising. The central region of Iowa having the most sales revenue was predicted due to it being one of the few majorly Urban regions of the generally rural state. However, what is shocking is the choice of alcohol. We predicted that beer was going to be the most popular due to the cheap cost and high volume per dollar. 


## Actions Needed
All data processed in the programs are completed using a single csv data file. If mutliple are used like in this project, fucntions are used to splice the csv files together.
(Continue)

## References/Source files:
List all the references the group used for the project, including journal & conference papers, GitHub repositories, open-source files, etc.

Stack Overflow: Loop through sub folders in a directory and import specified columns from .CSV files:
https://stackoverflow.com/questions/48940448/loop-through-sub-folders-in-a-directory-and-import-specified-columns-from-csv-f

Stack Overflow: How to group columns and sum them, in a large CSV?
https://stackoverflow.com/questions/71034664/how-to-group-columns-and-sum-them-in-a-large-csv

## Progress Report
11/12 
Currently the team is individually working on each of the three questions. Each memebr is practicing mutliple different strategies on how to splice together the csv files as well as sort them into regions.
Currently question 1 is complete by removing the headers and joining the csv files togther in the program. Then they are manually assigning each county to a region to answer the question. The answer to question 1 is in the "Results of the Analysis" portion of the README and the conclusions section was also updated accrodingly.
