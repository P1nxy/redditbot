import praw

r = praw.reddit(user_agent = "Schoolbot by Marek /u/P3nxy")
r.login()

def run_bot():
    subreddit = r.get subreddit("test")
    comment = subreddit.get_comments(limit=25)
    for comment in comments: