import os
import csv
import time
import pandas as pd


# csv file containing domains
file = 'domains.csv'

with open(file, encoding='utf-8-sig', newline='') as csvf:
    reader = csv.reader(csvf)
    data = list(reader)

#   converting list of lists to list of strings (flattening lists)
data = [x for i in data for x in i]
# print(data)

#   NOTE: AVOID LARGE COMPANY DOMAINS -> much more likely to encounter recursion depths

# runs 'email_crawler.py' on each domain listed in above csv file
count = 0
start = time.time()

for x in data:
    try:
        os.system(f"python email_crawler.py {x}")
    except RecursionError:      # will routinely encounter RecursionError max depths
        pass
    count += 1
    print(f"{count} out of {len(data)} domains have been crawled.")

final = time.time() - start
print("It took about {x} minutes to crawl {y} domains".format(x = int(final / 60), y = len(data)))
data = pd.read_csv("scraped_emails_domains.csv")
print("Scraped {z} potential email addresses".format(z = len(data)))
# to run:   "python batch_crawl.py"   in command line
