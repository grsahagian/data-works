
# from https://github.com/vdyagilev/RedditMBTI

from praw import Reddit




class SubredditPuller:
    """ Methods to pull a List of Reddit posts from a subreddit """

    def __init__(self):
        """ Initialize SubredditPuller """

        # Create the Reddit class provided by PRAWN

        # Import credentials from 'praw.ini' file
        self.reddit = Reddit(user_agent='crypto-bot by /u/JAWB-PLS', site_name='DEFAULT', client_id="2Orzi_6gQgmBGg", client_secret="mkW-uohIO5Bcg-4E7z_DsV04Tas0LQ", password="Candycrystal5446^", username="JAWB-PLS")

        # Set account only able to view posts
        self.reddit.read_only = True

    def pull_subreddit(self, subreddit, limit):
        """ Pull limit number of posts from specified subreddit. If limit==None, it'll tr to pull the max possible posts"""

        s = self.reddit.subreddit(subreddit)
        posts = []
        for submission in s.top('all', limit=limit):
            posts.append(submission)
        return posts
