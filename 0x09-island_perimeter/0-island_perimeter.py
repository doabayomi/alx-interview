#!/usr/bin/python3
"""Island perimeter algorithm"""


def island_perimeter(grid):
    """Finds the perimeter of an island in a grid
    """
    rows = len(grid)
    cols = len(grid[0])

    perimeter = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:

                try:
                    # check top
                    if i == 0 or grid[i - 1][j] == 0:
                        perimeter += 1
                    # check left
                    if j == 0 or grid[i][j - 1] == 0:
                        perimeter += 1
                    # check right
                    if j == cols - 1 or grid[i][j + 1] == 0:
                        perimeter += 1
                    # check bottom
                    if i == rows - 1 or grid[i + 1][j] == 0:
                        perimeter += 1
                except IndexError as e:
                    pass

    return perimeter
