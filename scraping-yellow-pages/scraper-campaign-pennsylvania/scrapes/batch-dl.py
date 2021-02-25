
import pandas as pd
import os
import time
from csv import reader

# FIFTH ITERATION OF YELLOW PAGES WEB SCRAPER
kw_list = ['hardware+stores','landscaping','marinas']

# PENNSYLVANIA (EAST)
towns = ["Brackney,PA",
         "Friendsville,PA",
         "Susquehanna,PA",
         "Lawton,PA",
         "Le+Raysville,PA",
         "Jackson,,PA",
         "Starruca,PA",
         "Starlight,PA",
         "Thompson,PA",
         "Lenox,PA",
         "Lemon,PA",
         "Meshoppen,PA",
         "Laceyville,PA",
         "Laceyville,PA",
         "Factoryville,PA",
         "Lake+Winola,PA",
         "Warren+Center,PA",
         "Scott,PA",
         "Forest+City,PA",
         "Lenoxville,PA",
         "Nicholson,PA",
         "Tunkhannock,PA",
         "Falls,PA",
         "Carbondale,PA",
         "Cochecton,PA",
         "Lackawaxen,PA",
         "Greeley,PA",
         "Lake+Ariel,PA",
         "Scranton,PA",
         "Moosic,PA",
         "Pittston,PA",
         "Meshoppen,PA",
         "Gouldsboro,PA",
         "Tobyhanna,PA",
         "Arrowhead+Lake,PA",
         "Philadelphia,PA",
         "King+of+Prussia,PA",
         "Levittown,PA",
         "Doylestown,PA",
         "Ottsville,PA",
         "Pennsburg,PA",
         "Soulderton,PA",
         "Fleetwood,PA",
         "New+Tripoli,PA",
         "Lansford,PA",
         "Walnutport,PA",
         "Lehighton,PA",
         "Kunkletown,PA",
         "Tamaqua,PA",
         "Albrightsville,PA",
         "Tannersville,PA",
         "Swiftwater,PA",
         "Blakeslee,PA",
         "Lake+Harmony,PA",
         "White+Haven,PA",
         "Birchwood+Lakes,PA",
         "Pecks+Pond,PA"
         "Skytop,PA",
         "Conashaugh+Lakes,PA",
         "Lackawaxen,PA"
         ]


combined = [(kw, town) for kw in kw_list for town in towns]
# print(combined)

for x in combined:
    keyword = x[0]
    place = x[1]
    os.system(f"python3 scraping_.py {keyword} {place}")
    time.sleep(3) # wait 3 second(s) before looping again, to avoid too many requests/second

# in working directory type the following to run wrapper script:
#               python3 batch-dl.py








