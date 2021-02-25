import os
import csv


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
for x in data:
    try:
        os.system(f"python email_crawler.py {x}")
    except RecursionError:      # will routinely encounter RecursionError max depths
        pass
    count += 1
    print(f"{count} domains have been crawled.")

# to run, enter "python3 batch_crawl.py" in cwd terminal
