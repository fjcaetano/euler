__author__ = 'Flavio'

from datetime import datetime


def sum_multiples_of_3_and_5(param):
    '''
    Sum all multiples of 3 and 5 below the given number.
    '''

    i = 1
    result = 0
    while i < param:

        if i % 3 == 0 or i % 5 == 0:
            result += i

        i += 1

    return result

if __name__ == '__main__':
    t0 = datetime.now()

    result = sum_multiples_of_3_and_5(1000)

    t1 = datetime.now() - t0

    print 'result: %d (%ss)' % (result, t1)
