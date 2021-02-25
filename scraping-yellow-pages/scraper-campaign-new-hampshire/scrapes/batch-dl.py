
import os
import time



# THIRD ITERATION OF YELLOW PAGES WEB SCRAPER
kw_list = ['hardware+stores','landscaping','marinas']

# NEW HAMPSHIRE
towns = ['Manchester,NH',
         'Nashua,NH',
         'Concord,NH',
         'Derry,NH',
         'Dover,NH',
         'Rochester,NH',
         'Salem,NH',
         'Merrimack,NH',
         'Londonderry,NH',
         'Hudson,NH',
         'Keene,NH',
         'Bedford,NH',
         'Portsmouth,NH',
         'Goffstown,NH',
         'Durham,NH',
         'Laconia,NH',
         'Milford,NH',
         'Hampton,NH',
         'Exeter,NH',
         'Windham,NH',
         'Hooksett,NH',
         'Pelham,NH',
         'New+London,NH',
         'Canaan,NH',
         'Waterville+Valley,NH',
         'Franconia,NH',
         'Lancaster,NH',
         'Errol,NH',
         'Pittsburg,NH',
         'Stratford,NH',
         'Warren,NH',
         'Madison,NH',
         'Franklin,NH',
         'Bradford,NH'
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








