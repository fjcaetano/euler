__author__ = 'Flavio'

from datetime import datetime


def sum_squares(num):
    '''
    Sum the squares of all numbers <= num
    '''

    return reduce(lambda x, y: x+y, map(lambda x: x**2, range(1, num+1)))


def square_sum(num):
    '''
    Square the sum of all numbers <= num
    '''

    return reduce(lambda x, y: x+y, range(1, num+1)) ** 2


if __name__ == '__main__':
    t0 = datetime.now()

    num = 100
    result = square_sum(num) - sum_squares(num)

    t1 = datetime.now() - t0

    print 'result: %d (%ss)' % (result, t1)