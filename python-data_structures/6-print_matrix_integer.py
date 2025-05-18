#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        if not row:
            print()
            continue
        for i, value in enumerate(row):
            if i < len(row) - 1:
                print("{:d}".format(value), end=" ")
            else:
                print("{:d}".format(value))
