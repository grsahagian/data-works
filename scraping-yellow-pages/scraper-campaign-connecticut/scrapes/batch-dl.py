
import pandas as pd
import os
import time
from csv import reader

# FOURTH ITERATION OF YELLOW PAGES WEB SCRAPER
kw_list = ['hardware+stores','landscaping','marinas']

# NEW YORK (UPSTATE)
towns = ["Stamford,CT",
         "Norwalk,CT",
         "Danbury,CT",
         "New+Haven,CT",
         "Salisbury,CT",
         "Barhamsted,CT",
         "Madison,CT",
         "Killingworth,CT",
         "Norwich,CT",
         "Griswold,CT",
         "Mansfield,CT",
         "New+Milford,CT"
         "Winsted,CT",
         "Old+Saybrook,CT",
         "Enfield,CT"
         ]


combined = [(kw, town) for kw in kw_list for town in towns]
# print(combined)

for x in combined:
    keyword = x[0]
    place = x[1]
    os.system(f"python3 scraping_.py {keyword} {place}")
    time.sleep(3) # wait 2 second(s) before looping again, to avoid too many requests/second

# in working directory type the following to run wrapper script:
#               python3 batch-dl.py








