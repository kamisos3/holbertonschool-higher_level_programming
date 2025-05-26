#!/usr/bin/python3
"""
This module defines a function to divide elements of a matrix.
"""


def matrix_divided(matrix, div):
    """Divides elements of a matrix by divisor"""
    if not isinstance(matrix, list):
        raise TypeError
        ("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError
            ("matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        for elem in row:
            if type(elem) not in (int, float):
                raise TypeError
                ("matrix must be a matrix (list of lists) of integers/floats")

    # Check if all rows have the same size
    row_lengths = set(len(row) for row in matrix)
    if len(row_lengths) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number (int or float, not bool)
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Create the new matrix with rounded values
    new_matrix = []
    for row in matrix:
        new_row = []
        for elem in row:
            # Perform division and round to two decimal places
            new_elem = round(elem / div, 2)
            new_row.append(new_elem)
        new_matrix.append(new_row)

    return new_matrix
