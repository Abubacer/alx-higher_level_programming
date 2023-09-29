#!/usr/bin/python3
"""
Fetches the URL: https://alx-intranet.hbtn.io/status using 'requests'
and displays the body of the response.
"""

import requests

if __name__ == "__main__":

    url = 'https://alx-intranet.hbtn.io/status'

    response = requests.get(url)
    content = response.text

    print("Body response:")
    print("	- type: {}".format(type(content)))
    print("	- content: {}".format(content))
