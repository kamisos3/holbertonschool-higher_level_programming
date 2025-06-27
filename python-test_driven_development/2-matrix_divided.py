#!/usr/bin/python3
"""
This module defines a function to divide elements of a matrix.
"""


def matrix_divided(matrix, div):
"""
    Divides all elements of a matrix by a number.

    Each element in the matrix must be an integer or float.
    The matrix must be a list of lists with rows of the same size.
    The result is a new matrix with elements rounded to 2 decimal places.

    Args:
        matrix (list of lists): The matrix to divide.
        div (int or float): The number to divide by.

    Returns:
        list of lists: A new matrix with divided values.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                   or if div is not a number.
        TypeError: If rows are not the same size.
        ZeroDivisionError: If div is 0.
    """
if not isinstance(matrix, list)
    or not all(isinstance(row, list) for row in matrix):
    raise TypeError
    ("matrix must be a matrix (list of lists) of integers/floats")

    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError
        ("matrix must be a matrix (list of lists) of integers/floats")

    row_length = len(matrix[0])
    if any(len(row) != row_length for row in matrix):
        raise TypeError
        ("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num / div, 2) for num in row] for row in matrix]
