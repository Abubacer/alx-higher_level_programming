#!/usr/bin/python3
"""Defines a script that adds all arguments to a Python list.
"""
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    pyth_list = load_from_json_file(filename)
except Exception:
    pyth_list = []

pyth_list.extend(sys.argv[1:])
save_to_json_file(pyth_list,  filename)
