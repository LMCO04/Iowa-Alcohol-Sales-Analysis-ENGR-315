
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Sort counties into regions
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

# Load the processed county sales data
data = pd.read_csv("../Data/Processed Data/county_totals_2021.csv")


# Find which region each county belongs to
def get_region(county):
    for region in regions:
        for name in regions[region]:
            if str(county).strip().upper() == name.upper():
                return region
    return "Unknown"


# Add the region to each county
data["region"] = data["county_name"].apply(get_region)

# Remove records without a known county region
data = data[data["region"] != "Unknown"]

# Sort counties by sales dollars
county_sales = data.sort_values("sales_dollars", ascending=False)

# Find the county with the highest sales
top_county = county_sales.iloc[0]

print("Question 2: Iowa Liquor Sales")
print("County with the highest sales:", top_county["county_name"])
print("Total sales: $", round(top_county["sales_dollars"], 2))
print()

# Calculate total sales for each region
region_totals = data.groupby("region")["sales_dollars"].sum()

print("Total sales by region:")
print(region_totals.round(2))
print()

# Calculate average sales per county in each region
region_average = data.groupby("region")["sales_dollars"].mean()

print("Average sales per county by region:")
print(region_average.round(2))

# Graph the average county sales for each region
plt.bar(region_average.index, region_average.values)
plt.title("Average County Liquor Sales by Region in Iowa (2021)")
plt.xlabel("Region")
plt.ylabel("Average Sales per County ($)")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig("question2_region_sales.png")
plt.show()
