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
def Regions(data):
   
   county = str(county).upper().strip() # Standardizes data to keep values consistent
   if county in regions:
       return regions[county]
   
   return "unknown"

complete_data["region"] = complete_data["county"].apply()

### Question 1: What type of alcohol is the most popular in each region of Iowa and what volume/cost was purchased? ###

# Puts all rows of the same region and alc type into a group wuhile sum adds the dollars and liters in each group
totals = df.groupby(["region", "category_name"])[["sales_dollars","sales_liters"]].sum()
totals = totals.reset_index()

def sort_type(data):

    totals = data.groupby(["region", "category_name"])["sales_dollars", "sales_liters", "sale_bottles"].sum().reset_index()
  
    return totals

def top_volume(total):
    results = []
    for region in totals["region"].unique():
        print()
        return