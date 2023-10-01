#!/usr/bin/python3

"""
0. Pascal's Triangle
"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the n-th row as a list of lists.

    Args:
    - n (int): The number of rows to generate.

    Returns:
    - List[List[int]]: Pascal's Triangle as a list of lists of integers.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[-1]
        current_row = [1] + [prev_row[j] + prev_row[j+1] for j in range(len(prev_row) - 1)] + [1]
        triangle.append(current_row)

    return triangle

(pascal_triangle(5))