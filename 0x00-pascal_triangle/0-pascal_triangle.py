#!/usr/bin/python3

"""
module contains a function that returns a list of
integers representing the Pascal's triangle of n
"""


def pascal_triangle(n):
    """
        returns a list of lists of integers representing
        the Pascal’s triangle of n
    """

    pascal = []

    for i in range(n):
        row = [1]

        if pascal:
            prev_row = pascal[-1]
            for j in range(len(prev_row) - 1):
                row.append(prev_row[j] + prev_row[j+1])
            row.append(1)
        pascal.append(row)
    return pascal
