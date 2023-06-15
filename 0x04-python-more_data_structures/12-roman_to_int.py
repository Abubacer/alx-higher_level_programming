#!/usr/bin/python3

def roman_to_int(roman_string):
    # a function that converts a Roman numeral to an integer.
    roman_num = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    conversion = 0
    last_value = 0

    for char in reversed(roman_string):
        if char not in roman_num:
            return 0

        int_value = roman_num[char]

        if int_value < last_value:
            conversion -= int_value
        else:
            conversion += int_value

        last_value = int_value

    return conversion
