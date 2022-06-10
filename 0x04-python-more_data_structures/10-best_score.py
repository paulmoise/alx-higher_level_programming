#!/usr/bin/python3


def best_score(a_dictionary):
    if not (a_dictionary and bool(a_dictionary)):
        return None

    max_value = max(list(a_dictionary.values()))
    for key, value in a_dictionary.items():
        if value == max_value:
            return key
