#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    """ Function that prints a matrix of integers"""

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            print('{}'.format(matrix[row][col]), end=" ")
        print()
