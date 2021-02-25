
import pandas as pd
import os
import time
from csv import reader

# SIXTH? ITERATION OF YELLOW PAGES WEB SCRAPER
kw_list = ['realtor','property+manager','real+estate']

# NEW JERSEY
towns = ['Westport,ME',
         'Bowdoinham,ME',
         'Wiscasset,ME',
         'Richmond,ME',
         'Jefferson,ME',
         'Winthrop,ME',
         'Bucksport,ME',
         'Glenburn,ME',
         'Newport,ME',
         'Enfield,ME',
         'Bowerbank,ME',
         'Biddeford,ME',
         'Saco,ME',
         'Westbrook,ME'
         'Augusta,ME',
         'Waterville,ME',
         'Brewer,ME',
         'Bath,ME',
         'Ellsworth,ME',
         'Caribou,ME',
         'Rockland,ME',
         'Belfast,ME',
         'Gardiner,ME',
         'Calais,ME',
         'Hallowell,ME',
         'Eastport,ME',
         'Portland,ME',
         'Lewiston,ME',
         'Auburn,ME',
         'Loon+Lake,ME',
         'Carrabasset+Valley,ME',
         'Roxbury,ME',
         'Bethel,ME',
         'Lovell,ME',
         'Rumford,ME',
         'Carthage,ME',
         'Andover,ME',
         'Sandy+River,ME',
         'Kingfield,ME',
         'Dennistown,ME',
         'The+Forks,ME',
         'Greenville,ME',
         'Kokadjo,ME',
         'Somerset+Junction,ME',
         'New+Vineyard,ME',
         'Denmark,ME',
         'Bingham,ME',
         'Jackman,ME',
         'Island+Falls,ME',
         'Danforth,ME',
         'Lakeville,ME',
         'Burlington,ME',
         'Machiasport,ME',
         'Jonesboro,ME',
         'Harrington,ME',
         'Patten,ME',
         'Hanover,ME',
         'Rangeley,ME',
         'Eustis,ME',
         'Great+Pond,ME'
         ]


combined = [(kw, town) for kw in kw_list for town in towns]
# print(combined)

for x in combined:
    keyword = x[0]
    place = x[1]
    os.system(f"python3 superscraper.py {keyword} {place}")
    time.sleep(3) # wait 2 second(s) before looping again, to avoid too many requests/second

# in working directory type the following to run wrapper script:
#               python3 batch-dl.py








