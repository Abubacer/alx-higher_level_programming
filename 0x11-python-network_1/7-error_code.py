#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL using 'requests' module, displays
the body of the response, and print the status code if it is >= to 400.
"""

import sys
import requests

if __name__ == "__main__":

    url = sys.argv[1]

    response = requests.get(url)

    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))

    else:
        content = response.text
        print("{}".format(content))
