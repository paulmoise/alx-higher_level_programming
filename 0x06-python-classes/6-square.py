#!/usr/bin/python3
""" Square with one attribute"""


class Square:
    """ Square class with size attribute"""

    def __init__(self, size=0, position=(0, 0)):
        """
            Function to initialize square with it's size
        """
        if type(size) == int:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
                self.__position = position
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """ Function that returns the current square area

            Args:
                self: the active instance of the class

            Returns:
                 int: return the area of the square
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """ size getter

            Args:
                 self: the active instance of the class

            Returns:
                    int: size of the area
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setter of size attribute

            Args:
                self: the active instance of the class
                value: the value to be set

            Returns:
                    nothing
        """

        if type(value) == int:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print(" "*self.__position[0], end="")
                for j in range(self.__size):
                    print('#', end="")
                print()

    @property
    def position(self):
        """ Getter for position property """
        return self.__position

    @position.setter
    def position(self, value):
        """ Setter for the position property """
        if type(value) == tuple and value > (0, 0):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
