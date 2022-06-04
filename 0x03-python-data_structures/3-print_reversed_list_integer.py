#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    """ Function that prints all integers of a list, in reverse"""

    for idx in range(len(my_list) - 1, -1, -1):
        print('{:d}'.format(my_list[idx]))
