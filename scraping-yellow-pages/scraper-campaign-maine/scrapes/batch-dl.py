
import os
import time

kw_list = ['hardware+stores','yacht+club','marinas']


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
         'Porland,ME',
         'Lewiston,ME',
         'Auburn,ME',
         ]

combined = [(kw, town) for kw in kw_list for town in towns]
# print(combined)

for x in combined:
    keyword = x[0]
    place = x[1]
    os.system(f"python3 scraping_.py {keyword} {place}")
    time.sleep(1) # wait 1 second before looping again, to avoid too many requests/second










