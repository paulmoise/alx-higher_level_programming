#!/usr/bin/python3


def no_c(my_string):
    """Function that remove all characters c and C from string"""
    s = ""
    for char in my_string:
        if char not in ['c', 'C']:
            s+=char;
    return s;

