
import pandas as pd
import os
import time
from csv import reader

# SIXTH? ITERATION OF YELLOW PAGES WEB SCRAPER
kw_list = ['hardware+stores','landscaping','marinas']

# NEW JERSEY
towns = ["Wantage,NJ",
         "Hackettstown,NJ",
         "Parsippany+Troy,NJ",
         "Maurice+River,NJ",
         "Vineland,NJ",
         "Bridgeton,NJ",
         "Deptford,NJ",
         "Fairfield,NJ",
         "Millvile,NJ",
         "Buena,NJ",
         "Franklin,NJ",
         "Elmer,NJ",
         "Pilesgrove,NJ",
         "Galloway,NJ",
         "Stow+Creek,NJ",
         "Sweetwater,NJ",
         "Tabernacle,NJ",
         "Evesham,NJ",
         "Bass+River,NJ",
         "Pemberton,NJ",
         "Burlington,NJ",
         "Lacey+Township,NJ",
         "North+Hanover,NJ",
         "Fort+Dix,NJ",
         "Plumstead,NJ",
         "Tuckerton,NJ",
         "Port+Republic,NJ",
         "Hamilton,NJ",
         "Toms+River,NJ",
         "Brick+Township,NJ",
         "Lakewood,NJ",
         "Point+Pleasant+Beach,NJ",
         "Howell+Township,NJ",
         "Cherry+Hill,NJ",
         "East+Windsor,NJ",
         "Lawrence+Township,NJ",
         "Neptune+City,NJ",
         "Millstone,NJ",
         "Pemberton,NJ",
         "Lawrence+Township,NJ",
         "Tinton+Falls,NJ",
         "Holmdel,NJ",
         "Hazlet,NJ",
         "Old+Bridge,NJ",
         "Princeton,NJ",
         "Washington,NJ",
         "Newark,NJ",
         "Paterson,NJ",
         "Ramsey,NJ",
         "West+Milford,NJ",
         "Watchung,NJ",
         "Jefferson,NJ"
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








