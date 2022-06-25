#!/usr/bin/python3
""" Square with one attribute"""


class Square:
    """ Square class with size attribute"""

    def __init__(self, size=0):
        """
            function to initialize square with it's size
        """
        if type(size) == int:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")
