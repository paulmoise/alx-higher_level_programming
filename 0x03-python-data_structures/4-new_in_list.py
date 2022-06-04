#!/usr/python3


def new_in_list(my_list, idx, element):
    """
    function that replaces an element in a list at specific position without
    modifying the original list
    ...
    Parameters
    ----------
    my_list : list
        The list of elements
    idx : integer
        The given position
    element : the new element
    Return:
        The original list if idx is negative or
        updated list
    """
    new_list = my_list.copy()
    if 0 <= idx < len(my_list):
        new_list[idx] = element
    return new_list
