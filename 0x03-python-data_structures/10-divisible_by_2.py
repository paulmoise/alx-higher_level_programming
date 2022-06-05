#!/usr/bin/python3


def is_odd(n):
    """ function to check if number is odd """
    return (n % 2 == 0)


def divisible_by_2(my_list=[]):
    """Function that finds all multiples of 2 in a list"""

    return list(map(is_odd, my_list))
