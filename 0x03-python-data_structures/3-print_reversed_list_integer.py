#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    """ Function that prints all integers of a list, in reverse"""
    my_list.reverse()
    if isinstance(my_list, list):
        for element in my_list:
            print("{:d}".format(element))
