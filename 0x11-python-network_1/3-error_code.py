#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL, displays the body of the response
decoded, manages urllib.error.HTTPError exceptions and print the status code.
"""

import sys
from urllib import request, error

if __name__ == "__main__":

    url = sys.argv[1]

    try:
        with request.urlopen(url) as response:
            content = response.read().decode('utf-8')

            print("{}".format(content))

    except error.HTTPError as exc:
        print("Error code: {}".format(exc.code))
