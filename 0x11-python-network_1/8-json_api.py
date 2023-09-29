#!/usr/bin/python3
"""
Takes in a letter and sends a POST request using 'requests' module to an URL
with the letter as a parameter.
"""

import sys
import requests

if __name__ == "__main__":

    url = sys.argv[1]

    if len(sys.argv) == 2:
        value = sys.argv[1]
    else:
        value = ""

    data = {"q": value}
    response = requests.post(url, data=data)

    try:
        json_data = response.json()
        if json_data:
            id_ = json_data.get("id")
            name = json_data.get("name")
            print("[{}] {}".format(id_, name))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
