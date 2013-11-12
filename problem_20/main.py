__author__ = 'flaviocaetano'

from datetime import datetime


def factorial(x):
    if x == 1:
        return 1

    return x * factorial(x-1)


if __name__ == '__main__':
    t0 = datetime.now()

    fact = factorial(100)
    result = sum(map(int, str(fact)))

    t1 = datetime.now() - t0

    print 'result: %s (%ss)' % (result, t1)
