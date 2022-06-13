#!/bin/usr/python3
def complex_delete(a_dictionary, value):
    """
    Function that deletes keys with a specific value in a dictionary
    """
    a_copy = a_dictionary.copy()
    for key, val in a_copy.items():
        if value == val:
            del a_dictionary[key]
    return a_dictionary
