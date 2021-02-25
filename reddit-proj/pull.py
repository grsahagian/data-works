from SubredditPuller import SubredditPuller

import pandas as pd
from tqdm import tqdm

s = SubredditPuller()
subrs = ['bitcoin', 'ethereum' , 'xrp']




def download_data():
    # Create DataFrames for each subreddit and their posts
    subreddit_df = pd.DataFrame(columns=['label', 'text'])


    for subr in tqdm(subrs):
        posts = s.pull_subreddit(subr, limit=1000)

        print(subr)
        for subm in tqdm(posts):

            # Delete posts with just a title, and merge the title into the text for the rest

            yes_text = True
            if subm.selftext == "":
                yes_text = False
            else:
                subm.selftext = subm.title + " " + subm.selftext

            if yes_text:
                append_df = pd.DataFrame([[subr, subm.selftext,]], columns=['label', 'text'])

                subreddit_df = pd.concat([subreddit_df, append_df])

                subreddit_df.to_csv('subreddit_data.csv')


def load_data():
    """ Use to load up your saved dataset """
    return pd.read_csv('subreddit_data.csv')


download_data()
