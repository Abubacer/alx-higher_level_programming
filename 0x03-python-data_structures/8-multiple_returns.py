#!/usr/bin/python3
"""multiple_returns - a function that returns a tuple
with the length of a string and its first character.
"""


def multiple_returns(sentence):
    if sentence == "":
        return None
    return len(sentence), sentence[0]
