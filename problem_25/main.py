__author__ = 'flaviocaetano'

from datetime import datetime


def fibonacci(nth):
    '''
    '''

    last = fib = 1

    i = 1
    while len(str(fib)) < nth:
        fib += last
        last = fib - last

        i += 1

    return i+1, fib


if __name__ == '__main__':
    t0 = datetime.now()

    result = fibonacci(1000)

    t1 = datetime.now() - t0

    print 'result: %s (%ss)' % (result, t1)
