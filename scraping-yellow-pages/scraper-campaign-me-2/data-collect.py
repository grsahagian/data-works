import pandas as pd
import glob


# takes all csv files in /path/ and combines them into one large excel file



path = './scrapes' # use your path
all_files = glob.glob(path + "/*.csv")

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)

frame = pd.concat(li, axis=0, ignore_index=True)

# groups businesses by town, drops useless yellow pages rank/rating columns
frame.groupby(['locality'])
frame.drop(columns=['rank','rating'], inplace=True)
frame.reset_index(drop=True, inplace=True)
# drops duplicate business entries
frame.drop_duplicates(subset=['business_name'], inplace=True)


# labelling current search results as ME2
frame["Campaign"] = 'ME2'

# importing previous Maine search results and labelling as 'ME1'
me1 = pd.read_excel("/Users/Graham/data-works/scraping-yellow-pages/scraper-campaign-maine/Maine_search.xlsx", engine="openpyxl")
me1 = me1.drop_duplicates(subset='website', keep="first")
me1["Campaign"] = 'ME1'

# Joining the two frames together, dropping duplicates and keeping only values from current search
df = pd.concat([me1, frame]).drop_duplicates(subset='business_name')
df = df.drop_duplicates(subset='website')
df = df[df.Campaign != "ME1"]

del df['Index']


df.to_excel("Maine_search_2.xlsx")










