#!/usr/bin/python3
"""Module prints triangle"""

def pascal_triangle(n):
    """Returns list of lists of integers"""
    if n <= 0:
        return []

    triangle = [[1]]  # 1st row

    for i in range(1, n):
        row = [1]  # All rows beggin with 1
        prev_row = triangle[i - 1]

        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])

        row.append(1)  # All rows end in 1
        triangle.append(row)

    return triangle
