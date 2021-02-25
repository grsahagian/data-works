import pandas as pd
import glob


# takes all csv files in /path/ and combines them into one large excel file


# ALTER ACCORDING TO CURRENT PROJ DIRECTORY
path = 'scrapes'  # use your path
all_files = glob.glob(path + "/*.csv")

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)

frame = pd.concat(li, axis=0, ignore_index=True)

# groups businesses by town, drops useless yellow pages rank/rating columns
frame.groupby(['locality'])
# frame.drop(columns=['rank','rating','business_page','listing_url'], inplace=True)
frame.reset_index(drop=True, inplace=True)
# drops duplicate business entries
frame.drop_duplicates(subset=['business_name'], inplace=True)
frame.drop_duplicates(subset=['website'], inplace=True)


# printing full dataframe
# pd.set_option("display.max_rows", None, "display.max_columns", None)

# CUMULATIVE MASTER SPREADSHEET
master = pd.read_excel("/Users/Graham/data-works/scraping-yellow-pages/leads_master_export1.xlsx", engine="openpyxl")
master = master.drop_duplicates(subset='website', keep="first")

# current search
df = pd.DataFrame(frame)
df = df.drop_duplicates(subset='website', keep="first")
df["Campaign"] = 'MER'
# MER = Maine Realtor (ME - R)

# combine potentially overlapping df with new search,
new_df = pd.concat([master, df]).drop_duplicates(subset='business_name')

# remove duplicate entries
new_df = new_df.drop_duplicates(subset='website')

# only include results for new search
new_df = new_df[new_df.Campaign == 'MER']
del new_df['index']



# print(df)
new_df.to_excel("Maine_realtor_search.xlsx")