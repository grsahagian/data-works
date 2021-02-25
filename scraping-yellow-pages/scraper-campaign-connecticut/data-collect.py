import pandas as pd
import glob

# takes all csv files in /path/ and combines them into one large excel file

# ALTER ACCORDING TO CURRENT PROJ DIRECTORY
path = './scrapes'  # use your path
all_files = glob.glob(path + "/*.csv")

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)

frame = pd.concat(li, axis=0, ignore_index=True)

# groups businesses by town, drops useless yellow pages rank/rating columns
frame.groupby(['locality'])
frame.drop(columns=['rank', 'rating', 'business_page', 'listing_url'], inplace=True)
frame.reset_index(drop=True, inplace=True)
# drops duplicate business entries
frame.drop_duplicates(subset=['business_name'], inplace=True)
frame.drop_duplicates(subset=['website'], inplace=True)

# printing full dataframe
# pd.set_option("display.max_rows", None, "display.max_columns", None)

# CUMULATIVE MASTER SPREADSHEET
master = pd.read_excel("/Users/Graham/data-works/scraping-yellow-pages/leads_master_export1.xlsx", engine="openpyxl")
master = master.drop_duplicates(subset='website', keep="first")

# current search (new york search 1)
ct1 = pd.DataFrame(frame)
ct1 = ct1.drop_duplicates(subset='website', keep="first")
ct1["Campaign"] = 'CT1'

# combine potentially overlapping df with new search,
df = pd.concat([master, ct1]).drop_duplicates(subset='business_name')

# remove duplicate entries
df = df.drop_duplicates(subset='website')

# only include results for new search
df = df[df.Campaign == 'CT1']
del df['index']

# df.to_excel("Connecticut_search.xlsx")
