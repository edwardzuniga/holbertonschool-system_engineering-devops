#!/usr/bin/python3
'''
Task 1. Top Ten
'''
import requests


def top_ten(subreddit):
    '''
    Top 10 posts  in subreddit
    '''
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    user_agent = 'reddit_user'

    headers = {'User-Agent': user_agent}

    req = requests.get(url, headers=headers, allow_redirects=False)

    if req.status_code != 200:
        print('None')
    else:
        data = req.json()['data']
        post_list = data['children']

        for posts in post_list[0:10]:
            print(posts['data']['title'])
