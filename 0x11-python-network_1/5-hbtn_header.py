#!/usr/bin/python3
"""
Takes in a URL, sends a request to the UR using 'requests' module
and displays the value of a variable found in the header of the response.
"""

import sys
from urllib import request

if __name__ == "__main__":

    url = sys.argv[1]

    response = requests.get(url)
    content = response.headers.get('X-Request-Id')

    print("{}".format(content))
