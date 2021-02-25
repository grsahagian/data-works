
import pandas as pd
import os
import time
from csv import reader

# FOURTH ITERATION OF YELLOW PAGES WEB SCRAPER
kw_list = ['hardware+stores','landscaping','marinas']

# NEW YORK (UPSTATE)
towns = ["Schenectady,NY",
         "Hudson,NY",
         "Ticonderoga,NY",
         "Schuylerville,NY",
         "Forestport,NY",
         "Old+Forge,NY",
         "Cranberry+Lake,NY",
         "Tupper+Lake,NY",
         "Childwold,NY",
         "Wanakena,NY",
         "Harrisville,NY",
         "Dannemora,NY",
         "Malone,NY",
         "Parishville,NY",
         "Potsdam,NY",
         "Gouverneur,NY",
         "Alexandria+Bay,NY",
         "Sackets+Harbor,NY",
         "Raquette+Lake,NY",
         "Oswegatchie,NY",
         "Lake+Placid,NY",
         "Schroon+Lake,NY",
         "Camden,NY",
         "Syracuse,NY",
         "Cooperstown,NY",
         "Saranac+Lake,NY",
         "Bolton,NY",
         "Northville,NY",
         "Poughkeepsie,NY",
         "Deposit,NY",
         "Kingston,NY",
         "Watertown,NY",
         "Redfield,NY",
         "Remsen,NY",
         "Higgins+Bay,NY"]


combined = [(kw, town) for kw in kw_list for town in towns]
# print(combined)

for x in combined:
    keyword = x[0]
    place = x[1]
    os.system(f"python3 scraping_.py {keyword} {place}")
    time.sleep(3) # wait 2 second(s) before looping again, to avoid too many requests/second

# in working directory type the following to run wrapper script:
#               python3 batch-dl.py








