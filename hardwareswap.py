#!/usr/bin/env python3

import praw

from reddit_info import client_id, client_secret, username, password, user_agent

reddit = praw.Reddit(client_id=client_id,
                    client_secret=client_secret,
                    username=username,
                    password=password,
                    user_agent=user_agent)

def search_keyword(keyword):
        
    for submission in reddit.subreddit("hardwareswap").search(keyword, sort="new", limit=10):

        print(submission.title, submission.author, submission.url)
    
search_keyword("ryzen")