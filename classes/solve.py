def findNextCellToFill(grid, i, j):
    for x in range(i, 9):
        for y in range(j, 9):
            if grid[x][y] == 0:
                return x, y

    for x in range(0, 9):
        for y in range(0, 9):
            if grid[x][y] == 0:
                return x, y

    return -1, -1


def isValid(grid, i, j, val):
    rowValid = all([val != grid[i][x] for x in range(9)])
    if rowValid:
        columnValid = all([val != grid[x][j] for x in range(9)])
        if columnValid:
            # Find top left coord for the square
            sqrTopX, sqrTopY = 3*(i//3), 3 * (j//3)
            for x in range(sqrTopX, sqrTopX+3):
                for y in range(sqrTopY, sqrTopY+3):
                    if grid[x][y] == val:
                        return False
            return True
    return False


def solve(grid, i=0, j=0):
    i, j = findNextCellToFill(grid, i, j)
    if i == -1:
        return True
    for val in range(1, 10):
        if isValid(grid, i, j, val):
            grid[i][j] = val
            if solve(grid, i, j):
                return grid
            grid[i][j] = 0
    return False
