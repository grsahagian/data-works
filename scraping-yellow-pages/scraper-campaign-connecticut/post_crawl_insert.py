import pandas as pd

# spreadsheet to insert values into
spreadsheet = "Connecticut_search.xlsx"
df = pd.read_excel(spreadsheet, engine="openpyxl")
df.rename(columns= {"Email": "email"},
          inplace=True)

# csv file that is read
email = pd.read_csv("scraped_emails_domains.csv", header=0)

output = (
    df
        .drop(columns=['email'])  #  this is empty and needs to be overwritten
        .merge(
            email.groupby('website', as_index=False).first(),  # just the first email
            on='website', how='left'  # left-join -> keep all rows from spreadsheet
        )
        .loc[:, df.columns] # get your original column order back
)

del output['Column1']

# output.to_excel("Connecticut_search_edit.xlsx")