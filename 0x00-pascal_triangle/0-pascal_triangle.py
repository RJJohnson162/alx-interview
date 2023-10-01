#!usr/bin/python3

"""
0.Pascal's Triangle
"""

def pascal_triangle(n):

    """
    return a list of integers representing the pascal's triangle of n
    """

    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = [1]
        if triangle:
            last_row = triangle[-1]
            row.extend([last_row[j] + last_row[j + 1] for j in range(len(last_row) - 1)])
            row.append(1)
        triangle.append(row)

    return triangle
(pascal_triangle(5))
