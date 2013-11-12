__author__ = 'flaviocaetano'

from datetime import datetime

from problem_21.main import divisor_generator


def abundant_list(limit):
    '''
    Yields a list with the abundant numbers to the limit
    '''

    for i in xrange(limit):
        divisors_sum = sum(set(divisor_generator(i))) - i
        if divisors_sum > i:
            # Is abundant
            yield i


def calc(limit):
    abd_list = list(abundant_list(limit))
    abd_sum = set()

    for i, abd1 in enumerate(abd_list):
        for j, abd2 in enumerate(abd_list, start=i+1):
            abd_sum.add(abd1+abd2)

    return set(xrange(limit)) - abd_sum

if __name__ == '__main__':
    t0 = datetime.now()

    result = sum(calc(28123))

    t1 = datetime.now() - t0

    print 'result: %s (%ss)' % (result, t1)
