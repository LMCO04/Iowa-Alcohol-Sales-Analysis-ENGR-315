# Import libraries
import numpy as np
import pandas as pd

# Load in CSV files
separated = ['../sales_data/iowa_liquor_sales_2021_1.csv', '../sales_data/iowa_liquor_sales_2021_2.csv', 
             '../sales_data/iowa_liquor_sales_2021_3.csv', '../sales_data/iowa_liquor_sales_2021_4.csv', 
             '../sales_data/iowa_liquor_sales_2021_5.csv']

complete_data = pd.concat((pd.read_csv(f) for f in separated), ignore_index = True)

#Test CSV load
# print('test')
# print(complete_data.head())

# Sort data into region
regions = {
    "Northwest": ["Lyon", "Osceola", "Dickinson", "Emmet", "Sioux", "O'Brien", "Clay",
                  "Palo Alto", "Plymouth", "Cherokee", "Buena Vista", "Pocahontas",
                  "Humboldt", "Woodbury", "Ida", "Sac", "Calhoun", "Webster",
                  "Monona", "Crawford", "Carroll"],

    "Northeast": ["Winnebago", "Worth", "Mitchell", "Howard", "Winneshiek", "Allamakee",
                  "Hancock", "Cerro Gordo", "Floyd", "Chickasaw", "Kossuth", "Wright",
                  "Franklin", "Butler", "Bremer", "Fayette", "Clayton", "Black Hawk",
                  "Buchanan", "Delaware", "Dubuque", "Grundy", "Benton", "Linn",
                  "Jones", "Jackson", "Clinton"],

    "Central":   ["Greene", "Boone", "Story", "Hamilton", "Hardin", "Marshall", "Tama",
                  "Poweshiek", "Dallas", "Polk", "Jasper", "Guthrie", "Madison",
                  "Warren", "Marion", "Mahaska"],

    "Southwest": ["Harrison", "Shelby", "Audubon", "Pottawattamie", "Cass", "Adair",
                  "Mills", "Montgomery", "Adams", "Fremont", "Page", "Taylor",
                  "Ringgold", "Union", "Clarke", "Decatur"],

    "Southeast": ["Lucas", "Wayne", "Appanoose", "Monroe", "Wapello", "Davis",
                  "Van Buren", "Jefferson", "Keokuk", "Washington", "Henry",
                  "Des Moines", "Lee", "Louisa", "Muscatine", "Scott", "Johnson",
                  "Iowa", "Cedar"],
}

# sorts data and checks if couties exist in a region
county_to_region= {}
for region, counties in regions.items():
    for c in counties:
        county_to_region[c.upper()] = region

def get_region(county):
   
   county = str(county).upper().strip() # Standardizes data to keep values consistent
   
   if county in county_to_region:
       return county_to_region[county]
   
   return "unknown"

complete_data["region"] = complete_data["county_name"].apply(get_region)

print(complete_data[complete_data["region"] == "Unknown"]["county_name"].unique())


### Question 1: What type of alcohol is the most popular in each region of Iowa and what volume/cost was purchased? ###


# Puts all rows of the same region and alc type into a group wuhile sum adds the dollars and liters in each group

def sort_type(data):

    # totals = data.groupby(["region", "category_name"])["sales_dollars", "sales_liters", "sales_bottles"].sum().reset_index()
    totals = complete_data.groupby(["region", "category_name"])[["sales_dollars","sales_liters"]].sum()
    totals = totals.reset_index()

    return totals

def find_top(totals, column):
    results = []
    for region in totals["region"].unique():
        rows = totals[totals["region"] == region]
        rows = rows.sort_values(column, ascending = False)
        top = rows.iloc[0]
        print(region, "|", top["category_name"], "|", round(top["sales_dollars"], 2), "dollars |", round(top["sales_liters"], 2), "liters")
        
        return

totals = sort_type(complete_data)

print("Most populat by money")
find_top(totals, "sales_dollars")

print()

print("Most popular by volume")
find_top(totals, "sales_liters")