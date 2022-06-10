#!/usr/bin/python3


def uniq_add(my_list=[]):
    uniq = dict()
    for element in my_list:
        if not uniq.get(element):
            uniq[element] = my_list.count(element)
    return sum(uniq.keys())
