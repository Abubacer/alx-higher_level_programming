#!/usr/bin/python3
"""
Takes user GitHub credentials (username and password) and uses the GitHub API
to display user id.
"""

import sys
import requests

if __name__ == "__main__":

    url = 'https://api.github.com/user'

    credentials = (sys.argv[1], sys.argv[2])
    response = requests.get(url, auth=credentials)
    my_id = response.json().get("id")
    print("{}".format(my_id))
