from opencage.geocoder import OpenCageGeocode
import pandas as pd
import os

## input dataframe read from excel file, and name it something
# for example:      convert_excel_to_coords(me2, 'Maine_search_2_coords')
def convert_excel_to_coords(df, name: str):
    key = 'd3b08f274381477ca65b8e463b5c7cd6'
    geocoder = OpenCageGeocode(key)
    list_lat = []
    list_long = []
    for index, row in df.iterrows():  # iterate over rows in dataframe

        City = row['locality']
        State = row['region']
        query = str(City) + ',' + str(State)

        results = geocoder.geocode(query)
        lat = results[0]['geometry']['lat']
        long = results[0]['geometry']['lng']

        list_lat.append(lat)
        list_long.append(long)

    # create new columns from lists

    df['lat'] = list_lat

    df['lon'] = list_long

    mdf = pd.DataFrame()
    mdf['business'] = df['business_name']
    mdf['city'] = df['locality']
    mdf['state'] = df['region']
    mdf['lat'] = df['lat']
    mdf['long'] = df['lon']

    mdf.to_excel(f"{name}.xlsx")


# path to formatted Excel file
# reading file to memory
# me2 = pd.read_excel(me2_path, engine='openpyxl')



# me_path = './scraper-campaign-maine/Maine_search_edit.xlsx'
# me = pd.read_excel(me_path, engine='openpyxl')
# me = me.loc[me.Pipeline.str.contains('Emailed', na=False)]
# convert_excel_to_coords(me, 'maine1_emailed_coords')
#
# vt_path = './scraper-campaign-vermont/Vermont_search_edited.xlsx'
# vt = pd.read_excel(vt_path, engine='openpyxl')
# vt = vt.loc[vt.Pipeline.str.contains('Emailed', na=False)]
# convert_excel_to_coords(vt, 'vermont1_emailed_coords')
#
# me2_path = './scraper-campaign-me-2/Maine_search_2_edit.xlsx'
# me2 = pd.read_excel(me2_path, engine='openpyxl')
# me2 = me2.loc[me2.Pipeline.str.contains('Emailed', na=False)]
# convert_excel_to_coords(me2, 'me2_emailed_coords')

# nh1_path = './scraper-campaign-new-hampshire/New_Hampshire_search.xlsx'
# nh1 = pd.read_excel(nh1_path, engine='openpyxl')
# nh1 = nh1.loc[nh1.Pipeline.str.contains('Emailed', na=False)]
# convert_excel_to_coords(nh1, 'nh1_emailed_coords')


# cwd = os.getcwd()
# ny1_path = os.path.join(cwd, 'scraper-campaign-new-york/New_York_search_edit.xlsx')
# ny1 = pd.read_excel(ny1_path, engine='openpyxl')
# ny1 = ny1.loc[ny1.Pipeline.str.contains('Emailed', na=False)]
# convert_excel_to_coords(ny1, 'ny1_emailed_coords')

# cwd = os.getcwd()
# path = os.path.join(cwd, 'scraper-campaign-connecticut/Connecticut_search_edit.xlsx')
# ct1 = pd.read_excel(path, engine='openpyxl')
# ct1 = ct1.loc[ct1.Pipeline.str.contains('Emailed', na=False)]
# convert_excel_to_coords(ct1, 'ct1_emailed_coords')

# cwd = os.getcwd()
# path = os.path.join(cwd, 'scraper-campaign-pennsylvania/Pennsylvania_search_edit.xlsx')
# pa1 = pd.read_excel(path, engine='openpyxl')
# pa1 = pa1.loc[pa1.Pipeline.str.contains('Emailed', na=False)]
# convert_excel_to_coords(pa1, 'pa1_emailed_coords')

cwd = os.getcwd()
path = os.path.join(cwd, 'scraper-campaign-new-jersey/New_Jersey_search_edit.xlsx')
df = pd.read_excel(path, engine='openpyxl')
df = df.loc[df.Pipeline.str.contains('Emailed', na=False)]
convert_excel_to_coords(df, 'nj1_emailed_coords')