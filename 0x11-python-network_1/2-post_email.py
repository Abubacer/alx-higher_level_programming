#!/usr/bin/python3
"""
Takes in a URL, sends a POST request to the passed URL with the email
as a parameter, and displays the body of the response decoded.
"""

import sys
from urllib import request, parse

if __name__ == "__main__":

    url = sys.argv[1]
    email = sys.argv[2]
    value = {'email': email}

    encoded_data = parse.urlencode(value).encode('utf-8')

    with request.urlopen(url, encoded_data) as response:
        content = response.read().decode('utf-8')

        print("{}".format(content))
