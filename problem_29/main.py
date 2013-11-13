__author__ = 'flaviocaetano'

from datetime import datetime


def comb(min, max):
    for a in range(min, max+1):
        for b in range(min, max+1):
            yield a**b


if __name__ == '__main__':
    t0 = datetime.now()

    result = len(set(comb(2, 100)))

    t1 = datetime.now() - t0

    print 'result: %s (%ss)' % (result, t1)
