#!/usr/bin/python3
'''
Returns the perimeter of the island based on `grid`
grid is a list of list of integers: 0 represents a water zone,
1 represents a land zone, One cell is a square with side length 1,
Grid cells are connected horizontally/vertically (not diagonally).
Grid is rectangular, width and height don’t exceed 100
Grid is completely surrounded by water, and there is one island
(or nothing). The island doesn’t have “lakes”(water inside that
isn’t connected to the water around the island).
'''


def island_perimeter(grid):
    '''
    computes the perimeter of the island described in the grid.

    args:
        grid: list of list of integers representing the island.

    returns:
        the perimeter of the island.

    '''

    perimeter = 0
    rows, cols = len(grid), len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4
                # Check adjacent cells
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter
