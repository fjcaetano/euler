__author__ = 'flaviocaetano'

from datetime import datetime


def max_adjacent(triangle):
    '''
    '''

    i = -1
    result = 0
    for line in triangle:
        if i == -1:
            i = 0
        else:
            if line[i+1] > line[i]:
                i += 1

        print line[i]
        result += line[i]

    return result


if __name__ == '__main__':
    t0 = datetime.now()

    result = 0
    triangle = list()
    with open('triangle.txt', 'r') as file:
        for line in file.readlines():
            triangle.append(map(int, line.split(' ')))

        result = max_adjacent(triangle)

    t1 = datetime.now() - t0

    print 'result: %s (%ss)' % (result, t1)
