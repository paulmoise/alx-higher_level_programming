#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    """ Function that prints all integers of a list, in reverse"""
    for idx in range(1, len(my_list) + 1):
        print('{:d}'.format(my_list[-idx]))
