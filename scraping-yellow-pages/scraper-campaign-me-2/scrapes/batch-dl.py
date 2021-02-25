
import os
import time



# THIRD ITERATION OF YELLOW PAGES WEB SCRAPER
# second run on Maine, to fill gaps in scraper coverage
kw_list = ['hardware+stores','landscaping','marinas']

# VERMONT
towns = ['Loon+Lake,ME',
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
# creates list for all combinations of (kw, town)
combined = [(kw, town) for kw in kw_list for town in towns]

# print(combined)

for x in combined:
    keyword = x[0]
    place = x[1]
    os.system(f"python3 scraping_.py {keyword} {place}")
    time.sleep(2) # wait 2 second(s) before looping again, to avoid too many requests/second

# in working directory type the following to run wrapper script:
#               python3 batch-dl.py








