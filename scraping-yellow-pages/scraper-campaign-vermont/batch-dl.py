
import os
import time



# SECOND ITERATION OF YELLOW PAGES WEB SCRAPER
kw_list = ['hardware+stores','landscaping','marinas']

# VERMONT
towns = ['Burlington,VT',
         'Essex,VT',
         'Colchester,VT',
         'South+Burlington,VT',
         'Colchester,VT',
         'Rutland+City,VT',
         'Bennington,VT',
         'Brattleboro,VT',
         'Milton,VT',
         'Essex+Junction,VT',
         'Williston,VT',
         'Hartford,VT',
         'Springfield,VT',
         'Middlebury,VT',
         'Barre+city,VT',
         'Barre,VT',
         'Shelburne,VT',
         'Montpelier,VT',
         'Winooski,VT',
         'St.Johnsbury,VT',
         'St.Albans+city,VT',
         'Swanton,VT',
         'St.Albans,VT',
         'Northfield,VT',
         'Lyndon,VT',
         'Morristown,VT',
         'Waterbury,VT',
         'Rockingham,VT',
         'Jericho,VT'
         ]

combined = [(kw, town) for kw in kw_list for town in towns]
# print(combined)

for x in combined:
    keyword = x[0]
    place = x[1]
    os.system(f"python3 scraping_.py {keyword} {place}")
    time.sleep(2) # wait 2 second(s) before looping again, to avoid too many requests/second

# in working directory type the following to run wrapper script:
#               python3 batch-dl.py








