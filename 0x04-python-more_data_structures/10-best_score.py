#!/usr/bin/python3


def best_score(a_dictionary):
    if not (a_dictionary and bool(a_dictionary)):
        return None
    return max(list(a_dictionary.keys()))
