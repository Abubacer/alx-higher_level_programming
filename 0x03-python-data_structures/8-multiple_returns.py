#!/usr/bin/python3

def multiple_returns(sentence):
    # a function that returns a tuple with the length of a string
    # and its first character
    # if the string is empty the first character is set to None.
    if sentence == "":
        return (0,None)
    return len(sentence), sentence[0]
