#!/usr/bin/python3
""" Square with one attribute"""


class Square:
    """ Class to represent square"""

    def __init__(self, size=0, position=(0, 0)):
        """Function to initialize optionnaly with size or position

        Args:
            size (int) : size of the square
            position (int, int) : the position of the square
        """
        self.__position = position
        self.__size = size

    @property
    def size(self):
        """ size getter

            Args:
                 self: the active instance of the class

            Returns:
                    size (int): size of the area
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setter of size attribute

            Args:
                self: the active instance of the class
                value (int) : the value of the size to be set
        """

        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    @property
    def position(self):
        """ Getter for position property """
        return self.__position

    @position.setter
    def position(self, value):
        """ Setter for the position property """
        if isinstance(value, tuple) and\
                len(value) == 2 and\
                all(isinstance(el, int) for el in value) and\
                value > (0, 0):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """ Function that returns the current square area

            Args:
                self (Square) : the active instance of the class

            Returns:
                 area (int): return the area of the square
        """
        return (self.__size ** 2)

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()

            for i in range(self.__size):
                print(" "*self.__position[0], end="")
                for j in range(self.__size):
                    print('#', end="")
                print()
