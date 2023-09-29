#!/usr/bin/python3
"""
Lists 10 commits from the most recent to oldest of the repo “rails” by the user
“rails”, and Prints all commits one by line by: `<sha>: <author name>`.
"""

import sys
import requests

if __name__ == "__main__":

    # https://api.github.com/repos/OWNER/REPO/commits
    url = f'https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits'
    params = {"per_page": 10, }

    response = requests.get(url, params=params)
    commits_list = response.json()

    for commit in commits_list:
        sha = commit.get("sha")
        author_name = commit.get("commit").get("author").get("name")
        print("{}: {}".format(sha, author_name))
