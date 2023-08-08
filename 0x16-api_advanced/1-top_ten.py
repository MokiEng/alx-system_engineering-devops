#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    uurl = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {
        'User-Agent': 'CustomUserAgent'
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        
        print(f"Top 10 Hot Posts in r/{subreddit}:")
        for post in posts:
            title = post['data']['title']
            print(title)
    elif response.status_code == 404:
        print(f"Subreddit '{subreddit}' not found.")
    else:
        print(f"Error fetching data for subreddit '{subreddit}':
              {response.status_code}")
