#!/usr/bin/python3
# uppercase - a function that prints a string in uppercase.

def uppercase(str):
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            char = chr(ord(char) - 32)
        print("{}".format(char), end="")
    print("")
