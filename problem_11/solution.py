__author__ = 'flaviocaetano'

from datetime import datetime


def build_adj(grid, i, j, length):
    yield [grid[i-n][j] for n in range(0, length) if i - n > 0]                                     # North
    yield [grid[i+n][j] for n in range(0, length) if i + n < len(grid)]                             # South
    yield [grid[i][j-n] for n in range(0, length) if j - n > 0]                                     # East
    yield [grid[i][j+n] for n in range(0, length) if j + n < len(grid[i])]                          # West

    yield [grid[i-n][j-n] for n in range(0, length) if i - n > 0 and j - n > 0]                     # Northeast
    yield [grid[i+n][j-n] for n in range(0, length) if i + n < len(grid) and j - n > 0]             # Southeast
    yield [grid[i-n][j+n] for n in range(0, length) if i - n > 0 and j + n < len(grid[i])]          # Northwest
    yield [grid[i+n][j+n] for n in range(0, length) if i + n < len(grid) and j + n < len(grid[i])]  # Southwest


def mult_adjacent(grid, length):
    '''
    '''

    result = -1
    mult = lambda a, b: a*b

    for i in range (0, len(grid)):
        for j in range(0, len(grid[i])):
            matrix = list(build_adj(grid, i, j, length))

            for line in matrix:
                if len(line) == length:
                    yield reduce(mult, line)


if __name__ == '__main__':
    t0 = datetime.now()

    result = None
    with open('grid.txt', 'r') as grid_file:
        grid = list()
        for line in grid_file.readlines():
            grid.append(map(int, line.split(' ')))

        result = max(mult_adjacent(grid, 4))

    t1 = datetime.now() - t0

    print 'result: %s (%ss)' % (result, t1)
