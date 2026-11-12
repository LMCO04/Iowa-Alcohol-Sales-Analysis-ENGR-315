import numpy as np
import pandas as pd

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