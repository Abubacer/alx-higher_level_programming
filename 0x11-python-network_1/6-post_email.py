#!/usr/bin/python3
"""
Takes in a URL, sends a POST request using 'requests' module to the passed URL
with the email as a parameter, and displays the body of the response decoded.
"""

import sys
import requests

if __name__ == "__main__":

    url = sys.argv[1]
    email = sys.argv[2]
    value = {'email': email}

    response = requests.put(url, data=value)
    content = response.text

    print("{}".format(content))
