#!/usr/bin/python3


def element_at(my_list, idx):
    """ Function that retrieve an element from a list"""
    if 0 <= idx < len(my_list):
        return my_list[idx]
    return None
