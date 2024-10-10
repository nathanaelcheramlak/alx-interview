#!/usr/bin/python3


def island_perimeter(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    n = len(grid)
    m = len(grid[0])
    perimeter = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                if i == 0:
                    perimeter += 1
                elif grid[i-1][j] == 0:
                    perimeter += 1
                if i == n-1:
                    perimeter += 1
                elif grid[i+1][j] == 0:
                    perimeter += 1
                if j == 0:
                    perimeter += 1
                elif grid[i][j-1] == 0:
                    perimeter += 1
                if j == m-1:
                    perimeter += 1
                elif grid[i][j+1] == 0:
                    perimeter += 1
    return perimeter