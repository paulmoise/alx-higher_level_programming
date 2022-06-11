#!/usr/bin/python3


def roman_to_int(roman_string):
    symbols = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    if not (isinstance(roman_string, str)) or not roman_string:
        return (0)

    if len(roman_string) == 1:
        value = symbols.get(roman_string[0])
        if not value:
            return (0)
        else:
            return value

    nums = 0
    for i in range(1, len(roman_string)):
        curr = symbols.get(roman_string[i])
        prev = symbols.get(roman_string[i - 1])
        if not curr or not prev:
            return (0)

        if curr <= prev:
            nums += prev
        else:
            nums -= prev

        if i == len(roman_string) - 1:
            nums += curr
    return nums
