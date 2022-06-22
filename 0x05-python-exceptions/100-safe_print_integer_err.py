#!/usr/bin/python3


def safe_print_integer_err(value):
    """
    Function that print integer
    """
    try:
        print("{:d}".format(value))
        return True
    except ValueError as e:
        print("Exception:{}".format(e))
        return False
