import pandas as pd

# yellow pages scraper spreadsheet
df = pd.read_excel("Pennsylvania_search.xlsx", engine="openpyxl")
df.rename(columns= {"Email": "email"},
          inplace=True)

# csv file containing email & domain data from web crawler
contacts = pd.read_csv("scraped_emails_domains.csv")
contacts.columns = ['email','website']

# removing useless entries
remove = ['jquery','typeahead','slick-carousel',
          'moment','handlebars','bootstrap','picturefill',
          'focus-within-polyfill','wixofday','core-js-bundle',
          'lodash','wixpress', 'search-insights',
          'requirejs','fancybox', 'web-vitals']
contacts = contacts[~contacts.email.str.contains('|'.join(remove))]

# merging yellow pages scrape data with email crawler data
output = (
    df
        .drop(columns=['email'])  #  this is empty and needs to be overwritten
        .merge(
            contacts.groupby('website', as_index=False).first(),  # just the first email
            on='website', how='left'  # left-join -> keep all rows from spreadsheet
        )
        .loc[:, df.columns] # get your original column order back
)

del output['Column1']

output.to_excel("Pennsylvania_search_edit.xlsx")