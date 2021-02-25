import sqlite3 as sql
import pandas as pd

def add_to_db(frame):
    conn = sql.connect('leads_.db')
    frame.to_sql('leads', conn, if_exists='append')

# Maine Search 1
# path_maine = "./scraper-campaign-maine/Maine_search_edit.xlsx"
# me = pd.read_excel(path_maine, engine="openpyxl")
# me.reset_index(inplace=True)
# me['Campaign'] = 'ME1'
# del me['index']
# del me['Index']
#
# # Vermont Search 1
# path_vt = "./scraper-campaign-vermont/Vermont_search_edited.xlsx"
# vt = pd.read_excel(path_vt, engine="openpyxl")
# vt.reset_index(inplace=True)
# vt['Campaign'] = 'VT1'
# del vt['index']
# del vt['Index']
#
# # Maine Search 2
# path_me2 = "./scraper-campaign-me-2/Maine_search_2_edit.xlsx"
# me2 = pd.read_excel(path_me2, engine="openpyxl")
# me2.reset_index(inplace=True)
# # me2['Campaign'] = 'ME2'
# del me2['index']
# del me2['Index']


# New Hampshire Search 1
# path_nh1 = "./scraper-campaign-new-hampshire/New_Hampshire_search.xlsx"
# nh1 = pd.read_excel(path_nh1, engine="openpyxl")
# nh1.reset_index(inplace=True)
# del nh1['Index']
# del nh1['index']

# New York Search 1
# path_ny1 = "scraper-campaign-new-york/New_York_search_edit.xlsx"
# ny1 = pd.read_excel(path_ny1, engine="openpyxl")
# ny1.reset_index(inplace=True)
# ny1 = ny1[ny1['Email'].notnull()]
# del ny1['Index']
# del ny1['index']
# print(ny1)
# add_to_db(ny1)


# Connecticut Search 1
# path = "scraper-campaign-connecticut/Connecticut_search_edit.xlsx"
# ct1 = pd.read_excel(path, engine="openpyxl")
# ct1.reset_index(inplace=True)
# ct1 = ct1[ct1['email'].notnull()]
# ct1 = ct1[ct1['Response?'] != 'NA']
# del ct1['Column1']
# del ct1['index']

# Pennsylvania Search 1
# path = "scraper-campaign-pennsylvania/Pennsylvania_search_edit.xlsx"
# pa1 = pd.read_excel(path, engine="openpyxl")
# pa1.reset_index(inplace=True)
# pa1 = pa1[pa1['email'].notnull()]
# pa1 = pa1[pa1['Response?'] != 'NA']
# pa1 = pa1[pa1['email'] != 'NA']
# del pa1['Column1']
# del pa1['index']
#
# # print(pa1.columns)
# add_to_db(pa1)

# New Jersey Search 1
# path = "scraper-campaign-new-jersey/New_Jersey_search_edit.xlsx"
# df = pd.read_excel(path, engine="openpyxl")
# df.reset_index(inplace=True)
# df = df[df['email'].notnull()]
# df = df[df['Response?'] != 'NA']
# df = df[df['email'] != 'NA']
# del df['Column1']
# del df['index']
#
# # print(df.columns)
# add_to_db(df)







# conn = sql.connect('leads_.db')

# me.to_sql('leads', conn)
# vt.to_sql('leads', conn, if_exists='append')






# query = 'SELECT * business_name ' \
#         'FROM leads ' \
#         'WHERE locality = Greene'
# table = pd.read_sql(query, conn)
# print(table)






