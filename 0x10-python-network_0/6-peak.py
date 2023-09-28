#!/usr/bin/python3
"""
A divide-and-conquer algorithm that efficiently finds a peak value
in an unsorted list of integers.

The algorithm has a time complexity of O(log n) because it efficiently divides
the search space in half with each iteration. This makes it very efficient for
finding a peak value in lists, as the number of elements to examine decreases
exponentially with each step.
"""


def find_peak(list_of_integers):
    """
    Find peaks in a list of unsorted ints.

    Args:
        list_of_integers (list): A list of unsorted ints.

    Returns:
        int: The peak value.
    """
    if not list_of_integers:
        return None

    left, right = 0, len(list_of_integers) - 1

    while left < right:
        midlle = left + (right - left) // 2

        if list_of_integers[midlle] < list_of_integers[midlle + 1]:
            left = midlle + 1
        else:
            right = midlle

    return list_of_integers[left]
