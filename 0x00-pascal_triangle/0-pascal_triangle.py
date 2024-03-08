#!/usr/bin/python3
"""
Pascal's triangle.
"""


def pascal_triangle(n: int) -> list:
    """
    Returns a list of lists of ints representing the Pascal's triangle of n:
    Returns an empty list if n <= 0
    Assumes `n` will be always an integer
    """

    if not isinstance(n, int):
        raise TypeError(f"{n} is not an integer")
    if n <= 0:
        return ([])
    triangles = []
    for i in range(n):
        temp = []

        for j in range(i+1):
            if j == 0 or j == i:
                temp.append(1)
            else:
                temp.append(triangles[i-1][j-1] + triangles[i-1][j])
        triangles.append(temp)
    return triangles