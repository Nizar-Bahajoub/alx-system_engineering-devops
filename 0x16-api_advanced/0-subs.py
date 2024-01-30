#!/usr/bin/python3
""" Getting Reddit data using Reddit API """


import requests


def number_of_subscribers(subreddit):
    """ Return the number of subscribers on a given subreddit """
    response = requests.get("https://www.reddit.com/r/{}/about.json".format(
                            subreddit),
                            headers={"User-Agent": "Nizar-Custom-User-Agent"},
                            allow_redirects=False)
    if response.status_code >= 300:
        return 0
    return response.json().get("data").get("subscribers")
