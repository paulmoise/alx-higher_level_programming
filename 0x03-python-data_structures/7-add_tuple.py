#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    """function that adds 2 tuples"""

    a, b = tuple_a, tuple_b
    if len(tuple_a) < 2:
        a = tuple_a + (0,)*(2 - len(tuple_a))
    if len(tuple_b) < 2:
        b = tuple_b + (0,)*(2 - len(tuple_b))

    res = list()
    for i in range(2):
        res.append(a[i] + b[i])

    return tuple(res)
