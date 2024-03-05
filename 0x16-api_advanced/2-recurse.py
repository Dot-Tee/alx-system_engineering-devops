#!/usr/bin/python3
import requests

def recurse(subreddit, hot_list=[]):
    """
    Recursively queries the Reddit API and returns a list of hot article titles for a given subreddit.
    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list, optional): Accumulator for hot article titles. Defaults to an empty list.
    Returns:
        list or None: List of hot article titles or None if the subreddit is invalid or has no hot articles.
    """
    base_url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "MyRedditBot"}  # Add your custom User-Agent here
    try:
        response = requests.get(base_url, headers=headers)
        response_data = response.json()
        if "data" in response_data and "children" in response_data["data"]:
            children = response_data["data"]["children"]
            for child in children:
                title = child["data"]["title"]
                hot_list.append(title)
            if "after" in response_data["data"]:
                # Recursive call for the next page
                return recurse(subreddit, hot_list, after=response_data["data"]["after"])
            else:
                return hot_list
        else:
            return None  # Invalid subreddit or no hot articles
    except requests.RequestException:
        return None  # Error occurred during API request
# Example usage:
subreddit_name = "learnprogramming"
hot_articles = recurse(subreddit_name)
if hot_articles:
    for i, title in enumerate(hot_articles, start=1):
        print(f"{i}. {title}")
else:
    print(f"No hot articles found for subreddit '{subreddit_name}' or invalid subreddit.")
