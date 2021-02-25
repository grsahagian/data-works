import pandas as pd
import glob


# takes all csv files in /path/ and combines them into one large excel file



path = r'/Users/Graham/data-works/scraping-yellow-pages/scrapes' # use your path
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

# unique = frame.locality.unique
# print(unique)


# printing full dataframe
# pd.set_option("display.max_rows", None, "display.max_columns", None)
print(frame.describe)
# frame.to_excel("Maine_search.xlsx")







