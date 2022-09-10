#!/usr/bin/python3
"""
Task  0. How many subs?
"""
import json
import requests


def number_of_subscribers(subreddit):
    """
    function that queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit.
    """
    url = 'https://www.reddit.com/r/{}.json'.format(subreddit)
    user_agent = 'reddit_user'

    headers = {'User-Agent': user_agent}

    req = requests.get(url, headers=headers, allow_redirects=False)

    if req.status_code != 200:
        return 0

    data = req.json()['data']
    page_list = data['children']
    page_data = page_list[0]['data']

    return page_data['subreddit_subscribers']
