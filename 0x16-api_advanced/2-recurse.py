#!/usr/bin/python3
"""a recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Returns a list of titles of all hot posts on a given subreddit."""
    if hot_list is None:
        hot_list = []
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {
        'User-Agent': 'CustomUserAgent'
    }
    if after:
        url += f'&after={after}'

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        for post in posts:
            title = post['data']['title']
            hot_list.append(title)

        after = data['data']['after']
        if after:
            recurse(subreddit, hot_list, after)
        else:
            return hot_list
    elif response.status_code == 404:
        print(f"Subreddit '{subreddit}' not found.")
        return None
    else:
        print(f"Error fetching data for subreddit
                '{subreddit}': {response.status_code}")
        return None
